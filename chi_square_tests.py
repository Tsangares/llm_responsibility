"""
Chi-square tests for JoEP submission
"The Role of Responsibility in AI's Strategic Risk-Taking"
"""
import pandas as pd
import numpy as np
from scipy import stats

def chi2_test(a_success, a_total, b_success, b_total, label_a="A", label_b="B"):
    """Run chi-square test and return formatted results"""
    contingency = np.array([[a_success, a_total - a_success],
                           [b_success, b_total - b_success]])
    chi2, p, dof, expected = stats.chi2_contingency(contingency)

    pct_a = 100 * a_success / a_total
    pct_b = 100 * b_success / b_total

    p_str = "p < .001" if p < 0.001 else f"p = {p:.3f}"
    sig = "***" if p < 0.001 else ("**" if p < 0.01 else ("*" if p < 0.05 else "n.s."))

    print(f"  {label_a}: {a_success}/{a_total} ({pct_a:.2f}%)")
    print(f"  {label_b}: {b_success}/{b_total} ({pct_b:.2f}%)")
    print(f"  χ²(1) = {chi2:.2f}, {p_str} {sig}")
    print(f"  LaTeX: $\\chi^2(1) = {chi2:.2f}$, ${p_str}$")
    print()
    return chi2, p, pct_a, pct_b

# =============================================================
# 1. MAIN RESULT: LLM Play-for-Pair vs Play-for-Self
# =============================================================
print("=" * 70)
print("1. MAIN RESULT: LLM Play-for-Pair vs Play-for-Self")
print("=" * 70)
pp_df = pd.read_csv('./dist/pp_df_1734395183.csv')
ps_df = pd.read_csv('./dist/ps_df_1734395183.csv')

pp_stag = pp_df['stag'].sum()
pp_total = len(pp_df)
ps_stag = ps_df['stag'].sum()
ps_total = len(ps_df)

chi2_test(pp_stag, pp_total, ps_stag, ps_total, "Play-for-Pair (Stag)", "Play-for-Self (Stag)")

# =============================================================
# 2-3. VS HUMAN (Charness & Jackson 2009)
# =============================================================
human_n = 1440  # 96 subjects x 15 rounds
human_pp_stag = int(0.429 * human_n)  # 617
human_ps_stag = int(0.612 * human_n)  # 881

print("=" * 70)
print("2. LLM vs Human - Play-for-Pair")
print("=" * 70)
chi2_test(pp_stag, pp_total, human_pp_stag, human_n, "LLM (PP)", "Human (PP)")

print("=" * 70)
print("3. LLM vs Human - Play-for-Self")
print("=" * 70)
chi2_test(ps_stag, ps_total, human_ps_stag, human_n, "LLM (PS)", "Human (PS)")

# =============================================================
# 4. CONCEALED GAME (Option A/B)
# =============================================================
print("=" * 70)
print("4. CONCEALED GAME: Play-for-Pair vs Play-for-Self (Option A/B)")
print("=" * 70)
concealed_pp = pd.read_csv('./dist/pp_df_1738973049.csv')
concealed_ps = pd.read_csv('./dist/ps_df_1738973049.csv')

concealed_pp_a = concealed_pp['option_a'].sum()
concealed_pp_total = len(concealed_pp)
concealed_ps_a = concealed_ps['option_a'].sum()
concealed_ps_total = len(concealed_ps)

chi2_test(concealed_pp_a, concealed_pp_total, concealed_ps_a, concealed_ps_total,
          "Play-for-Pair (Option A)", "Play-for-Self (Option A)")

# =============================================================
# 5. RANDOM AGENT (50-50): PP vs PS
# =============================================================
print("=" * 70)
print("5. RANDOM AGENT (50-50): PP vs PS")
print("=" * 70)
random_pp = pd.read_csv('./dist/pp_df_1734473675.csv')
random_ps = pd.read_csv('./dist/ps_df_1734473675.csv')

# Filter to LLM only (Team1/Player1)
random_pp_llm = random_pp[random_pp['player'].isin(['Team1', 'Player1'])]
random_ps_llm = random_ps[random_ps['player'].isin(['Player1'])]

chi2_test(random_pp_llm['stag'].sum(), len(random_pp_llm),
          random_ps_llm['stag'].sum(), len(random_ps_llm),
          "Play-for-Pair (Stag)", "Play-for-Self (Stag)")

# =============================================================
# 6. MIXED STRATEGY AGENT: PP vs PS
# =============================================================
print("=" * 70)
print("6. MIXED STRATEGY AGENT: PP vs PS")
print("=" * 70)
mixed_pp = pd.read_csv('./dist/pp_df_1736822704.csv')
mixed_ps = pd.read_csv('./dist/ps_df_1736822704.csv')

mixed_pp_llm = mixed_pp[mixed_pp['player'].isin(['Team1', 'Player1'])]
mixed_ps_llm = mixed_ps[mixed_ps['player'].isin(['Player1'])]

chi2_test(mixed_pp_llm['stag'].sum(), len(mixed_pp_llm),
          mixed_ps_llm['stag'].sum(), len(mixed_ps_llm),
          "Play-for-Pair (Stag)", "Play-for-Self (Stag)")

# =============================================================
# 7-12. PERSONA COMPARISONS
# =============================================================
personas = {
    "No Persona": 1734395183,
    "Young": 1738885303,
    "Older": 1738885546,
    "Man": 1738885722,
    "Woman": 1738885914,
    "Competitive": 1738886203,
    "Introvert": 1738886397,
    "Extrovert": 1738886580
}

# Load all persona data
persona_data = {}
for name, file_id in personas.items():
    pp = pd.read_csv(f'./dist/pp_df_{file_id}.csv')
    ps = pd.read_csv(f'./dist/ps_df_{file_id}.csv')
    persona_data[name] = {
        'pp_stag': pp['stag'].sum(),
        'pp_total': len(pp),
        'ps_stag': ps['stag'].sum(),
        'ps_total': len(ps)
    }

# 7-8. PP vs PS within each persona
print("=" * 70)
print("7-14. PP vs PS WITHIN EACH PERSONA")
print("=" * 70)
for name, data in persona_data.items():
    print(f"\n{name}:")
    chi2_test(data['pp_stag'], data['pp_total'],
              data['ps_stag'], data['ps_total'],
              "Play-for-Pair", "Play-for-Self")

# Persona pair comparisons (within PP treatment)
print("=" * 70)
print("15-18. PERSONA PAIR COMPARISONS (Play-for-Pair treatment)")
print("=" * 70)
persona_pairs = [
    ('Young', 'Older'),
    ('Man', 'Woman'),
    ('Introvert', 'Extrovert'),
    ('Competitive', 'No Persona')
]

for p1, p2 in persona_pairs:
    d1, d2 = persona_data[p1], persona_data[p2]
    print(f"\n{p1} vs {p2} (PP):")
    chi2_test(d1['pp_stag'], d1['pp_total'],
              d2['pp_stag'], d2['pp_total'],
              p1, p2)

# Persona pair comparisons (within PS treatment)
print("=" * 70)
print("19-22. PERSONA PAIR COMPARISONS (Play-for-Self treatment)")
print("=" * 70)
for p1, p2 in persona_pairs:
    d1, d2 = persona_data[p1], persona_data[p2]
    print(f"\n{p1} vs {p2} (PS):")
    chi2_test(d1['ps_stag'], d1['ps_total'],
              d2['ps_stag'], d2['ps_total'],
              p1, p2)

# =============================================================
# SUMMARY TABLE
# =============================================================
print("\n" + "=" * 70)
print("SUMMARY TABLE FOR PAPER")
print("=" * 70)
print("""
| Test | Comparison | χ²(1) | p-value | Significant |
|------|------------|-------|---------|-------------|
""")
