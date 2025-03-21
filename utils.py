import os
import requests

def save_image(image_url, folder="static/images"):
    """Download and save image from URL."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    response = requests.get(image_url)
    filename = os.path.join(folder, "generated_image.jpg")
    with open(filename, "wb") as file:
        file.write(response.content)
    return filename
