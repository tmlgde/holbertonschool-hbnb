#!/bin/bash

# Remplace ces valeurs par les vrais UUIDs créés dans la sandbox principale
USER_ID="xxxx-xxxx-xxxx-xxxx"
PLACE_ID="yyyy-yyyy-yyyy-yyyy"

echo "➡️  Creating a new review..."
REVIEW=$(curl -s -X POST http://localhost:5000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Amazing location!",
    "rating": 5,
    "user_id": "'$USER_ID'",
    "place_id": "'$PLACE_ID'"
  }')

REVIEW_ID=$(echo $REVIEW | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])")

echo "✅ Created Review ID: $REVIEW_ID"

echo -e "\n➡️  Getting all reviews..."
curl -s http://localhost:5000/api/v1/reviews/ | jq

echo -e "\n➡️  Getting the review by ID..."
curl -s http://localhost:5000/api/v1/reviews/$REVIEW_ID | jq

echo -e "\n➡️  Updating the review..."
curl -s -X PUT http://localhost:5000/api/v1/reviews/$REVIEW_ID \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Nice place, very clean",
    "rating": 4
  }' | jq

echo -e "\n➡️  Getting all reviews for place $PLACE_ID..."
curl -s http://localhost:5000/api/v1/places/$PLACE_ID/reviews | jq

echo -e "\n➡️  Deleting the review..."
curl -s -X DELETE http://localhost:5000/api/v1/reviews/$REVIEW_ID | jq

echo -e "\n✅ All done!"

