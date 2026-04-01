# Image Resizing and URL Management System

## Overview

This repository contains a Python-based image processing system designed to resize images and manage their URLs through GitHub integration. The system downloads images from external URLs, resizes them to standardized dimensions, uploads them to a GitHub repository, and maintains a CSV database of original and resized image URLs.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

The system follows a modular Python architecture with clear separation of concerns:

1. **Image Processing Pipeline**: Downloads, resizes, and uploads images
2. **URL Management**: Tracks original and processed image URLs in CSV format
3. **GitHub Integration**: Uses GitHub as a CDN for storing resized images
4. **Verification System**: Includes multiple validation and cleanup utilities

## Key Components

### Core Processing Module (`image_resizer.py`)
- **Purpose**: Main image processing engine
- **Functionality**: Downloads images, resizes to 600x600 pixels, uploads to GitHub
- **Technologies**: PIL/Pillow for image processing, GitHub API for storage
- **Architecture Decision**: Uses GitHub as a free CDN solution for image hosting

### URL Verification (`check_urls.py`)
- **Purpose**: Validates accessibility of resized image URLs
- **Functionality**: Performs HTTP HEAD requests to verify image availability
- **Design Choice**: Uses HEAD requests instead of GET for efficiency

### Data Cleanup Utilities
- **`cleanup_csv.py`**: Removes duplicates and invalid entries from the CSV database
- **`verify_images.py`**: Cross-validates local files with CSV records

### CSV Database Structure
- **Fields**: `image_url` (original), `resized_image_url` (processed)
- **Format**: UTF-8 encoded CSV for cross-platform compatibility

## Data Flow

1. **Input**: Original image URLs (source not specified in current codebase)
2. **Processing**: 
   - Download image from original URL
   - Resize to standardized dimensions (600x600)
   - Upload to GitHub repository
   - Generate public GitHub URL
3. **Storage**: Record URL mapping in CSV file
4. **Verification**: Validate accessibility and integrity

## External Dependencies

### Required Python Packages
- `requests`: HTTP client for downloading images and GitHub API calls
- `Pillow (PIL)`: Image processing and manipulation
- `csv`: Built-in CSV handling
- `logging`: Built-in logging framework

### External Services
- **GitHub API**: Primary storage backend for resized images
- **GitHub Repository**: `Thierrydel69/images-resized` (main branch)

### Environment Variables
- `GITHUB_TOKEN`: Required for GitHub API authentication

## Deployment Strategy

### Configuration Requirements
1. Set `GITHUB_TOKEN` environment variable
2. Ensure target GitHub repository exists and is accessible
3. Install required Python dependencies

### File Structure
```
/
├── resized_images/          # Local cache directory
├── processed_images.csv     # URL mapping database
├── image_resizer.py        # Main processing module
├── check_urls.py           # URL verification utility
├── cleanup_csv.py          # Data cleanup utility
└── verify_images.py        # Image verification utility
```

### Operational Considerations
- **Storage**: Uses GitHub repository as permanent storage
- **Backup**: Automatic backup creation before CSV cleanup operations
- **Error Handling**: Comprehensive logging throughout all modules
- **Format Support**: JPEG, PNG, WebP image formats

### Scalability Notes
- GitHub API rate limits may affect batch processing
- Local storage is used for temporary caching only
- CSV database may become unwieldy with large datasets (consider migration to proper database for scale)