import streamlit as st
import base64
from pathlib import Path

CURRENT_FOLDER = Path(__file__).parent
LOGO_FILE_PATH = CURRENT_FOLDER / "njr_logo.png"

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

NJR_LOGO = get_base64_image(LOGO_FILE_PATH)

def footer_home():
    st.markdown(f"""
        <div style="margin-top: 2rem; display: flex; gap: 6px; justify-content: center; align-items: center;">
            <p style="font-weight: bold; color: white; margin: 0;">Created with ❤️ by</p>
            <img src="{NJR_LOGO}" style="max-height: 25px; width: auto;" alt="NJR Logo" />
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    st.markdown(f"""
        <div style="margin-top: 2rem; display: flex; gap: 6px; justify-content: center; align-items: center;">
            <p style="font-weight: bold; color: black; margin: 0;">Created with ❤️ by</p>
            <img src="{NJR_LOGO}" style="max-height: 25px; width: auto;" alt="NJR Logo" />
        </div>
    """, unsafe_allow_html=True)