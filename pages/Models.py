import streamlit as st
import requests as rq
import streamlit.components.v1 as components
import base64
import pandas as pd
import time


st.set_page_config(
     page_title='To infinity and beyond 🚀',
     layout="wide",
     initial_sidebar_state="collapsed",
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

def display_model_name(model_name):
    return f'{str(model_name).capitalize()} is running. 🦿'

def predict_class(number):
    out = ""
    if isinstance(number, float):
        st.success('Processing complete')
        out = "STAR ✨" if number < 0.1 else "GALAXY 🌌"
    return out

def display_redshift(z):
    return f'The predicted redshift value is {z}'

def calc_velocity(z):
    c = 299792.458
    return round(z * c, 2)

def calc_distance_earth_obj(V):
    V = float(V)
    H0 = 73
    Mpc = 3.26
    d = V/H0
    return round(d * Mpc)

def display_prediction(classif, v):
    return st.write(f'This is a **{classif}**! Traveling at **{calc_velocity(v):,}** km/s and being **{calc_distance_earth_obj(v):,}** million-years away from us.')


def get_random_data_for_tabular():
    datum = pd.read_csv('./data/MF.csv')
    return datum.sample()

def get_random_data_for_hybrid():
    datum = pd.read_csv('./data/MF_sample.csv')
    return datum

set_background('./static/galaxy.png')

code = """
<style>
    h1, h3 {
        color: white;
    }

    h1 {
        font-size: 4.5em;
    }

    h3 {
        font-size: 3em;
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
        display: none;
    }

    .stButton p {
        color: #272F47;
    }

    .e1nzilvr4 p {
        font-size: 1.8em;
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
                        with st.spinner(text='R2D2 & Murphy models are working 🔧'):
                            img_bytes = celestial.getvalue()
                            api_url = base_uri + 'category_from_image'
                            api_url_rs = base_uri + 'redshift_from_image'
                            res = rq.post(api_url, files={'file': img_bytes}).json()
                            res_rs = rq.post(api_url_rs, files={'file': img_bytes}).json()
                            classif = predict_class(res['prediction'])
                            V = calc_velocity(res_rs['prediction'])
                            col2.write(display_prediction(classif, V))


filling_data = get_random_data_for_tabular()
filling_data_hybrid = get_random_data_for_hybrid()

with tabular:
    st.title('StarTable 🌌')
    col1_tab, col2_tab = st.columns(2)
    with col1_tab:
        st.subheader("Fill the values")
        form = st.form(key="tabular_data")
        alpha = form.text_input('Alpha',filling_data.alpha.values[0])
        delta = form.text_input('Delta',filling_data.delta.values[0])
        classif = form.text_input('Class',filling_data.label.values[0])
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
            with st.spinner(text='Chewbacca is working 🐻'):
                res_from_params = rq.get(api_url_tab, api_params).json()
                st.write(display_redshift(res_from_params['prediction']))

with millenium:
    st.title('MilleniumSnap🌌')
    col1_fc, col2_fc = st.columns(2)
    celestial_fc = False
    with col1_fc:
        st.subheader('Fill and upload your data ✍️')

        form_fc = st.form(key="hybrid_data")
        celestial_fc = form_fc.file_uploader("Upload your image",['jpeg'], accept_multiple_files=False)
        alpha_fc = form_fc.text_input('Alpha',filling_data_hybrid.alpha.values[0])
        delta_fc = form_fc.text_input('Delta',filling_data_hybrid.delta.values[0])
        classif_fc = form_fc.text_input('Class',filling_data_hybrid.label.values[0])
        uv_fc = form_fc.text_input('Ultraviolet Filter',filling_data_hybrid.u.values[0])
        gf_fc = form_fc.text_input('Green Filter',filling_data_hybrid.g.values[0])
        rf_fc = form_fc.text_input('Red Filter',filling_data_hybrid.r.values[0])
        nf_fc = form_fc.text_input('Near Infrared Filter',filling_data_hybrid.i.values[0])
        irf_fc = form_fc.text_input('Infrared Filter',filling_data_hybrid.z.values[0])
        submit_st_fc = form_fc.form_submit_button("Run")

    with col2_fc:
        st.subheader("Predictions")
        api_url_millenium = base_uri + 'redshift_from_image_and_params'
        if submit_st_fc:
            with st.spinner(text='Millenium Falcon model is working 🛸'):
                img_bytes_millenium = celestial_fc.getvalue()
                api_params_fc = {
                    'alpha':alpha_fc,
                    'delta':delta_fc,
                    'g':uv_fc,
                    'u':gf_fc,
                    'r':rf_fc,
                    'i':nf_fc,
                    'z':irf_fc,
                }
                res_fc = rq.post(api_url_millenium, files={'file': img_bytes_millenium}, data=api_params_fc).json()

                st.write(display_redshift(str(res_fc['prediction'])))
