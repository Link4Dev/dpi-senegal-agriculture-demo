#!/bin/bash
echo "🇸🇳 Initialisation de la démo OpenG2P pour le Ministère de l'Agriculture..."

# Attendre que le conteneur Odoo soit totalement opérationnel avant de lancer le script
sleep 15 

# Exécution du script d'injection des filières Riz & Arachide
python3 /workspace/data-seeds/setup_demo.py

echo "✅ Environnement configuré avec succès !"
echo "👉 Ouvrez l'onglet 'Ports' et cliquez sur l'adresse locale du port 8069 pour accéder à l'interface."
