# Image Resizer - Automatic Image Resizing Tool

A Python tool that downloads images from URLs, resizes them to **600x600 pixels** with a white background, and automatically hosts them on GitHub.

---

## How It Works

1. Add image URLs to the `images.csv` file
2. Run the script
3. Each image is downloaded, resized, and uploaded to GitHub
4. The new public URLs are saved in `processed_images.csv`

---

## Features

- Resizes images to **600x600 pixels** while preserving the original aspect ratio
- Automatic white background (including transparent PNG images)
- Output format: **WebP** (maximum quality, optimized for the web)
- Free hosting via **GitHub** (direct public URLs)
- Skips images already present in `processed_images.csv`

---

## Installation

### Requirements

- Python 3.x
- A GitHub account with a **Personal Access Token** (scope: `repo`)

### Python Dependencies

```bash
pip install requests Pillow
```

### Configuration

Set your GitHub token as an environment variable:

```bash
export GITHUB_TOKEN=your_github_token
```

---

## Usage

### 1. Prepare your `images.csv` file

```csv
image_url
https://example.com/image1.jpg
https://example.com/image2.png
```

> If the URL contains a comma in the filename, wrap it in quotes:
> `"https://example.com/image,name.webp"`

### 2. Run the script

```bash
python image_resizer.py images.csv
```

### 3. Retrieve the URLs

Resized image URLs are available in `processed_images.csv`:

```csv
image_url,resized_image_url
https://example.com/image1.jpg,https://raw.githubusercontent.com/...
```

---

## File Structure

```
/
├── image_resizer.py        # Main script
├── check_urls.py           # Checks accessibility of generated URLs
├── cleanup_csv.py          # Removes duplicates and invalid CSV entries
├── verify_images.py        # Verifies image dimensions and background color
├── push_to_github.py       # Exports source code to GitHub
├── images.csv              # Source URLs to process
├── processed_images.csv    # Output: original URLs + resized URLs
└── resized_images/         # Local cache of processed images
```

---

## Additional Tools

| Script | Description |
|--------|-------------|
| `check_urls.py` | Verifies that all URLs in `processed_images.csv` are accessible |
| `cleanup_csv.py` | Removes duplicates and rows with missing resized URLs |
| `verify_images.py` | Checks dimensions (600x600) and background color (pure white) |
| `push_to_github.py` | Pushes project files to your GitHub repository |

---

## Technologies

- **Python** — core language
- **Pillow (PIL)** — image processing and resizing
- **Requests** — image downloading and GitHub API calls
- **GitHub API v3** — hosting for resized images

---

## Known Limitations

- GitHub API has rate limits for large volumes of images
- Some websites block automatic downloads (SSL errors or access denied)
- For CSV files with commas in filenames, wrap the URL in double quotes
