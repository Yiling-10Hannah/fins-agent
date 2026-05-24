# Week 3 Data

Week 3's main app now keeps its deploy-safe fixture inputs in this folder:

- `australia_macro_stage1_long.csv`: committed Australia Stage 1 source table
  used to rebuild the fixture Australia monthly and quarterly forecast panels
- `benchmark_leaderboard_fixture.csv`: committed Week 3 default-sample
  benchmark leaderboard used for the fast fixture app path

Week 3 also uses:

- frozen U.S. validation datasets from `fintools.datasets`
- optional live RBA and FRED refreshes when the app or scripts run in live mode

Keep future committed source inputs here and document their columns and timing
contracts explicitly.
