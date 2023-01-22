import streamlit as st
import requests

api = 'Kz9Cd6ANCrAqkQlmoctNMq7Z9ZaZPEJGdJxdmhMv'

url = f'https://api.nasa.gov/planetary/apod?api_key={api}'


response = requests.get(url)
content = response.json()

# download the image
image_filepath = 'image.png'
image_response = requests.get(content['url'])
with open (image_filepath, 'wb') as file:
    file.write(image_response.content)

st.title(content["title"])
st.image(content['url'])
st.write(content['explanation'])


