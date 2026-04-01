import requests
import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_image_urls(csv_file='processed_images.csv'):
    """
    Vérifie l'accessibilité des URLs des images redimensionnées
    """
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = row.get('resized_image_url', '')
                if not url:
                    continue
                
                logger.info(f"Vérification de l'URL: {url}")
                response = requests.head(url)
                
                if response.status_code == 200:
                    logger.info(f"✅ URL accessible: {url}")
                    logger.info(f"   Type de contenu: {response.headers.get('content-type', 'Non spécifié')}")
                else:
                    logger.error(f"❌ URL inaccessible: {url}")
                    logger.error(f"   Code de statut: {response.status_code}")

    except Exception as e:
        logger.error(f"Erreur lors de la vérification: {str(e)}")

if __name__ == "__main__":
    check_image_urls()
