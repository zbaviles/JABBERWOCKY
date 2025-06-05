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

# Ping google.com and save the output to google.com.ping
ping -c 4 google.com > google.com.ping

wc -l index.html > lines.txt

# Start HTTPS server in background using your server.pem
python3 -m http.server 8443 --bind 127.0.0.1 --directory . --certfile server.pem &
server_pid=$!
sleep 2  # Give the server time to start

# Use wget to securely fetch the directory listing (information summary)
wget --no-check-certificate https://127.0.0.1:8443 -O directory.html

# Kill the server after fetching
kill $server_pid

# Show a summary of the downloaded file
echo "Downloaded directory listing summary:"
head -20 directory.html

# Display the contents of example.cpp
echo "Displaying example.cpp:"
cat example.cpp
./a.out
whoami