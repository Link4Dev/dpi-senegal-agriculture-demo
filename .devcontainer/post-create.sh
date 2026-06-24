#!/bin/bash

echo "🇸🇳 Initialisation de la démo OpenG2P pour le Ministère de l'Agriculture..."

BASE_DIR="/workspaces/dpi-senegal-agriculture-demo"
SCRIPT="$BASE_DIR/data-seeds/setup_demo.py"

if [ ! -f "$SCRIPT" ]; then
  echo "❌ Script introuvable : $SCRIPT"
  exit 1
fi

echo "⏳ Attente du démarrage des services..."
sleep 20

echo "🚀 Lancement du script d'initialisation..."
python3 "$SCRIPT"

echo "✅ Initialisation terminée"
echo "👉 Ouvrez le port 8069 pour accéder à Odoo"
