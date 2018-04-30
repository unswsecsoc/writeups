#!/bin/bash

CONF_DIR=/etc/cjdns

if [ ! -f "$CONF_DIR/cjdroute.conf" ]; then
	echo "Generating $CONF_DIR/cjdroute.conf"
	cjdroute --genconf > "$CONF_DIR/cjdroute.conf"
fi

cjdroute --nobg < "$CONF_DIR/cjdroute.conf" &
trap 'kill %1' EXIT

xinetd -d -dontfork
