#!/bin/bash

# Check if an IP address was passed as an argument
if [ $# -eq 0 ]; then
	  echo "Usage: $0 {IP_ADDRESS}"
	    exit 1
fi

# Ping the IP address 5 times
ping -c 5 $1
