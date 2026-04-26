-- Table utilisateurs
CREATE TABLE utilisateurs (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  nom VARCHAR(100) NOT NULL,
  prenom VARCHAR(100) NOT NULL,
  telephone VARCHAR(20),
  langue_preferee VARCHAR(10) DEFAULT 'fr',
  teranga_points INTEGER DEFAULT 0,
  type_connexion VARCHAR(20) DEFAULT 'email',
  created_at TIMESTAMP DEFAULT NOW()
);

-- Table pass JOJ
CREATE TABLE pass_joj (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  utilisateur_id UUID REFERENCES utilisateurs(id),
  code_qr VARCHAR(255) UNIQUE NOT NULL,
  zones_acces TEXT[] DEFAULT ARRAY['tribune'],
  valide_jusqu_au TIMESTAMP,
  actif BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Table lieux (POI)
CREATE TABLE lieux (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  nom VARCHAR(200) NOT NULL,
  type VARCHAR(50) NOT NULL,
  latitude DECIMAL(10, 8) NOT NULL,
  longitude DECIMAL(11, 8) NOT NULL,
  description TEXT,
  rating DECIMAL(3,2),
  distance_stade INTEGER,
  horaires VARCHAR(200),
  telephone VARCHAR(20),
  premium BOOLEAN DEFAULT false,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Table navettes
CREATE TABLE navettes (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  nom VARCHAR(100) NOT NULL,
  depart VARCHAR(200) NOT NULL,
  arrivee VARCHAR(200) NOT NULL,
  lat_depart DECIMAL(10,8),
  lng_depart DECIMAL(11,8),
  lat_arrivee DECIMAL(10,8),
  lng_arrivee DECIMAL(11,8),
  heure_depart TIMESTAMP NOT NULL,
  capacite INTEGER DEFAULT 50,
  places_restantes INTEGER DEFAULT 50,
  statut VARCHAR(20) DEFAULT 'a_lheure',
  created_at TIMESTAMP DEFAULT NOW()
);

-- Table résultats sportifs
CREATE TABLE resultats (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  sport VARCHAR(100) NOT NULL,
  epreuve VARCHAR(200) NOT NULL,
  equipe1 VARCHAR(100),
  equipe2 VARCHAR(100),
  score1 INTEGER DEFAULT 0,
  score2 INTEGER DEFAULT 0,
  statut VARCHAR(20) DEFAULT 'a_venir',
  phase VARCHAR(50),
  heure_debut TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Table historique entrées
CREATE TABLE historique_entrees (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  utilisateur_id UUID REFERENCES utilisateurs(id),
  lieu VARCHAR(200) NOT NULL,
  zone VARCHAR(100),
  entree_at TIMESTAMP DEFAULT NOW()
);

-- Données de test lieux
INSERT INTO lieux (nom, type, latitude, longitude, description, rating) VALUES
('Stade Abdoulaye Wade', 'stade', 14.7645, -17.3660, 'Athlétisme · 50 000 places · Site principal JOJ', 4.9),
('Diamniadio Arena', 'stade', 14.7200, -17.1800, 'Basketball · 15 000 places', 4.8),
('Piscine Olympique', 'stade', 14.6800, -17.4200, 'Natation · Plongeon', 4.7),
('Chez Aminata', 'street_food', 14.6929, -17.4467, 'Thiébou Djeun · Fait maison', 4.8),
('Restaurant Le Baobab', 'restaurant', 14.6850, -17.4390, 'Cuisine sénégalaise traditionnelle', 4.6),
('Maiga Sandaga', 'street_food', 14.6780, -17.4410, 'Street Food local · Pas cher', 4.5),
('Quai B3 Plateau', 'navette', 14.6920, -17.4380, 'Navette → Diamniadio · Toutes les 15 min', null),
('Terminal Petersen', 'navette', 14.6870, -17.4350, 'Navette → Stade Wade · Toutes les 10 min', null);

-- Données de test résultats
INSERT INTO resultats (sport, epreuve, equipe1, equipe2, score1, score2, statut, phase) VALUES
('Basketball', 'Tournoi Masculin', 'Sénégal 🇸🇳', 'Nigeria 🇳🇬', 42, 38, 'en_cours', 'Quart de finale'),
('Athlétisme', '100m Haies Femmes', 'Finale', null, 0, 0, 'a_venir', 'Finale'),
('Natation', '200m Nage Libre', 'Résultats disponibles', null, 0, 0, 'termine', 'Finale');
