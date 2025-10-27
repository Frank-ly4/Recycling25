#!/bin/bash
# Spec-Kit command wrapper for Bangkok Recycling Business Plan

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPECS_DIR="$REPO_ROOT/specs/001-bangkok-recycling"
CURSOR_DIR="$REPO_ROOT/.cursor"

function print_usage() {
  echo "Spec-Kit Command Wrapper"
  echo "------------------------"
  echo "Usage: ./scripts/speckit.sh [command]"
  echo ""
  echo "Available commands:"
  echo "  run [agent_name]   - Run a specific agent (e.g., qa_probe_agent)"
  echo "  implement          - Execute the full implementation plan"
  echo "  status             - Check implementation status"
  echo "  help               - Show this help message"
  echo ""
}

function run_agent() {
  local agent_name=$1
  if [ -z "$agent_name" ]; then
    echo "Error: Agent name required"
    echo "Usage: ./scripts/speckit.sh run [agent_name]"
    echo "Available agents: strategy_analyst, finance_modeler, operations_planner, compliance_reviewer, qa_probe_agent"
    exit 1
  fi

  local agent_prompt="$CURSOR_DIR/agents/${agent_name}.prompt"
  if [ ! -f "$agent_prompt" ]; then
    echo "Error: Agent prompt not found at $agent_prompt"
    exit 1
  fi

  echo "Running $agent_name agent..."
  echo "Using prompt: $agent_prompt"
  
  # Here we would call the actual Spec-Kit command
  # For now, we'll simulate by showing what would happen
  echo "Agent would generate files based on its prompt and tasks.md"
  echo "Output would be presented as diffs for approval"
}

function implement_plan() {
  echo "Implementing Bangkok Recycling Business Plan..."
  echo "Following task sequence from $SPECS_DIR/tasks.md"
  
  # Check prerequisites
  if [ ! -f "$SPECS_DIR/spec.md" ] || [ ! -f "$SPECS_DIR/plan.md" ] || [ ! -f "$SPECS_DIR/tasks.md" ]; then
    echo "Error: Missing required files. Ensure spec.md, plan.md, and tasks.md exist in $SPECS_DIR"
    exit 1
  fi
  
  # Execute each agent in sequence based on tasks.md
  echo "1. Running qa_probe_agent for initial assessment..."
  run_agent "qa_probe_agent"
  
  echo "2. Running strategy_analyst..."
  run_agent "strategy_analyst"
  
  echo "3. Running finance_modeler..."
  run_agent "finance_modeler"
  
  echo "4. Running operations_planner..."
  run_agent "operations_planner"
  
  echo "5. Running compliance_reviewer..."
  run_agent "compliance_reviewer"
  
  echo "6. Running qa_probe_agent for final validation..."
  run_agent "qa_probe_agent"
  
  echo "Implementation plan execution complete!"
}

function check_status() {
  echo "Checking implementation status..."
  
  # Check for expected output files
  local total_tasks=18
  local completed_tasks=0
  
  # Strategy files
  if [ -f "$REPO_ROOT/docs/BusinessPlan/strategy_summary.md" ]; then ((completed_tasks++)); fi
  if [ -f "$REPO_ROOT/docs/BusinessPlan/market_segmentation.md" ]; then ((completed_tasks++)); fi
  
  # Finance files
  if [ -f "$REPO_ROOT/finance/financial_model.csv" ]; then ((completed_tasks++)); fi
  if [ -f "$REPO_ROOT/finance/pricing_catalog.csv" ]; then ((completed_tasks++)); fi
  if [ -f "$REPO_ROOT/finance/assumptions.md" ]; then ((completed_tasks++)); fi
  
  # Operations files
  if [ -f "$REPO_ROOT/ops/facility_plan.md" ]; then ((completed_tasks++)); fi
  if [ -f "$REPO_ROOT/ops/hiring_plan.md" ]; then ((completed_tasks++)); fi
  if [ -f "$REPO_ROOT/ops/ops_risk_matrix.md" ]; then ((completed_tasks++)); fi
  
  # Legal files
  if [ -f "$REPO_ROOT/legal/legal_gap_list.md" ]; then ((completed_tasks++)); fi
  
  # QA files
  if [ -f "$REPO_ROOT/.cursor/qa/inventory.json" ]; then ((completed_tasks++)); fi
  if [ -f "$REPO_ROOT/.cursor/qa/coverage_matrix.md" ]; then ((completed_tasks++)); fi
  if [ -f "$REPO_ROOT/.cursor/qa/gap_list.md" ]; then ((completed_tasks++)); fi
  if [ -f "$REPO_ROOT/.cursor/qa/financial_probe_results.json" ]; then ((completed_tasks++)); fi
  
  local progress=$((completed_tasks * 100 / total_tasks))
  echo "Progress: $progress% ($completed_tasks/$total_tasks tasks completed)"
}

# Main command processing
case "$1" in
  run)
    run_agent "$2"
    ;;
  implement)
    implement_plan
    ;;
  status)
    check_status
    ;;
  help|--help|-h)
    print_usage
    ;;
  *)
    print_usage
    exit 1
    ;;
esac
