#!/bin/bash
# sends a POST request to the passed URL- send two variables email & subject with their values
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
