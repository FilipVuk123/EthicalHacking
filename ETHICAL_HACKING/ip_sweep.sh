#!/bin/bash

if [ "$1" == "" ]
then
  echo "You forgot ip address"
  echo "Syntax: sh ip_sweep.sh 192.168.0"
  exit 1
fi

# Use `parallel` command to ping multiple IP addresses in parallel
parallel -j 255 ping -c 1 "$1.{}" > /dev/null 2>&1 && printf '%s\n' "$1.{}" ::: {1..254}