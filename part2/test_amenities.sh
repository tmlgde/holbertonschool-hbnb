#!/bin/bash

echo ">>> Test POST (create amenity)"
response=$(curl -s -X POST http://localhost:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Wi-Fi"}')

echo "$response"
id=$(echo "$response" | jq -r '.id')

if [ "$id" == "null" ] || [ -z "$id" ]; then
  echo "❌ Échec de la création de l'amenity, ID non trouvé."
  exit 1
fi

echo "✅ Amenity créée avec l'ID : $id"
echo ""

echo ">>> Test GET (get all amenities)"
curl -s http://localhost:5000/api/v1/amenities/ | jq
echo ""

echo ">>> Test GET (get amenity by ID)"
curl -s http://localhost:5000/api/v1/amenities/$id | jq
echo ""

echo ">>> Test PUT (update amenity)"
curl -s -X PUT http://localhost:5000/api/v1/amenities/$id \
  -H "Content-Type: application/json" \
  -d '{"name": "Climatisation"}' | jq
echo ""

