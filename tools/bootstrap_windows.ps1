$ErrorActionPreference = "Stop"

Write-Host "Bootstrapping fins-agent with Python 3.13 and pip..."

if (-not (Test-Path (Join-Path $PWD "pyproject.toml")) -or
    -not (Test-Path (Join-Path $PWD "tools\setup_student.py"))) {
    Write-Host "This script must be run from the fins-agent repo root."
    Write-Host "Expected to find pyproject.toml and tools\setup_student.py in:"
    Write-Host "  $PWD"
    Write-Host "Fix: cd into the cloned fins-agent folder, then rerun."
    exit 1
}

if ($PWD.Path -match "(?i)OneDrive") {
    Write-Host ""
    Write-Host "Note: this repo is inside a OneDrive-synced folder."
    Write-Host "OneDrive can lock files during 'pip install' and cause"
    Write-Host "'Access is denied' or 'file in use' errors. If bootstrap"
    Write-Host "fails with those errors, pause OneDrive sync and rerun,"
    Write-Host "or move the repo to a non-synced path such as C:\fins-agent."
    Write-Host ""
}

function Test-RipgrepWorks {
    if (-not (Get-Command rg -ErrorAction SilentlyContinue)) {
        return $false
    }

    try {
        $version = @(& rg --version 2>$null)
        if ($LASTEXITCODE -ne 0 -or $version.Count -eq 0) {
            return $false
        }
        $rgFiles = @(& rg --files -g AGENTS.md 2>$null)
        if ($LASTEXITCODE -ne 0 -or -not ($rgFiles -match "AGENTS.md")) {
            return $false
        }
        Write-Host "ripgrep ready: $($version[0])"
        return $true
    } catch {
        return $false
    }
}

function Ensure-RipgrepRecommendedTool {
    Write-Host "Checking optional AI search tool: ripgrep..."
    if (Test-RipgrepWorks) {
        return
    }

    Write-Host "Warning: ripgrep (rg) is not available yet."
    Write-Host "AI assistants can still work, but repo search will be slower."
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        Write-Host "Suggested install after setup: winget install --id BurntSushi.ripgrep.MSVC -e"
        Write-Host "If winget is missing, update Windows or install App Installer."
        return
    }

    Write-Host "Trying to install ripgrep for faster AI-assisted repo search..."
    & winget install --id BurntSushi.ripgrep.MSVC -e --source winget --accept-source-agreements --accept-package-agreements
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Warning: could not install ripgrep automatically. Continuing setup."
        Write-Host "Suggested install later: winget install --id BurntSushi.ripgrep.MSVC -e"
        return
    }

    if (-not (Test-RipgrepWorks)) {
        Write-Host "Warning: ripgrep installed, but this shell cannot run rg yet."
        Write-Host "Close and reopen PowerShell or PyCharm, then run: rg --version"
    }
}

Ensure-RipgrepRecommendedTool

function Get-VenvLockHolders {
    $venvPath = Join-Path $PWD ".venv"
    if (-not (Test-Path $venvPath)) {
        return @()
    }

    $resolvedVenv = [System.IO.Path]::GetFullPath($venvPath).ToLowerInvariant()
    try {
        return @(
            Get-CimInstance Win32_Process |
                Where-Object {
                    $_.ProcessId -ne $PID -and
                    $_.CommandLine -and
                    $_.CommandLine.ToLowerInvariant().Contains($resolvedVenv)
                } |
                Select-Object ProcessId, Name, CommandLine
        )
    } catch {
        Write-Host "Could not check whether .venv is in use:"
        Write-Host "  $($_.Exception.Message)"
        Write-Host "Close PyCharm Python Console tabs, notebooks, Streamlit apps, and terminals using .venv, then rerun setup."
        exit 1
    }
}

function Assert-VenvUnlocked {
    $holders = @(Get-VenvLockHolders)
    if ($holders.Count -eq 0) {
        return
    }

    Write-Host ""
    Write-Host "The repo virtual environment is currently in use."
    foreach ($holder in $holders) {
        Write-Host "  PID $($holder.ProcessId): $($holder.Name)"
        if ($holder.CommandLine) {
            $summary = [string]::Join(" ", $holder.CommandLine.Split())
            if ($summary.Length -gt 180) {
                $summary = $summary.Substring(0, 177) + "..."
            }
            Write-Host "    $summary"
        }
    }
    Write-Host ""
    Write-Host "Close PyCharm Python Console tabs, notebooks, Streamlit apps, and terminals using .venv, then rerun setup."
    exit 1
}

$venvPython = Join-Path $PWD ".venv\Scripts\python.exe"
if (Test-Path $venvPython) {
    Write-Host "Checking existing .venv before rebuilding..."
    & $venvPython tools/setup_student.py
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Existing .venv passed setup checks; bootstrap complete."
        exit 0
    }
    Write-Host "Existing .venv did not pass setup checks; bootstrap will repair it."
}

$pythonCommand = $null
$pythonArgs = @()
$tempRoot = Join-Path $PWD ".tmp-bootstrap\bootstrap-$PID"

New-Item -ItemType Directory -Force -Path $tempRoot | Out-Null
$env:TEMP = $tempRoot
$env:TMP = $tempRoot

if (Get-Command py -ErrorAction SilentlyContinue) {
    try {
        $pyVersion = (& py -3.13 --version 2>$null)
        if ($LASTEXITCODE -eq 0 -and $pyVersion -like "Python 3.13*") {
            $pythonCommand = "py"
            $pythonArgs = @("-3.13")
        }
    } catch {
        $pyVersion = $null
    }
}

if (-not $pythonCommand -and (Get-Command python -ErrorAction SilentlyContinue)) {
    $pythonPath = (Get-Command python).Source
    if ($pythonPath -and $pythonPath -match "(?i)WindowsApps") {
        Write-Host "The 'python' command on PATH points to the Microsoft Store stub:"
        Write-Host "  $pythonPath"
        Write-Host "That stub opens the Store instead of running Python."
        Write-Host "Install Python 3.13 with: winget install Python.Python.3.13"
        Write-Host "Then close this terminal, open a new one, and rerun."
        exit 1
    }
    try {
        $pythonVersion = (& python --version 2>$null)
        if ($LASTEXITCODE -eq 0 -and $pythonVersion -like "Python 3.13*") {
            $pythonCommand = "python"
        }
    } catch {
        $pythonVersion = $null
    }
}

if (-not $pythonCommand) {
    Write-Host "Python 3.13 was not found."
    Write-Host "Install it first with: winget install Python.Python.3.13"
    exit 1
}

$bundledPip = (& $pythonCommand @pythonArgs -c "import ensurepip, pathlib; d = pathlib.Path(ensurepip.__file__).resolve().parent / '_bundled'; print(sorted(d.glob('pip-*.whl'))[-1])")
if ($LASTEXITCODE -ne 0 -or -not $bundledPip) {
    throw "Failed to locate the bundled pip wheel"
}

Assert-VenvUnlocked

& $pythonCommand @pythonArgs -m venv --clear --without-pip .venv
if ($LASTEXITCODE -ne 0) {
    throw "Failed to create .venv"
}

& $pythonCommand @pythonArgs -m pip --python $venvPython install $bundledPip
if ($LASTEXITCODE -ne 0) {
    throw "Failed to seed pip in .venv"
}

& $venvPython -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) {
    throw "Failed to upgrade pip in .venv"
}

& $venvPython -m pip install -r requirements.txt -r requirements-dev.txt
if ($LASTEXITCODE -ne 0) {
    throw "Failed to install requirements"
}

& $venvPython tools/setup_student.py
exit $LASTEXITCODE
