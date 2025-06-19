#!/bin/bash

echo ">>> Test POST (create place)"

# Remplacer cette valeur par un vrai ID d'utilisateur existant dans ton système
OWNER_ID="3fa85f64-5717-4562-b3fc-2c963f66afa6"

# Créer un lieu
response=$(curl -s -X POST http://localhost:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"Cozy Apartment\",
    \"description\": \"A nice place to stay\",
    \"price\": 100.0,
    \"latitude\": 37.7749,
    \"longitude\": -122.4194,
    \"owner_id\": \"$OWNER_ID\",
    \"amenities\": []
}")

echo "$response"

# Extraire l'ID du lieu
place_id=$(echo "$response" | jq -r '.id')

if [ "$place_id" == "null" ] || [ -z "$place_id" ]; then
  echo "❌ Échec de la création du lieu, ID non trouvé."
  exit 1
fi

echo "✅ Lieu créé avec l'ID : $place_id"


echo ""
echo ">>> Test GET (get all places)"
curl -s -X GET http://localhost:5000/api/v1/places/ | jq


echo ""
echo ">>> Test GET (get place by ID)"
curl -s -X GET http://localhost:5000/api/v1/places/$place_id | jq


echo ""
echo ">>> Test PUT (update place)"
curl -s -X PUT http://localhost:5000/api/v1/places/$place_id \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Luxury Condo",
    "description": "An upscale place to stay",
    "price": 200.0
  }' | jq

