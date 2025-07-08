import streamlit as st
import time
from image_fetcher import fetch_ice_cream_image

st.set_page_config(page_title="🍦 Inpay's Ice Cream Shop", layout="centered")

# Auto-start loop when app runs
if "looping" not in st.session_state:
    st.session_state.looping = True  # Auto-start enabled

st.title("🍨 Inpay's Ice Cream Shop")

# Main loop
if st.session_state.looping:
    img_url = fetch_ice_cream_image()
    if img_url:
        st.image(img_url, caption="Data & AI LOVES Ice cream", use_container_width=True)
    else:
        st.warning("No image found. Try again.")

    time.sleep(3)
    st.rerun()
