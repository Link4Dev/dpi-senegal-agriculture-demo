import os
import xmlrpc.client
import csv

print("🇸🇳 Début de la configuration des programmes de subvention Sénégal...")

# Connexion à l'instance OpenG2P/Odoo locale du Codespace
url = 'http://localhost:8069'
db = 'postgres'
username = 'admin'
password = 'admin_password_demo' # À adapter selon la conf d'initialisation

try:
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
    print("✅ Connexion réussie à l'API OpenG2P.")
except Exception as e:
    print("⚠️ Impossible de se connecter à OpenG2P (Instance en cours de démarrage ou identifiants par défaut manquants).")
    uid = None

if uid:
    # 1. Création du Programme 1 : RIZ (Mode Voucher)
    prog_riz_id = models.execute_kw(db, uid, password, 'g2p.program', 'create', [{
        'name': 'Subvention Intrants Riz - Campagne Hivernage',
        'code': 'SUBV-RIZ-2026',
        'delivery_type': 'voucher',  # Mode Bon d'achat
        'description': 'Distribution de bons électroniques pour engrais Urée et semences certifiées (Zone SAED & Anambé).'
    }])
    print(f"🌾 Programme RIZ (Voucher) créé avec l'ID: {prog_riz_id}")

    # 2. Création du Programme 2 : ARACHIDE (Mode Cash Transfer)
    prog_arachide_id = models.execute_kw(db, uid, password, 'g2p.program', 'create', [{
        'name': 'Soutien Producteurs Arachide - Bassin Arachidier',
        'code': 'CASH-ARACH-2026',
        'delivery_type': 'cash',     # Mode Transfert Mobile Money
        'description': 'Transfert monétaire direct pour l'achat de semences d'arachides et NPK (Kaolack, Kaffrine, Diourbel).'
    }])
    print(f"🥜 Programme ARACHIDE (Cash) créé avec l'ID: {prog_arachide_id}")

    # 3. Importation et ciblage des agriculteurs depuis le CSV
    csv_path = '/workspace/data-seeds/farmers.csv'
    if os.path.exists(csv_path):
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Création du profil bénéficiaire
                beneficiary_id = models.execute_kw(db, uid, password, 'g2p.beneficiary', 'create', [{
                    'firstname': row['prenom'],
                    'lastname': row['nom'],
                    'phone': row['telephone'],
                    'location_state': row['region'],
                    'farm_size_ha': float(row['surface_ha']),
                    'cooperative_status': row['statut_cooperative']
                }])
                
                # Assignation au bon programme selon la filière
                if row['filiere'] == 'RIZ':
                    models.execute_kw(db, uid, password, 'g2p.program.membership', 'create', [{
                        'program_id': prog_riz_id,
                        'beneficiary_id': beneficiary_id,
                        'status': 'eligible'
                    }])
                elif row['filiere'] == 'ARACHIDE':
                    models.execute_kw(db, uid, password, 'g2p.program.membership', 'create', [{
                        'program_id': prog_arachide_id,
                        'beneficiary_id': beneficiary_id,
                        'status': 'eligible'
                    }])
        print("✅ Registre des agriculteurs importé et assigné aux programmes correspondants.")
