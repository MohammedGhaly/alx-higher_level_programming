#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL
# displays the size of the body of the response
curl -s -w %{size_download}"\n" "$1"
