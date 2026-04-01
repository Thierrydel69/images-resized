# Image Resizer - Redimensionnement automatique d'images

Un outil Python qui télécharge des images depuis des URLs, les redimensionne en **600x600 pixels** avec un fond blanc, et les héberge automatiquement sur GitHub.

---

## Fonctionnement

1. Vous ajoutez des URLs d'images dans le fichier `images.csv`
2. Vous lancez le script
3. Chaque image est téléchargée, redimensionnée et uploadée sur GitHub
4. Les nouvelles URLs publiques sont enregistrées dans `processed_images.csv`

---

## Caractéristiques

- Redimensionnement en **600x600 pixels** avec les proportions d'origine conservées
- Fond blanc automatique (même pour les images avec transparence PNG)
- Format de sortie **WebP** (qualité maximale, optimisé pour le web)
- Hébergement gratuit via **GitHub** (URLs publiques directes)
- Evite de retraiter les images déjà présentes dans `processed_images.csv`

---

## Installation

### Prérequis

- Python 3.x
- Un compte GitHub avec un **Personal Access Token** (scope `repo`)

### Dépendances Python

```bash
pip install requests Pillow
```

### Configuration

Créez une variable d'environnement avec votre token GitHub :

```bash
export GITHUB_TOKEN=votre_token_github
```

---

## Utilisation

### 1. Préparez votre fichier `images.csv`

```csv
image_url
https://example.com/image1.jpg
https://example.com/image2.png
```

> Si l'URL contient une virgule dans le nom du fichier, mettez-la entre guillemets :
> `"https://example.com/image,nom.webp"`

### 2. Lancez le script

```bash
python image_resizer.py images.csv
```

### 3. Récupérez les URLs

Les URLs des images redimensionnées sont disponibles dans `processed_images.csv` :

```csv
image_url,resized_image_url
https://example.com/image1.jpg,https://raw.githubusercontent.com/...
```

---

## Structure des fichiers

```
/
├── image_resizer.py        # Script principal
├── check_urls.py           # Vérifie l'accessibilité des URLs générées
├── cleanup_csv.py          # Nettoie les doublons et entrées invalides du CSV
├── verify_images.py        # Vérifie les dimensions et le fond des images
├── push_to_github.py       # Exporte le code source vers GitHub
├── images.csv              # URLs sources à traiter
├── processed_images.csv    # Résultat : URLs originales + URLs redimensionnées
└── resized_images/         # Cache local des images traitées
```

---

## Outils complémentaires

| Script | Description |
|--------|-------------|
| `check_urls.py` | Vérifie que toutes les URLs dans `processed_images.csv` sont accessibles |
| `cleanup_csv.py` | Supprime les doublons et les lignes sans URL redimensionnée |
| `verify_images.py` | Contrôle les dimensions (600x600) et la couleur du fond (blanc pur) |
| `push_to_github.py` | Exporte les fichiers du projet vers votre dépôt GitHub |

---

## Technologies utilisées

- **Python** — langage principal
- **Pillow (PIL)** — traitement et redimensionnement des images
- **Requests** — téléchargement des images et appels à l'API GitHub
- **GitHub API v3** — hébergement des images redimensionnées

---

## Limites connues

- L'API GitHub a des limites de débit (rate limits) pour les gros volumes d'images
- Certains sites bloquent le téléchargement automatique (erreurs SSL ou accès refusé)
- Pour les fichiers CSV avec des virgules dans les noms de fichiers, pensez à entourer l'URL de guillemets
