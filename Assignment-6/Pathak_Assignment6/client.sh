#!/bin/bash

VAR1="client"
read -p "Command: " VAR2

if [[ "$VAR1" == "$VAR2" ]]; then
    echo "Image Classification Server"
    echo "Sagar"
    echo "Apr, 28 2022"
else
    echo "Getting Response"
    python3 web-client.py
fi
