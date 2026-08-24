#!/data/data/com.termux/files/usr/bin/bash
# AJ V2 updater - Termux
# Re-downloads ajv2.py (nub.py) from the repo, overwriting the installed copy.
# Run this any time to pull the latest version without reinstalling everything.
set -e

REPO_RAW="https://raw.githubusercontent.com/aaalmaz0/mm2/refs/heads/main"
INSTALL_DIR="$HOME/ajv2"

if [ ! -d "$INSTALL_DIR" ]; then
    echo "AJ V2 is not installed yet. Run the installer first:"
    echo "  curl -fsSL $REPO_RAW/install.sh | bash"
    exit 1
fi

echo "==> Updating ajv2.py..."
curl -fsSL "$REPO_RAW/ajv2.py" -o "$INSTALL_DIR/ajv2.py.new"
mv "$INSTALL_DIR/ajv2.py.new" "$INSTALL_DIR/ajv2.py"

echo "Done. ajv2.py is up to date."
echo "Run it with:  ajv2"
