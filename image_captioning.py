
import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

st.set_page_config(
    page_title="AI Image Captioning",
    page_icon="🖼️",
    layout="centered"
)

st.title("🖼️ AI Image Captioning")
st.write("Upload an image and let AI describe it!")

@st.cache_resource
def load_model():
    model_name = "Salesforce/blip-image-captioning-base"

    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(
        model_name
    )

    model.eval()
    return processor, model

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Your uploaded image",
        use_container_width=True
    )

    if st.button("Generate Caption"):
        try:
            with st.spinner("AI is analyzing your image..."):
                processor, model = load_model()

                inputs = processor(
                    images=image,
                    return_tensors="pt"
                )

                with torch.no_grad():
                    output = model.generate(
                        **inputs,
                        max_new_tokens=50,
                        num_beams=4
                    )

                caption = processor.decode(
                    output[0],
                    skip_special_tokens=True
                )

            st.success("Caption generated successfully!")
            st.subheader("AI Generated Caption")
            st.write(caption)

        except Exception as error:
            st.error(
                "Something went wrong. Check your internet "
                "connection and installed packages."
            )
            st.exception(error)
