from resume_analyze import upload_file
import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from PIL import Image


def load_model():
    model = MobileNetV2(weights="imagenet")
    return model

def preprocess_image(image):
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (224,224))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis = 0)
    return img

def Classify_image(model,image):
    try:
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        decoded_prediction = decode_predictions(predictions, top=3)[0]
        
        return decoded_prediction
    
    except Exception as e:
        st.error(f"Error classifying image: {str(e)}")
        return None

def main():
    st.set_page_config(page_title = "AI Image Classifier", page_icon = "🔍",layout="centered")
    
    st.title("AI Image Classifier 🤖")
    st.write("Upload an image and let AI identify objects with 90% accuracy!")

    @st.cache_resource
    def load_cached_model():
        return load_model()
    
    model = load_cached_model()

    upload_file = st.file_uploader("choose an image...", type = ["jpeg", "jpg", "png", "bmp"])


    if upload_file is not None:
        image = st.image(
            upload_file, caption="Uploaded Image", use_container_width=True
        )
        btn = st.button("Classify Image")

        if btn:
            with st.spinner("Analyzing Image..."):
                image = Image.open(upload_file)
                predictions = Classify_image(model, image)

                if predictions:
                    st.subheader("Predictions")
                    for _, lable, score in predictions:
                        st.write(f"**{lable}** : {score:.2f}%") 

if __name__ == "__main__":
    main()    

    
    
    