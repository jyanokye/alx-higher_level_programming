#!/bin/bash
# takes in a URL and displays all the HTTP methods the server will accept
curl -sI "$1" | grep "Allow: " | sed 's/Allow: //'
