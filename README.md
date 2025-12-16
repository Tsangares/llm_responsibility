# The Role of Responsibility in AI's Strategic Risk-Taking

Replication code and data for DeAngelo, McCannon & Wyatt (2025).

**OSF Repository**: https://osf.io/a6f3u/

## Overview

This repository contains code to replicate experiments testing how responsibility affects LLM decision-making in a Stag-Hare coordination game. We compare "play-for-pair" (deciding for a team) vs "play-for-self" (deciding individually).

## Data Files

All data is in `dist/`. Files are named `{treatment}_df_{timestamp}.csv`.

| Timestamp | Description | N |
|-----------|-------------|---|
| 1734395183 | Main LLM vs LLM experiment | 15,000 |
| 1734473675 | LLM vs Random (50-50) agent | 7,500 |
| 1736822704 | LLM vs Mixed strategy agent | 750 |
| 1738885303 | Young persona | 4,500 |
| 1738885546 | Older persona | 4,500 |
| 1738885722 | Man persona | 4,500 |
| 1738885914 | Woman persona | 4,500 |
| 1738886203 | Competitive persona | 4,500 |
| 1738886397 | Introvert persona | 4,500 |
| 1738886580 | Extrovert persona | 4,500 |
| 1738973049 | Concealed game (Option A/B labels) | 4,500 |

Each experiment has a corresponding `notes_{timestamp}.yaml` with prompts and parameters.

## Setup

```bash
pip install -r requirements.txt
```

Create `.env` with your OpenAI API key:
```
OPENAI_API_KEY=your_key_here
```

## Usage

### Replicate Analysis
```bash
jupyter notebook replication.ipynb
```

### Run New Experiments
```bash
jupyter notebook game_play.ipynb
```

### Statistical Tests
```bash
python chi_square_tests.py
```

## Key Results

| Comparison | PP | PS | χ²(1) | p |
|------------|----|----|-------|---|
| Main result | 76.0% | 61.1% | 772.00 | <.001 |
| vs Human (C&J 2009) | 76.0% vs 42.9% | 61.1% vs 61.2% | 734.23 / 0.00 | <.001 / .991 |
| Concealed (Option A) | 3.1% | 1.1% | 44.23 | <.001 |

LLMs take significantly more risk when responsible for others.

## Files

- `game_play.ipynb` - Main experiment runner
- `game_play_options.ipynb` - Concealed game variant
- `persona_analysis.ipynb` - Persona experiment analysis
- `replication.ipynb` - Results replication
- `chi_square_tests.py` - Statistical tests for paper
- `statistical_results.md` - Summary of all test results

## Citation

```bibtex
@article{deangelo2025responsibility,
  title={The Role of Responsibility in AI's Strategic Risk-Taking},
  author={DeAngelo, Gregory and McCannon, Bryan and Wyatt, Aaron},
  journal={Journal of Economic Psychology},
  year={2025}
}
```

## Contact

Open an issue or contact the authors with questions.
