#!/bin/bash

set -e
set -u
set -o pipefail

. /opt/pysetup/.venv/bin/activate
exec "$@"
