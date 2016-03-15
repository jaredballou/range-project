#!/bin/bash
if [ ! -e /usr/local/bin/erg ]; then
	brew tap square/self
	brew install erg
fi
