#!/bin/bash
export GOPATH="$HOME/go"
export SRC="github.com/jaredballou"

#if [ ! -e "${GOPATH}" ]; then mkdir -p "${GOPATH}"; fi

export GRANGE_SERVER_PORT=8080
export GRANGE_SERVER_CONFIG="${GOPATH}/src/${SRC}/grange-server/grange.gcfg"
