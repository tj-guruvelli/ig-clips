# run-daily.ps1 — local Windows runner for ig-clips daily discovery.
#
# Registered by scripts/scheduler.ps1 (schtasks.exe-based). Runs the pipeline
# with system Python and logs to logs/discovery-YYYY-MM-DD.log.
#
# KNOWN GAP (as of 2026-07-07): no local venv exists yet for this pipeline.
# requirements.txt needs `playwright` (+ `playwright install` for browser
# binaries), `requests`, `python-dotenv`. First scheduled run WILL fail with
# ModuleNotFoundError until dependencies are installed. See README.md "Setup".
[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [string]$RepoRoot
)

$ErrorActionPreference = "Continue"

if (-not $RepoRoot) {
    $RepoRoot = (Resolve-Path (Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Definition) "..")).Path
}
Set-Location $RepoRoot

$LogDir = Join-Path $RepoRoot "logs"
if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir | Out-Null }
$Date = Get-Date -Format "yyyy-MM-dd"
$LogFile = Join-Path $LogDir "discovery-$Date.log"

"[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] ig-clips run-daily starting" | Out-File -FilePath $LogFile -Append

# Prefer a local venv if one exists (Windows-native: Scripts\python.exe).
$VenvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
$PythonExe = if (Test-Path $VenvPython) { $VenvPython } else {
    $sys = (Get-Command py -ErrorAction SilentlyContinue)
    if ($sys) { "py" } else { "python" }
}

Push-Location (Join-Path $RepoRoot "src")
try {
    if ($PythonExe -eq "py") {
        & py -3.8 main.py 2>&1 | Tee-Object -FilePath $LogFile -Append
    } else {
        & $PythonExe main.py 2>&1 | Tee-Object -FilePath $LogFile -Append
    }
    $ExitCode = $LASTEXITCODE
} finally {
    Pop-Location
}

"[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] ig-clips run-daily exit $ExitCode" | Out-File -FilePath $LogFile -Append
exit $ExitCode
