#!/bin/bash
source grange-env.sh
"${GOPATH}/bin/grange-server" --port=$GRANGE_SERVER_PORT "${GRANGE_SERVER_CONFIG}"
