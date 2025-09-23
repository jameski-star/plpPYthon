import os
import requests
from urllib.parse import urlparse
from urllib.parse import urlunparse

def get_filename_from_url(url):
    """Extracts the filename from the URL or generates one if not available."""
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')
    if path_parts:
        return path_parts[-1] or 'image'  # Use the last part as the filename
    return 'image'  # Default filename if path is empty

def download_image(url, directory='Fetched_Images'):
    """Downloads the image from the URL and saves it to the specified directory."""
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses

        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        # Extract the filename from the URL
        filename = get_filename_from_url(url)
        file_path = os.path.join(directory, filename)

        # Save the image to the file
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Image saved successfully as {filename} in {directory}.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def main():
    print("Ubuntu_Requests: Image Downloader")
    url = input("Please enter the URL of the image: ").strip()

    if not url:
        print("Error: The URL cannot be empty.")
        return

    download_image(url)

if __name__ == "__main__":
    main()