#!/data/data/com.termux/files/usr/bin/bash
# AJ V2 installer - Termux
set -e

REPO_RAW="https://raw.githubusercontent.com/aaalmaz0/mm2/refs/heads/main"
INSTALL_DIR="$HOME/ajv2"
BIN_DIR="$PREFIX/bin"

echo "==> Installing system packages..."
pkg install -y python git >/dev/null

echo "==> Installing Python packages..."
pip install requests pyfiglet colorama prettytable bypasstools discord.py

echo "==> Downloading ajv2.py..."
mkdir -p "$INSTALL_DIR"
curl -fsSL "$REPO_RAW/ajv2.py" -o "$INSTALL_DIR/ajv2.py"

echo "==> Installing the 'ajv2' command..."
cat > "$BIN_DIR/ajv2" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
cd "$INSTALL_DIR" && exec python ajv2.py "\$@"
EOF
chmod +x "$BIN_DIR/ajv2"

echo
echo "Done. Run it with:  ajv2"
echo "Installed at: $INSTALL_DIR/ajv2.py"
