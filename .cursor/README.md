# Cursor Agent Orchestration — Recycling25 Business Plan

**Owner & Approver:** Frank-ly4  
**Agent Prompts Location:** `.cursor/agents/*.prompt`  
**Governance:** All agents output unapplied diffs + audit entries; owner must approve commits to canonical artifacts (prefix `BP_`).

## Agent Roles
- `strategy_analyst` → docs/BusinessPlan (market analysis, value prop, GTM)
- `finance_modeler` → finance (financial models, pricing catalogs, assumptions)
- `operations_planner` → ops (facility plans, hiring, risk matrix)
- `compliance_reviewer` → legal (gap analysis, regulatory checks)
- `qa_probe_agent` → .cursor/qa (coverage, consistency, financial sanity probes)

## Running QA Probes
Invoke `qa_probe_agent` to execute runtime tests per `.cursor/specify.json` financialProbeRules. Review `.cursor/qa/financial_probe_results.json` for pass/fail status.

## Naming Pattern
Published artifacts use prefix `BP_` with pattern: `BP_<type>_<YYYYMMDD>_v<semver>`.

