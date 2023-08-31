#!/bin/bash
# takes a URL, sends a request, displays the size of the body of the response
curl -s -w %{size_download}"\n" "$1"
