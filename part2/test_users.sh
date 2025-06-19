#!/bin/bash

# Créer un utilisateur
echo ">>> Test POST (create user)"
curl -s -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"}' | tee response.json

echo -e "\n\n"

# Extraire l'ID créé
USER_ID=$(jq -r '.id' response.json)

# Vérifier si l'ID est bien récupéré
if [ "$USER_ID" == "null" ] || [ -z "$USER_ID" ]; then
  echo "Échec de la création de l'utilisateur, ID non trouvé."
  exit 1
fi

# Lire les détails de l'utilisateur
echo ">>> Test GET by ID (user ID = $USER_ID)"
curl -s http://localhost:5000/api/v1/users/$USER_ID | jq
echo -e "\n\n"

# Modifier l'utilisateur
echo ">>> Test PUT (update user)"
curl -s -X PUT http://localhost:5000/api/v1/users/$USER_ID \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"}' | jq

echo -e "\n\n"

# Liste tous les utilisateurs
echo ">>> Test GET all users"
curl -s http://localhost:5000/api/v1/users/ | jq
