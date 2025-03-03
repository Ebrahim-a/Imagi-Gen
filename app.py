from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey
from streamlit_carousel import carousel


client=OpenAI(api_key=apikey)

single_img=dict(
        title="",
        text="",
        interval=None,
        img="",
    )

def generate_images(image_description, num_images):
    image_gallery=[]
    for i in range(num_images):

        img_response=client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1

        )
        image_url = img_response.data[0].url
        new_image=single_img.copy()
        new_image["title"]=f"Image {i+1}"
        new_image["text"]=image_description
        new_image["img"]=image_url
        image_gallery.append(new_image)
    return image_gallery
st.set_page_config(page_title="Dalle-Image-Generation", page_icon=":camera:", layout="wide")


st.title("DALLE-E-3 Image Generation Tool")


st.subheader("POWERED BY API DALLE - E")
img_description = st.text_input("Enter description for Image")
num_of_images = st.number_input("number of image u want to generate", min_value=1, max_value= 10, value=1)

if st.button("Generate Image"):
    generate_image=generate_images(img_description, num_of_images)

    carousel(items=generate_image,width="100%")
