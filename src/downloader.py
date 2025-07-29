# downloader.py
import requests

print("Loading downloader.py...") # Added print statement

def download_html(url):
    """Downloads the HTML content of a webpage."""
    print(f"Fetching data from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Webpage fetched successfully from {url}!")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage from {url}: {e}")
        return None

print("Finished loading downloader.py") # Added print statement