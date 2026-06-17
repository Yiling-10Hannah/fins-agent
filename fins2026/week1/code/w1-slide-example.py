# 导入pandas库
import pandas as pd

# Step1：读取原始CSV文件
panel = pd.read_csv(
    "fins2026/week1/data/week1_workshop_panel.csv",
    parse_dates=["Date"],   # 自动把Date列识别为【日期格式】，不再是字符串
    dayfirst=True,          # 核心关键：日期DD/MM/YYYY，03/01/2000=1月3日（日在前，不加则识别成3月1日）
)

# Step2-1：去重，【同一天+同一只股票只保留1行】，删掉重复脏数据
panel = panel.drop_duplicates(subset=["Date", "Ticker"])
# 原始26159行 → 删除3条重复 → 26156行（CRSP权威数据库也自带脏数据，DFF清洗必要性）

# Step2-2：按股票、日期升序规整排序
panel = panel.sort_values(["Ticker", "Date"]).reset_index(drop=True)

# Step2-3：保存为parquet格式
panel.to_parquet("fins2026/week1/data/week1_workshop_panel.parquet")

# 结果校验
print(panel.shape)    # 输出(26156,6)：26156行、6列
print(panel.dtypes["Date"]) # datetime64[us]：日期格式永久保存在parquet里

# Step3：Query with DuckDB
import duckdb

#写法一：
ranks = duckdb.sql("""
  SELECT Ticker,
    AVG(Price)    AS mean_price,    -- 股票平均股价
    STDDEV_POP(Price) AS sd_price,   -- 总体标准差（分母N）
    COUNT(*)      AS n_days         -- 有效交易日总数
    FROM 'fins2026/week1/data/week1_workshop_panel.parquet'
    GROUP BY Ticker ORDER BY mean_price DESC; -- 按均价从高到低排序
""").df()
# Ticker mean_price sd_price n_days
# AAPL   177.44      144.62   6539  (NVDA, MSFT, ORCL follow)

#写法二：Pandas 内存分组
ranks = (
    panel.groupby("Ticker")["Price"]
    .agg(mean_price="mean",
         sd_price=lambda s: s.std(ddof=0), # ddof=0：改成总体标准差，对齐DuckDB
         n_days="size")
    .sort_values("mean_price",ascending=False)
    .reset_index()
)

# Step4: slice
#Time-series: Apple alone, all dates
aapl_timeseries = panel[panel["Ticker"] == "AAPL"].sort_values("Date")
print(aapl_timeseries.shape) # (6539,6)：6539行=苹果全部历史日线

#Cross-section:all tickers on the COVID-crash Monday
cross_section = panel[panel["Date"] == "2020-03-16"]
# 只查看三列关键数据
cross_section[["Ticker","Price","TotalReturn"]]

# Step5+Step6：长→宽转换 + 复利计算 + 对数绘图

wide_return = panel.pivot(
    index="Date",
    columns="Ticker",
    values="TotalReturn"
).dropna()

# 期初本金=1美元，(1+单日收益)不断相乘
growth = (1 + wide_return).cumprod()
# 期末2025年末资产结果
growth.tail(1).round(2)

#对数绘图
growth.plot(
    title="Tech 4 growth of $1, 2000-2025",
    logy=True, # 关键：Y轴对数刻度
    ylabel="value of $1 (log)"
)
