#!/bin/bash

if [ "$1" == "" ]; then
  echo "You forgot the IP address."
  echo "Syntax: sh ip_sweep.sh 192.168.0"
  exit 1
fi

for ip in {1..254}; do
  ping -c 1 "$1.$ip" &>/dev/null && echo "$1.$ip" &
done
wait
