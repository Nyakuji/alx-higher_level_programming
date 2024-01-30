#!/bin/bash
#script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s "$1" -X POST -d "email=opiyophilipo@gmail.com&subject=I will always be here for PLD"
