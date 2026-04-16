import threading
import streamlit as st
import streamlit.components.v1 as components

# Start Flask in a background thread
def run_flask():
    from app import app
    app.run(port=5000)

thread = threading.Thread(target=run_flask, daemon=True)
thread.start()

st.set_page_config(page_title="DHI - InvoiceLens", layout="wide")
st.markdown("<style>iframe{border:none;}</style>", unsafe_allow_html=True)

components.iframe("http://localhost:5000", height=900, scrolling=True)