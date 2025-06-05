#!/bin/bash

# Search for index.html in the current directory and subdirectories
file_path=$(find . -type f -name "index.html" | head -n 1)

if [[ -z "$file_path" ]]; then
  echo "index.html not found."
  exit 1
fi

# Encrypt the file using openssl with -pbkdf2 for better security
openssl enc -aes-256-cbc -salt -pbkdf2 -in "$file_path" -out /tmp/index.html.enc -k "HHH"

# Send the encrypted file as an HTTP POST request using curl
curl -X POST --data-binary @/tmp/index.html.enc http://localhost:5550/

# Clean up
rm /tmp/index.html.enc

# ...existing code...

# Ping google.com and save the output to google.com.ping
ping -c 4 google.com > google.com.ping

# ...existing code...