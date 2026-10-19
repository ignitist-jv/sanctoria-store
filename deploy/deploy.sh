#!/usr/bin/env bash
# Deploy site/ to LiquidWeb over explicit FTPS using credentials in .env.
# Usage: deploy/deploy.sh [--dry-run]
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec python3 "$REPO_ROOT/deploy/deploy.py" "$@"
