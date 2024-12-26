#!/bin/bash

echo "Ajout des fichiers..."
git add .

echo "Commit des modifications..."
git commit -m "Mise à jour automatique"

echo "Pousser sur GitHub..."
git push origin main

echo "Lancement du conteneur Docker..."
docker-compose down
docker-compose up --build -d

