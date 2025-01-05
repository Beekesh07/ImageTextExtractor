import streamlit as st
from PIL import Image
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

# Define the Hugging Face model name for OCR (you can choose another model if needed)
model_name = "microsoft/layoutlmv3-base"

# Load the model and tokenizer
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Streamlit App
st.title("Text Extraction from Image")
st.write("Extract text from images using a pre-trained model from Hugging Face.")

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Open the uploaded image
    image = Image.open(uploaded_image)

    # Display the image
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    if st.button("Extract Text"):
        # Preprocessing the image for the model (resize, normalize, etc.)
        # The model will need the image in a specific format; you can preprocess as per the model's needs.

        # Placeholder for the image text extraction logic
        # For now, we assume you'd have OCR logic here, for example using pytesseract or another OCR tool
        # You can use Hugging Face's models directly, but for OCR, a specific model that supports image inputs is needed

        # Example: Placeholder for text extraction (replace with actual model inference code)
        extracted_text = "Extracted text goes here."  # Replace with model output

        # Display the extracted text
        st.write("### Extracted Text:")
        st.write(extracted_text)
