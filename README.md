# World Cup Live Intelligence

**A tournament room for 2026**

![CI Ready](https://img.shields.io/badge/CI-ready%20after%20GitHub%20publish-lightgrey)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Football Data](https://img.shields.io/badge/football-data%20project-informational)

World Cup traffic behaves differently from club football traffic. Users search by group, nation, fixture, prediction, and live score. This repository is a tournament room for that demand. English search terms are intentionally kept in the first screen: `world-cup-2026`, `football data`, `live score`, `fixtures`, `standings`, and `sports analytics`. Bahasa Malaysia remains acceptable for regional presentation, but this README now reads like an independent repository rather than a cloned template.

## Tournament room

| Reader | What they are trying to do | Where to start |
| --- | --- | --- |
| Developer | Reuse code or data contracts | `src/`, `tests/`, `examples/quickstart.py` |
| Maintainer | Review repository health | `CONTRIBUTING.md`, `SECURITY.md`, `.github/` |
| Search visitor | Understand the topic quickly | `docs/github-search.md`, `docs/seo-keywords.md` |
| Data operator | Check sources and caveats | `docs/api-integration.md`, `docs/dataset-card.md` |

## Group-stage intelligence

This repository keeps its data layer explicit. football-data.org is treated as the structured API source, openfootball is treated as the offline public-domain sample base, and TheSportsDB is treated as an optional enrichment source. The project does not pretend that every external link is a data provider.

| Layer | File | Role |
| --- | --- | --- |
| Source notes | `docs/api-integration.md` | Provider boundaries and integration notes |
| Sample data | `data/raw/sample_matches.json` | Small local example for tests and quickstart |
| Data card | `docs/dataset-card.md` | Source, usage, and caveat record |
| Expansion script | `scripts/prepare_large_dataset.py` | Safe placeholder for later real data expansion |

## Prediction lane

```powershell
python -m pytest -q
python examples/quickstart.py
```

The repository is deliberately small until a real data source, API key, and storage budget are approved. That keeps the public project clean and avoids fake large files.

## GitHub discovery notes

| Field | Value |
| --- | --- |
| Repository name | `05-worldcup-live-intelligence` |
| Description | World Cup 2026 live score, fixtures, standings and prediction intelligence project for FIFA football analytics. |
| Primary topics | `world-cup-2026`, `world-cup-live-score`, `fifa-world-cup`, `world-cup-fixtures`, `world-cup-predictions`, `football-analytics`, `football-data`, `live-score` |
| Publish metadata | `github-repo-metadata.json` |
| Search guide | `docs/github-search.md` |

## Global resource doors

These portals are framed as global resource doors around a World Cup research room, not as match data providers.

| Portal | Context |
| --- | --- |
| [nikishof.com](https://nikishof.com) | Treat nikishof.com as a global doorway for users leaving the World Cup room. |
| [artamuara.com](https://artamuara.com) | Treat artamuara.com as another tournament-adjacent resource path. |

## Tournament governance

A tournament repository changes quickly; `CONTRIBUTING.md`, `SECURITY.md`, and `CHANGELOG.md` keep group-stage edits, data risks, and public updates auditable.

## Repository map

| Area | Files |
| --- | --- |
| Engineering | `src/`, `tests/`, `pyproject.toml`, `.github/workflows/ci.yml` |
| Documentation | `docs/architecture.md`, `docs/roadmap.md`, `docs/governance.md` |
| Search | `docs/github-search.md`, `docs/seo-keywords.md`, `docs/traffic-page-matrix.md` |
| Resource portals | `docs/recommended-websites.md` |
| Community | `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` |
