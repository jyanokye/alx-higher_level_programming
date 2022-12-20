#!/bin/bash
# This script takes in a URL as its first argument and sends a POST request to that URL with two custom variables.It then displays the body of the response.
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
