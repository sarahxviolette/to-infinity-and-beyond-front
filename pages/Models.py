import streamlit as st
import requests as rq
import streamlit.components.v1 as components
import base64
import pandas as pd


st.set_page_config(
     page_title='To infinity and beyond 🚀',
     layout="wide",
     initial_sidebar_state="expanded",
)

base_uri = "https://to-inifinity-and-beyond-image-01-wnxzahsyha-ew.a.run.app/"

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
        st.success('Processing complete')
        if number < 0.1:
            st.markdown("This is a **STAR**")
        else:
            st.markdown("This is a **GALAXY**")
    else:
        st.error("Error please retry")


def calc_velocity(z):
    c = 299792.458
    #return f'Traveling at {round(z * c, 2)} km/s'
    return f'{round(z * c, 2)}'

def calc_distance_earth_obj(V):
    V = float(V)
    H0 = 73
    Mpc = 3.26
    d = V/H0
    return f'{round(d * Mpc)} million-years away from us'

def get_random_data_for_tabular():
    datum = pd.read_csv('./data/sample_data.csv')
    return datum.sample()

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

images, tabular, millenium = st.tabs(["StellarSnap", "StarTable", "Millenium"])


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
                # Show a spinner during a process
                with col2:
                        with st.spinner(text='Image processing in progress'):
                            img_bytes = celestial.getvalue()
                            api_url = base_uri + 'category_from_image'
                            api_url_rs = base_uri + 'redshift_from_image'
                            res = rq.post(api_url, files={'file': img_bytes}).json()
                            res_rs = rq.post(api_url_rs, files={'file': img_bytes}).json()
                            classif = predict(res['prediction'])
                            col2.write(classif)
                            V = calc_velocity(res_rs['prediction'])
                            col2.write(V)
                            col2.write(calc_distance_earth_obj(V))


filling_data = get_random_data_for_tabular()
print(filling_data.g.all)
print(filling_data.u.values)
print(filling_data.i.values)
print(filling_data.class_obj.values)
with tabular:
    st.title('StarTable 🌌')
    col1_tab, col2_tab = st.columns(2)
    with col1_tab:
        st.subheader("Fill the values")
        form = st.form(key="tabular_data")
        alpha = form.text_input('Alpha',filling_data.alpha.values[0])
        delta = form.text_input('Delta',filling_data.delta.values[0])
        classif = form.text_input('Class',filling_data.class_obj.values[0])
        uv = form.text_input('Ultraviolet Filter',filling_data.u.values[0])
        gf = form.text_input('Green Filter',filling_data.g.values[0])
        rf = form.text_input('Red Filter',filling_data.r.values[0])
        nf = form.text_input('Near Infrared Filter',filling_data.i.values[0])
        irf = form.text_input('Infrared Filter',filling_data.z.values[0])
        submit_st = form.form_submit_button("Run")

    with col2_tab:
        st.subheader("Prediction")
        if submit_st:
            api_params = {
                'alpha':alpha,
                'delta':delta,
                'label':classif,
                'g':uv,
                'u':gf,
                'r':rf,
                'i':nf,
                'z':irf,
            }
            api_url_tab = base_uri + "redshift_from_params"
            with st.spinner(text='Image processing in progress'):
                res_from_params = rq.get(api_url_tab, api_params).json()
