param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path,
    [string]$PersonalSkillsDir = (Join-Path $HOME '.codex\skills'),
    [switch]$DryRun,
    [switch]$PruneStale
)

$ErrorActionPreference = 'Stop'

$skillsDir = Join-Path $RepoRoot 'skills'
if (-not (Test-Path -LiteralPath $skillsDir -PathType Container)) {
    throw "Missing skills directory: $skillsDir"
}

if (-not (Test-Path -LiteralPath $PersonalSkillsDir -PathType Container)) {
    if ($DryRun) {
        Write-Output "CREATE directory $PersonalSkillsDir"
    } else {
        New-Item -ItemType Directory -Path $PersonalSkillsDir | Out-Null
    }
}

$created = 0
$skipped = 0
$failed = 0
$pruned = 0
$stale = 0

$skillsRoot = [System.IO.Path]::GetFullPath($skillsDir).TrimEnd('\')
$skillsRootPrefix = "$skillsRoot\"
$currentSkillNames = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)

Get-ChildItem -LiteralPath $skillsDir -Directory | Sort-Object Name | ForEach-Object {
    [void]$currentSkillNames.Add($_.Name)
    $source = $_.FullName
    $dest = Join-Path $PersonalSkillsDir $_.Name

    if (Test-Path -LiteralPath $dest) {
        $item = Get-Item -LiteralPath $dest -Force
        $target = @($item.Target)[0]
        if ($item.LinkType -eq 'Junction' -and $target -eq $source) {
            Write-Output "OK $($_.Name) -> $source"
            $script:skipped += 1
            return
        }

        Write-Error "Refusing to replace existing path: $dest"
        $script:failed += 1
        return
    }

    if ($DryRun) {
        Write-Output "CREATE $dest -> $source"
    } else {
        New-Item -ItemType Junction -Path $dest -Target $source | Out-Null
        Write-Output "CREATED $($_.Name) -> $source"
    }
    $script:created += 1
}

Get-ChildItem -LiteralPath $PersonalSkillsDir -Force | Where-Object { $_.Name -like 'cflow*' } | Sort-Object Name | ForEach-Object {
    if ($currentSkillNames.Contains($_.Name)) {
        return
    }

    $target = @($_.Target)[0]
    if ($_.LinkType -ne 'Junction' -or -not $target) {
        return
    }

    $targetFullPath = [System.IO.Path]::GetFullPath($target)
    $pointsIntoCflowSkills = $targetFullPath.Equals($skillsRoot, [System.StringComparison]::OrdinalIgnoreCase) -or
        $targetFullPath.StartsWith($skillsRootPrefix, [System.StringComparison]::OrdinalIgnoreCase)

    if (-not $pointsIntoCflowSkills) {
        return
    }

    if (Test-Path -LiteralPath $targetFullPath) {
        return
    }

    $script:stale += 1
    if ($PruneStale) {
        if ($DryRun) {
            Write-Output "PRUNE $($_.FullName) -> $targetFullPath"
        } else {
            Remove-Item -LiteralPath $_.FullName -Force
            Write-Output "PRUNED $($_.Name) -> $targetFullPath"
        }
        $script:pruned += 1
    } else {
        Write-Output "STALE $($_.Name) -> $targetFullPath (run with -PruneStale to remove)"
    }
}

if ($failed -gt 0) {
    Write-Error "$failed link(s) failed"
    exit 1
}

Write-Output "Done. created=$created skipped=$skipped stale=$stale pruned=$pruned"
