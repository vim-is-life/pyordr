#!/usr/bin/env sh
set -e

# if [ $# -ne 2 ]; then
#     echo "usage deploy.sh <SERVICE_USER>"
# fi


# # SERVICE_DIR="$(pkg-config systemd --variable=systemduserunitdir)"
# SERVICE_DIR="$(pkg-config systemd --variable=systemdsystemunitdir)"
SERVICE_DIR="/etc/systemd/system"
$SERVICE_USER=$USER
PROJECT_DIR="$(pwd)"
APP_PORT=5100
NUM_WORKERS=$(($(nproc) * 2))
TMP=$(mktemp)

echo "============================================="
echo "             Making unit file                "
echo "============================================="

tee "$TMP" <<EOF
[Unit]
Description=gunicorn instance to serve the 'pyordr' app.
After=network.target

[Service]
User=$SERVICE_USER
# Group=www-data
WorkingDirectory=$PROJECT_DIR
Environment="PATH=$PROJECT_DIR/.venv/bin"
ExecStart=$PROJECT_DIR/.venv/bin/gunicorn -b 0.0.0.0:$APP_PORT -w $NUM_WORKERS wsgi:app

[Install]
WantedBy=multi-user.target
EOF

echo "============================================="
echo "               Moving temp file              "
echo "============================================="

set -x
sudo mv "$TMP" "$SERVICE_DIR/pyordr.service"
unset xtrace
