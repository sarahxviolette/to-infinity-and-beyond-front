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
        if number < 0.1:
            st.write("STAR")
        else:
            st.write("GALAXY")
    else:
        st.error("Error please retry")


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
    submit = False
    col2.subheader("Predict")
    with col1:
        st.subheader("Upload")
        celestial = st.file_uploader("Upload your image",['jpeg'], accept_multiple_files=False)
        if celestial:
            img_cel = st.image(celestial)
            submit = st.button("Run")
            if submit:
                col2.write("lol")
                img_bytes = celestial.getvalue()
                api_url = 'https://to-inifinity-and-beyond-image-01-wnxzahsyha-ew.a.run.app/predict_from_image'
                res = rq.post(api_url, files={'file': img_bytes}).json()

                col2.write(predict(res['prediction']))
                # col2.write(res.json['prediction'])
                #st.write(r.json.prediction)

with tabular:
    st.title('StarTable 🌌')
    col1_tab, col2_tab = st.columns(2)
    with col1_tab:
        st.write("test")
    with col2_tab:
        st.write("display pred")
