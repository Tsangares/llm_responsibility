# Statistical Test Results for JoEP Submission

## Summary Table

| Test | Comparison | χ²(1) | p-value | Sig |
|------|------------|-------|---------|-----|
| **Main Result** | LLM PP (76.03%) vs PS (61.13%) | 772.00 | < .001 | *** |
| **LLM vs Human (PP)** | LLM (76.03%) vs Human (42.85%) | 734.23 | < .001 | *** |
| **LLM vs Human (PS)** | LLM (61.13%) vs Human (61.18%) | 0.00 | .991 | n.s. |
| **Concealed Game** | PP Option A (3.09%) vs PS (1.07%) | 44.23 | < .001 | *** |
| **Random Agent** | PP (38.27%) vs PS (36.40%) | 2.71 | .100 | n.s. |
| **Mixed Strategy** | PP (87.73%) vs PS (74.13%) | 21.60 | < .001 | *** |

## Persona Results (PP vs PS within persona)

| Persona | PP Stag % | PS Stag % | χ²(1) | p-value | Sig |
|---------|-----------|-----------|-------|---------|-----|
| No Persona | 76.03% | 61.13% | 772.00 | < .001 | *** |
| Young | 71.09% | 72.82% | 3.26 | .071 | n.s. |
| Older | 42.87% | 73.71% | 879.17 | < .001 | *** (reversed) |
| Man | 55.56% | 78.67% | 543.43 | < .001 | *** (reversed) |
| Woman | 17.51% | 63.33% | 1959.79 | < .001 | *** (reversed) |
| Competitive | 89.31% | 17.87% | 4614.80 | < .001 | *** |
| Introvert | 4.18% | 12.91% | 218.49 | < .001 | *** (reversed) |
| Extrovert | 88.11% | 100.00% | 566.69 | < .001 | *** |

Note: "reversed" means PS > PP (opposite of main result)

## Persona Pair Comparisons (within PP treatment)

| Comparison | χ²(1) | p-value | Sig |
|------------|-------|---------|-----|
| Young (71.09%) vs Older (42.87%) | 729.93 | < .001 | *** |
| Man (55.56%) vs Woman (17.51%) | 1402.89 | < .001 | *** |
| Introvert (4.18%) vs Extrovert (88.11%) | 6374.87 | < .001 | *** |
| Competitive (89.31%) vs No Persona (76.03%) | 368.61 | < .001 | *** |

## Persona Pair Comparisons (within PS treatment)

| Comparison | χ²(1) | p-value | Sig |
|------------|-------|---------|-----|
| Young (72.82%) vs Older (73.71%) | 0.86 | .353 | n.s. |
| Man (78.67%) vs Woman (63.33%) | 256.18 | < .001 | *** |
| Introvert (12.91%) vs Extrovert (100%) | 6938.20 | < .001 | *** |
| Competitive (17.87%) vs No Persona (61.13%) | 2590.83 | < .001 | *** |

## LaTeX Snippets for Paper

### Section 4 - Main Results
```latex
LLMs chose Stag significantly more often under play-for-pair (76.03\%) than
play-for-self (61.13\%), $\chi^2(1) = 772.00$, $p < .001$.

Compared to humans, LLMs differed significantly in play-for-pair
($\chi^2(1) = 734.23$, $p < .001$) but not in play-for-self
($\chi^2(1) = 0.00$, $p = .991$).
```

### Section 5.1 - Concealed Game
```latex
When game labels were concealed (Option A/B), the effect persisted:
play-for-pair (3.09\%) vs play-for-self (1.07\%), $\chi^2(1) = 44.23$, $p < .001$.
```

### Section 5.3 - Random and Mixed Strategy Agents
```latex
Against a random (50-50) agent, the difference was not significant
($\chi^2(1) = 2.71$, $p = .100$). However, against a mixed strategy agent
the effect remained significant ($\chi^2(1) = 21.60$, $p < .001$).
```

## Data Files Audit

### Essential Files (keep for OSF/GitHub)

| Timestamp | Description | Rows | Used In |
|-----------|-------------|------|---------|
| 1734395183 | Main LLM vs LLM | 15,000 | Section 4 |
| 1734473675 | Random agent (50-50) | 7,500 | Section 5.3 |
| 1736822704 | Mixed strategy agent | 750 | Section 5.3 |
| 1738885303 | Young persona | 4,500 | Section 5.2 |
| 1738885546 | Older persona | 4,500 | Section 5.2 |
| 1738885722 | Man persona | 4,500 | Section 5.2 |
| 1738885914 | Woman persona | 4,500 | Section 5.2 |
| 1738886203 | Competitive persona | 4,500 | Section 5.2 |
| 1738886397 | Introvert persona | 4,500 | Section 5.2 |
| 1738886580 | Extrovert persona | 4,500 | Section 5.2 |
| 1738973049 | Concealed game (Option A/B) | 4,500 | Section 5.1 |

### Non-Essential Files (pilot/test runs - can remove)

| Timestamp | Description | Rows | Notes |
|-----------|-------------|------|-------|
| 1734475400 | Random agent duplicate | 7,500 | Duplicate of 1734473675 |
| 1738712498 | Test run (50 rounds, 3/trial) | 300 | Pilot study |
| 1738880266 | Different system prompt | 250 | Pilot study |
| 1738880392 | 15 rounds/trial variant | 750 | Pilot study |
| 1738882488 | No persona baseline | 750 | Pilot study |
| 1738885041 | Young persona (different prompt) | 1,500 | Superseded by 1738885303 |
| 1745975387 | Test run (20 rounds) | 600 | Test run |

### Summary Files (keep)

| File | Description |
|------|-------------|
| personalities_pp_mean.csv | Aggregated persona means (PP) |
| personalities_ps_mean.csv | Aggregated persona means (PS) |
| notes_*.yaml | Experiment metadata (keep matching essential files)
