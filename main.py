import streamlit as st
from PIL import Image
import pytesseract

# Streamlit App
st.title("Text Extraction from Image")
st.write("Extract text from images using OCR (Tesseract).")

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Open the uploaded image
    image = Image.open(uploaded_image)

    # Display the image
    st.image(image, caption="Uploaded Image.", use_container_width=True)

    if st.button("Extract Text"):
        # Use pytesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(image)

        if extracted_text.strip():
            # Display the extracted text
            st.write("### Extracted Text:")
            st.write(extracted_text)
        else:
            st.warning("No text found in the image.")
