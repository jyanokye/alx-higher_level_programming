#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument and dsplays the body of the response
curl -sX DELETE "$1"
