# Feature-ledger workspace

Repo-local feature/action ledger files live in this directory. Keep entries
compact, append-only, and provenance-marked. Repo-local ledgers remain the
authoritative source; dory-memory backups are advisory mirrors only.

- ledger-index.yaml tracks the active ledger file and rotation limits
- tally.yaml keeps compact per-feature counts
- giles-ledger-0001.md stores the compact feature-action entries
