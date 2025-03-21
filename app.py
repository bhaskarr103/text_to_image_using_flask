import os
from flask import Flask, render_template, request, send_from_directory
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from PIL import Image

# Load environment variables
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# Initialize Flask app
app = Flask(__name__)

# Configure Hugging Face Inference Client
client = InferenceClient(model="stabilityai/stable-diffusion-xl-base-1.0")

# Ensure 'static' folder exists for saving images
os.makedirs("static", exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None

    if request.method == "POST":
        prompt = request.form.get("prompt")

        if prompt:
            # Generate image
            image = client.text_to_image(prompt)
            image_path = "static/generated_image.png"
            image.save(image_path, format="PNG")

            # Set image URL
            image_url = image_path

    return render_template("index.html", image_url=image_url)


@app.route("/download")
def download_image():
    return send_from_directory(directory="static", path="generated_image.png", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
