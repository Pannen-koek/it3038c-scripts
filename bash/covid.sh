#!/bin/bash
# Script downloads covid data and displays it.

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
DEATH=$(echo $DATA | jq '.[0].death')

echo "As of $TODAY, there are $POSITIVE postive cases, $NEGATIVE negative cases, and $PENDING pending results from testing."

echo "The current death toll looms at $DEATH deaths." 
