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

def predict(number):
    if isinstance(number, float):
        st.success('Success message')
        if (1 - number) > 0.9:
            st.write("STAR")
            st.write(f"{1-number}")
        else:
            st.write("GALAXY")
            st.write(f"{1-number}")
    else:
        st.error("ERROR")


set_background('./static/galaxy.png')

code = """
<style>
    h1, h3 {
        color: white;
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

    .e1f1d6gn3 {
        background: rgba(255,255,255, 0.3);
        color: #272F47;
        padding: 5px 25px 25px 25px;
        border-radius: 10px 10px;
    }

    #upload h3 {
        color: #272F47;
    }

    .e1b2p2ww7 {
        color: white;
    }

    .stButton p {
        color: #272F47;
    }



</style>
"""
st.html(code)

images, tabular = st.tabs(["StellarSnap", "StarTable"])



with images:
    st.title('StellarSnap 🚀')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Upload")
        celestial = st.file_uploader("Upload your image",['jpeg'])
        if celestial:
            st.image(celestial)
            submit = st.button("Run")
    with col2:
        st.subheader("Predict")

        predict(0.43)

with tabular:
    st.title('StarTable 🌌')
    col1_tab, col2_tab = st.columns(2)
    with col1_tab:
        st.write("test")
    with col2_tab:
        st.write("display pred")

# submit = st.button('go')
# if submit:
#     api_url = 'https://to-inifinity-and-beyond-image-01-wnxzahsyha-ew.a.run.app/predict_from_image'
#     api_params = {
#     }
#     r = rq.post(api_url, api_params)
#     #r.status_code
#     r.text
