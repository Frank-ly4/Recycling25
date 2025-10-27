# Spec-Kit Integration for Bangkok Recycling Business Plan

This document explains how to use Spec-Kit to activate and orchestrate the agents for the Bangkok Recycling Business Plan project.

## Setup Overview

The project has been configured with:

1. **Agent Prompts** - Located in `.cursor/agents/` directory:
   - strategy_analyst.prompt
   - finance_modeler.prompt
   - operations_planner.prompt
   - compliance_reviewer.prompt
   - qa_probe_agent.prompt

2. **Spec-Kit Configuration** - Located in:
   - `.cursor/specify.json` - Main configuration
   - `specs/001-bangkok-recycling/` - Specification files
   - `memory/constitution.md` - Agent constitution

3. **Template Files** - Located in `templates/` directory:
   - financials_template.csv
   - pricing_catalog_template.csv
   - ops_checklist.md

## Using Spec-Kit Commands

### PowerShell (Windows)

```powershell
# Run a specific agent
.\scripts\speckit.ps1 run qa_probe_agent
.\scripts\speckit.ps1 run strategy_analyst
.\scripts\speckit.ps1 run finance_modeler
.\scripts\speckit.ps1 run operations_planner
.\scripts\speckit.ps1 run compliance_reviewer

# Run the full implementation plan
.\scripts\speckit.ps1 implement

# Check implementation status
.\scripts\speckit.ps1 status

# Show help
.\scripts\speckit.ps1 help
```

### Bash (Linux/Mac)

```bash
# Run a specific agent
./scripts/speckit.sh run qa_probe_agent
./scripts/speckit.sh run strategy_analyst
./scripts/speckit.sh run finance_modeler
./scripts/speckit.sh run operations_planner
./scripts/speckit.sh run compliance_reviewer

# Run the full implementation plan
./scripts/speckit.sh implement

# Check implementation status
./scripts/speckit.sh status

# Show help
./scripts/speckit.sh help
```

## Implementation Workflow

1. **Initial Assessment**:
   ```
   .\scripts\speckit.ps1 run qa_probe_agent
   ```
   This will analyze the current state of the project and identify gaps.

2. **Strategy Development**:
   ```
   .\scripts\speckit.ps1 run strategy_analyst
   ```
   This will create strategy_summary.md and market_segmentation.md.

3. **Financial Modeling**:
   ```
   .\scripts\speckit.ps1 run finance_modeler
   ```
   This will create financial_model.csv, pricing_catalog.csv, and assumptions.md.

4. **Operations Planning**:
   ```
   .\scripts\speckit.ps1 run operations_planner
   ```
   This will create facility_plan.md, hiring_plan.md, and ops_risk_matrix.md.

5. **Compliance Review**:
   ```
   .\scripts\speckit.ps1 run compliance_reviewer
   ```
   This will create legal_gap_list.md.

6. **Final Validation**:
   ```
   .\scripts\speckit.ps1 run qa_probe_agent
   ```
   This will validate the complete business plan.

Alternatively, run the full implementation in one go:
```
.\scripts\speckit.ps1 implement
```

## Output and Approval

Each agent will:
1. Generate files according to its prompt and tasks
2. Present changes as diffs for your approval
3. Include audit metadata with each change
4. Wait for your approval before committing

## Monitoring Progress

Check the implementation status at any time:
```
.\scripts\speckit.ps1 status
```

This will show you the percentage of completed tasks and which files have been created.
