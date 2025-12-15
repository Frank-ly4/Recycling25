# Spec-Kit command wrapper for Bangkok Recycling Business Plan (PowerShell version)

$REPO_ROOT = Split-Path -Parent $PSScriptRoot
$SPECS_DIR = Join-Path $REPO_ROOT "specs\001-bangkok-recycling"
$CURSOR_DIR = Join-Path $REPO_ROOT ".cursor"

function Print-Usage {
  Write-Host "Spec-Kit Command Wrapper"
  Write-Host "------------------------"
  Write-Host "Usage: .\scripts\speckit.ps1 [command]"
  Write-Host ""
  Write-Host "Available commands:"
  Write-Host "  run [agent_name]   - Run a specific agent (e.g., qa_probe_agent)"
  Write-Host "  implement          - Execute the full implementation plan"
  Write-Host "  status             - Check implementation status"
  Write-Host "  help               - Show this help message"
  Write-Host ""
}

function Run-Agent {
  param (
    [string]$agentName
  )
  
  if ([string]::IsNullOrEmpty($agentName)) {
    Write-Host "Error: Agent name required" -ForegroundColor Red
    Write-Host "Usage: .\scripts\speckit.ps1 run [agent_name]"
    Write-Host "Available agents: strategy_analyst, finance_modeler, operations_planner, compliance_reviewer, qa_probe_agent"
    exit 1
  }

  $agentPrompt = Join-Path $CURSOR_DIR "agents\${agentName}.prompt"
  if (-not (Test-Path $agentPrompt)) {
    Write-Host "Error: Agent prompt not found at $agentPrompt" -ForegroundColor Red
    exit 1
  }

  Write-Host "Running $agentName agent..." -ForegroundColor Green
  Write-Host "Using prompt: $agentPrompt"
  
  # Here we would call the actual Spec-Kit command
  # For now, we'll simulate by showing what would happen
  Write-Host "Agent would generate files based on its prompt and tasks.md"
  Write-Host "Output would be presented as diffs for approval"
}

function Implement-Plan {
  Write-Host "Implementing Bangkok Recycling Business Plan..." -ForegroundColor Green
  Write-Host "Following task sequence from $SPECS_DIR\tasks.md"
  
  # Check prerequisites
  $specFile = Join-Path $SPECS_DIR "spec.md"
  $planFile = Join-Path $SPECS_DIR "plan.md"
  $tasksFile = Join-Path $SPECS_DIR "tasks.md"
  
  if (-not ((Test-Path $specFile) -and (Test-Path $planFile) -and (Test-Path $tasksFile))) {
    Write-Host "Error: Missing required files. Ensure spec.md, plan.md, and tasks.md exist in $SPECS_DIR" -ForegroundColor Red
    exit 1
  }
  
  # Execute each agent in sequence based on tasks.md
  Write-Host "1. Running qa_probe_agent for initial assessment..." -ForegroundColor Cyan
  Run-Agent "qa_probe_agent"
  
  Write-Host "2. Running strategy_analyst..." -ForegroundColor Cyan
  Run-Agent "strategy_analyst"
  
  Write-Host "3. Running finance_modeler..." -ForegroundColor Cyan
  Run-Agent "finance_modeler"
  
  Write-Host "4. Running operations_planner..." -ForegroundColor Cyan
  Run-Agent "operations_planner"
  
  Write-Host "5. Running compliance_reviewer..." -ForegroundColor Cyan
  Run-Agent "compliance_reviewer"
  
  Write-Host "6. Running qa_probe_agent for final validation..." -ForegroundColor Cyan
  Run-Agent "qa_probe_agent"
  
  Write-Host "Implementation plan execution complete!" -ForegroundColor Green
}

function Check-Status {
  Write-Host "Checking implementation status..." -ForegroundColor Green
  
  # Check for expected output files
  $totalTasks = 18
  $completedTasks = 0
  
  # Strategy files
  if (Test-Path (Join-Path $REPO_ROOT "docs\BusinessPlan\strategy_summary.md")) { $completedTasks++ }
  if (Test-Path (Join-Path $REPO_ROOT "docs\BusinessPlan\market_segmentation.md")) { $completedTasks++ }
  
  # Finance files
  if (Test-Path (Join-Path $REPO_ROOT "finance\financial_model.csv")) { $completedTasks++ }
  if (Test-Path (Join-Path $REPO_ROOT "finance\pricing_catalog.csv")) { $completedTasks++ }
  if (Test-Path (Join-Path $REPO_ROOT "finance\assumptions.md")) { $completedTasks++ }
  
  # Operations files
  if (Test-Path (Join-Path $REPO_ROOT "ops\facility_plan.md")) { $completedTasks++ }
  if (Test-Path (Join-Path $REPO_ROOT "ops\hiring_plan.md")) { $completedTasks++ }
  if (Test-Path (Join-Path $REPO_ROOT "ops\ops_risk_matrix.md")) { $completedTasks++ }
  
  # Legal files
  if (Test-Path (Join-Path $REPO_ROOT "legal\legal_gap_list.md")) { $completedTasks++ }
  
  # QA files
  if (Test-Path (Join-Path $REPO_ROOT ".cursor\qa\inventory.json")) { $completedTasks++ }
  if (Test-Path (Join-Path $REPO_ROOT ".cursor\qa\coverage_matrix.md")) { $completedTasks++ }
  if (Test-Path (Join-Path $REPO_ROOT ".cursor\qa\gap_list.md")) { $completedTasks++ }
  if (Test-Path (Join-Path $REPO_ROOT ".cursor\qa\financial_probe_results.json")) { $completedTasks++ }
  
  $progress = [math]::Round(($completedTasks * 100 / $totalTasks))
  Write-Host "Progress: $progress% ($completedTasks/$totalTasks tasks completed)" -ForegroundColor Yellow
}

# Main command processing
switch ($args[0]) {
  "run" {
    Run-Agent $args[1]
    break
  }
  "implement" {
    Implement-Plan
    break
  }
  "status" {
    Check-Status
    break
  }
  "help" {
    Print-Usage
    break
  }
  default {
    Print-Usage
    if ($args.Count -gt 0) {
      exit 1
    }
  }
}
