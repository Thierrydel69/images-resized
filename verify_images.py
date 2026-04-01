import os
import csv
import requests
from PIL import Image

def verify_resized_images(csv_file='processed_images.csv'):
    """
    Vérifie les images redimensionnées et leurs URLs
    """
    print("Vérification des images redimensionnées et des URLs...")

    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                original_url = row.get('image_url', '')
                resized_url = row.get('resized_image_url', '')

                if not resized_url:
                    print(f"❌ Pas d'URL redimensionnée pour: {original_url}")
                    continue

                print(f"\nImage originale: {original_url}")
                print(f"URL redimensionnée: {resized_url}")

                # Vérification du fichier local
                filename = resized_url.split('/')[-1]
                local_path = os.path.join('resized_images', filename)

                if os.path.exists(local_path):
                    with Image.open(local_path) as img:
                        print(f"✅ Image locale trouvée: {local_path}")
                        print(f"   Dimensions: {img.size[0]}x{img.size[1]}")
                else:
                    print(f"❌ Image locale non trouvée: {local_path}")

    except FileNotFoundError:
        print(f"❌ Fichier CSV non trouvé: {csv_file}")
    except Exception as e:
        print(f"❌ Erreur lors de la vérification: {str(e)}")

if __name__ == "__main__":
    verify_resized_images()