#!/usr/bin/env bash
# Script to restart Odoo and upgrade custom modules cleanly
set -e

DB_NAME="${1:-postgres}"
MODULE_NAME="${2:-project_vault}"

echo "==========================================="
echo " 1. Restarting Odoo container..."
echo "==========================================="
docker compose restart odoo

echo "==========================================="
echo " 2. Upgrading module '$MODULE_NAME' on '$DB_NAME'..."
echo "==========================================="
docker compose exec odoo odoo -u "$MODULE_NAME" -d "$DB_NAME" --stop-after-init

echo "==========================================="
echo " Done! Refresh your browser on :8089"
echo "==========================================="

