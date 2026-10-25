
# CODSOFT AI Internship - Task 5
# Face Detection using OpenCV

import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="AI Face Detection",
    page_icon="👤"
)

st.title("AI Face Detection System")
st.write("Upload a photo to detect faces using OpenCV.")

@st.cache_resource
def load_detector():
    cascade_path = (
        cv2.data.haarcascades
        + "haarcascade_frontalface_default.xml"
    )
    return cv2.CascadeClassifier(cascade_path)

uploaded_file = st.file_uploader(
    "Choose a photo",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_array = np.array(image)

    st.subheader("Original Image")
    st.image(image_array, use_container_width=True)

    if st.button("Detect Faces"):
        detector = load_detector()

        gray_image = cv2.cvtColor(
            image_array, cv2.COLOR_RGB2GRAY
        )

        faces = detector.detectMultiScale(
            gray_image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        result = image_array.copy()

        for (x, y, w, h) in faces:
            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                3
            )

        st.subheader("Detection Result")
        st.image(result, use_container_width=True)

        st.success(
            f"Number of faces detected: {len(faces)}"
        )

        if len(faces) == 0:
            st.info(
                "No faces detected. Try a clear, front-facing photo."
            )
