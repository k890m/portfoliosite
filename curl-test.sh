#!/bin/bash

ENDPOINT_URL = http://localhost:5000/api/timeline_post

# Random inputs
random_name="User_$RANDOM"
random_email="user_$RANDOM@example.com"
random_content="Message Number: $RANDOM"

# POST request
curl -X POST "$ENDPOINT_URL" -d "name=$random_name&email=$random_email&content=$random_content"

# GET request
response=$(curl -s "$ENDPOINT_URL")

# Check if to see if added
if echo "$response" | grep -q "$random_content"; then
    echo "Timeline post was successfully added!"
else
    echo "Failed to find the timeline post."
fi
