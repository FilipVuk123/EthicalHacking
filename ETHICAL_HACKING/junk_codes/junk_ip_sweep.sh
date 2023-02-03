#!/bin/bash

if [ "$1" == "" ]
then
  echo "You forgot ip address"
  echo "Syntax: sh ip_sweep.sh 192.168.0"

else
  for ip in {1..254}
  do
    ping -c 1 "$1.$ip" > /dev/null 2>&1 && printf '%s\n' "$1.$ip" &
  done
fi