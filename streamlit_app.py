import threading
import streamlit as st
import streamlit.components.v1 as components

# Start Flask in a background thread
def run_flask():
    from app import app
    app.run(host="0.0.0.0", port=5000, debug=False)

thread = threading.Thread(target=run_flask, daemon=True)
thread.start()

st.set_page_config(
    page_title="DHI - InvoiceOCR",
    layout="wide"
)

st.title("DHI Invoice OCR Tool")

components.iframe(
    "http://localhost:5000",
    height=900,
    scrolling=True
)