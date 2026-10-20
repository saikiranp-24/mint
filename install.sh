#!/bin/sh
set -eu

REPO="saikiranp-24/mint"
INSTALL_DIR="${HOME}/.local/bin"

if [ "$(uname -s)" != "Linux" ]; then
    echo "Error: This script is for Linux only."
    echo "macOS: brew install saikiranp-24/tap/mint"
    echo "Windows: scoop install mint"
    exit 1
fi

if command -v curl >/dev/null 2>&1; then
    FETCH_CMD="curl -sL"
    HEADER_CMD="curl -sI"
elif command -v wget >/dev/null 2>&1; then
    FETCH_CMD="wget -qO-"
    HEADER_CMD="wget -qS --spider"
else
    echo "Error: curl or wget is required."
    exit 1
fi

ARCH=$(uname -m)
case "$ARCH" in
    x86_64|amd64) TARGET_ARCH="x86_64" ;;
    aarch64|arm64) TARGET_ARCH="aarch64" ;;
    *) echo "Unsupported architecture: $ARCH"; exit 1 ;;
esac

# 2. Bottleneck fixed: Safe musl detection without crashing `set -e`
LIBC="glibc"
if [ -f /lib/ld-musl-${TARGET_ARCH}.so.1 ] || command -v apk >/dev/null 2>&1; then
    LIBC="musl"
else
    # Fallback to checking ldd safely without using --version
    if ldd /bin/sh 2>&1 | grep -q 'musl'; then
        LIBC="musl"
    fi
fi

TARGET="${TARGET_ARCH}-unknown-linux-${LIBC}"

echo "Fetching latest version..."
# 3. Bottleneck fixed: Robust version fetching
VERSION=$($HEADER_CMD "https://github.com/$REPO/releases/latest" 2>&1 | grep -i "^[[:space:]]*location:" | grep -o "v[0-9]\+\.[0-9]\+\.[0-9]\+" | head -n 1)

if [ -z "$VERSION" ]; then
    echo "Error: Failed to fetch latest version."
    exit 1
fi

FILENAME="mint-${VERSION}-${TARGET}.tar.gz"
DOWNLOAD_URL="https://github.com/${REPO}/releases/download/${VERSION}/${FILENAME}"

echo "Downloading mint ${VERSION} for${TARGET}..."
mkdir -p "$INSTALL_DIR"

# 4. Bottleneck fixed: Isolated temp directory
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

$FETCH_CMD "$DOWNLOAD_URL" | tar -xz -C "$TMP_DIR"
mv "$TMP_DIR/mint" "$INSTALL_DIR/mint"
chmod +x "$INSTALL_DIR/mint"

echo "Successfully installed mint to $INSTALL_DIR/mint"

case ":${PATH}:" in
    *":$INSTALL_DIR:"*) ;;
    *) echo "Note: Add $INSTALL_DIR to your PATH to use mint globally." ;;
esac
