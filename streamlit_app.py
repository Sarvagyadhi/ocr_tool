import threading
import time
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="DHI Invoice OCR Tool", layout="wide")

st.title("DHI Invoice OCR Tool")
st.subheader("Invoice OCR Interface")

# Function to run Flask app
def run_flask():
    from app import app
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

# Start Flask only once
if "flask_started" not in st.session_state:
    thread = threading.Thread(target=run_flask, daemon=True)
    thread.start()
    st.session_state.flask_started = True
    time.sleep(3)  # Give Flask time to start

st.success("Flask server is running.")

# Embed Flask UI
components.iframe(
    src="http://localhost:5000",
    height=900,
    scrolling=True
)