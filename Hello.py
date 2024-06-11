import streamlit as st
import requests as rq
import streamlit.components.v1 as components
import base64

st.set_page_config(
     page_title='To infinity and beyond 🚀',
     layout="wide",
     initial_sidebar_state="expanded",
)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-color: #272F47;
    }
    </style>
    ''' % bin_str
    st.html(page_bg_img)

set_background('./static/galaxy.png')
code = """
<style>
    h1{
        color: white; important!
    }

    p {
        color: #FFFFFF;
    }

    .eczjsme8{
        background-color: #FFFFFF;
        color: #272F47;
    }
    .eczjsme8 h1{
        color: #272F47;
    }


</style>
"""
st.html(code)


st.title('Le Wagon\'s space agency 🪐')
st.write("Welcome to the unoffical secret space agency, thanks to our over-boosted models you can upload a picture taken from a telescope and know how far you are from the selected celestial object")
