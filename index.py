import requests
import os
from urllib.parse import urlparse
from datetime import datetime


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for URL
    url = input("Please enter the image URL: ").strip()

    # Create directory if it doesn’t exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error for bad HTTP status

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:  # if empty, generate one
            filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

        # Full path
        filepath = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}\n")

    except requests.exceptions.MissingSchema:
        print("⚠ Invalid URL. Please make sure you enter a valid image link.")
    except requests.exceptions.HTTPError as e:
        print(f"⚠ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("⚠ Connection Error. Please check your internet connection.")
    except Exception as e:
        print(f"⚠ An unexpected error occurred: {e}")

    print("Connection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
