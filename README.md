# 🇸🇳 Infrastructure Publique Numérique (DPI) – Démonstration OpenG2P
### Ministère de l'Agriculture, de la Souveraineté Alimentaire et de l'Élevage du Sénégal

Ce dépôt contient une instance de démonstration clé en main de la plateforme **OpenG2P** (Open Government-to-Person), configurée spécifiquement pour répondre aux enjeux de ciblage, de transparence et de distribution des subventions agricoles au Sénégal. 

Grâce à **GitHub Codespaces**, cette plateforme se déploie instantanément dans le cloud sans aucune installation locale nécessaire.

---

## 🎯 Objectifs de la Démonstration
L'objectif est de montrer comment une Infrastructure Publique Numérique (DPI) basée sur des Biens Publics Numériques (DPG) peut moderniser la gestion des campagnes agricoles à travers deux filières stratégiques :
1. **La Filière Riz (Vallée du Fleuve Sénégal & Anambé) :** Automatisation du ciblage et distribution sécurisée via **Vouchers électroniques** (Bons d'achat d'intrants).
2. **La Filière Arachide (Bassin Arachidier) :** Acheminement direct des subventions de l'État aux producteurs via **Cash Transfer** (Mobile Money).

---

## 🚀 Lancement Rapide (En 1 Clic)

1. En haut de cette page GitHub, cliquez sur le bouton vert **`<> Code`**.
2. Sélectionnez l'onglet **`Codespaces`**.
3. Cliquez sur **`Create codespace on main`**.
4. Patientez 2 à 3 minutes pendant que l'environnement cloud configure l'application OpenG2P et injecte la base de données de test.
5. Dès que l'environnement est prêt, un pop-up apparaît en bas à droite. Cliquez sur **`Open in Browser`** (ou allez dans l'onglet *Ports* et ouvrez le port `8069`) pour accéder à l'interface d'administration.

---

## 🎭 Guide de Présentation : Scénarios Métier à dérouler

Utilisez ce guide comme fil conducteur lors de votre présentation devant les équipes du Ministère.

### 🌾 Scénario 1 : La Filière Riz – Mode "Voucher Électronique"
> **Le besoin ministériel :** Veiller à ce que la subvention de l'État soit exclusivement convertie en engrais Urée et semences certifiées (ex: Sahel 108) au niveau de la SAED, en évitant le détournement des fonds.

* **Étape 1 : Consultation du Registre Unifié (G2P Registry)**
  * Accédez au menu *Registre des bénéficiaires*.
  * Ouvrez le profil de **Amadou Diop** (Localisation : *Saint-Louis/Ross Béthio*).
  * Montrez ses critères d'éligibilité pré-chargés : Taille d'exploitation (*2.5 ha*) et son affiliation certifiée à la coopérative de la SAED.
* **Étape 2 : Le Ciblage Dynamique**
  * Accédez au programme *« Subvention Intrants Riz - Campagne Hivernage »*.
  * Montrez comment le système a automatiquement rattaché Amadou Diop à ce programme sur la base de ses critères géographiques et de sa filière.
* **Étape 3 : Émission du Bon Électronique**
  * Simulez la génération du **Voucher**. La plateforme calcule la valeur de l'aide selon les 2.5 ha déclarés. Un code unique (QR Code / SMS) est généré pour permettre à Amadou de récupérer ses intrants chez un fournisseur agréé.

---

### 🥜 Scénario 2 : La Filière Arachide – Mode "Cash Transfer Direct"
> **Le besoin ministériel :** Injecter rapidement des liquidités auprès des producteurs du Bassin Arachidier (Kaolack, Kaffrine, Diourbel) avant les premières pluies pour financer la préparation des sols et l'achat de semences décortiquées.

* **Étape 1 : Profil et Mode de Paiement Numérique**
  * Ouvrez la fiche de **Fatou Sarr** (Localisation : *Kaolack / Nioro du Rip*).
  * Mettez en avant le fait que son profil intègre directement ses coordonnées de paiement Mobile Money validées (Wave / Orange Money).
* **Étape 2 : Calcul et Orchestration du Flux Financier**
  * Ouvrez le programme *« Soutien Producteurs Arachide - Bassin Arachidier »*.
  * Visualisez la liste des bénéficiaires éligibles et cliquez sur *Generate Payment File*. La plateforme OpenG2P consolide instantanément les montants au prorata des surfaces (ex: 4 ha pour Fatou Sarr).
* **Étape 3 : Simulation du Transfert de Masse (Bulk Payment)**
  * Montrez l'interface d'interfaçage avec les opérateurs financiers. En un clic, l'État valide l'envoi des fonds, déclenchant la notification de réception de cash directement sur le téléphone mobile de l'agriculteur.

---

## 📊 Souveraineté des Données & Pilotage (Reporting)
Terminez la démonstration en montrant l'onglet **Tableau de Bord / Analytics** :
* Expliquez aux directeurs comment ce système offre au Ministère une **visibilité en temps réel à 360°** sur l'utilisation du budget public : taux de consommation des enveloppes budgétaires par région, volume d'intrants distribués, et traçabilité totale des audits financiers.

---

## 🛠️ Architecture Technique du Dépôt
Pour les équipes techniques (DAGE / DSI du Ministère), le projet est structuré selon les standards de l'architecture d'entreprise :
* `.devcontainer/` : Configuration de l'environnement de développement et script d'allumage automatique.
* `docker-compose.yml` : Orchestration multi-conteneurs unissant le cœur du framework OpenG2P (Odoo) et la base de données relationnelle sécurisée PostgreSQL.
* `data-seeds/` : Contient les scripts d'initialisation (`setup_demo.py`) et les fichiers de données d'agriculteurs (`farmers.csv`) spécifiques aux réalités des terroirs sénégalais.
