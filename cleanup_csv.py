import csv
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def cleanup_processed_csv(input_csv='processed_images.csv'):
    """
    Nettoie le fichier CSV des images traitées en :
    1. Supprimant les entrées sans URL redimensionnée
    2. Retirant les doublons
    3. Créant une sauvegarde du fichier original
    """
    try:
        # Lecture du CSV original
        valid_entries = []
        seen_urls = set()
        
        with open(input_csv, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                original_url = row.get('image_url', '').strip()
                resized_url = row.get('resized_image_url', '').strip()
                
                # Ne garde que les entrées valides et uniques
                if resized_url and original_url not in seen_urls:
                    valid_entries.append({
                        'image_url': original_url,
                        'resized_image_url': resized_url
                    })
                    seen_urls.add(original_url)

        # Création d'une sauvegarde du fichier original
        backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{input_csv}"
        import shutil
        shutil.copy2(input_csv, backup_name)
        logger.info(f"Sauvegarde créée: {backup_name}")

        # Écriture du nouveau fichier nettoyé
        with open(input_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['image_url', 'resized_image_url'])
            writer.writeheader()
            writer.writerows(valid_entries)

        logger.info(f"Nettoyage terminé. {len(valid_entries)} entrées valides conservées")
        return True

    except Exception as e:
        logger.error(f"Erreur lors du nettoyage du CSV: {str(e)}")
        return False

if __name__ == "__main__":
    cleanup_processed_csv()
