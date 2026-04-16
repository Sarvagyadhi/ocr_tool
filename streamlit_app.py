import streamlit as st
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from threading import Thread
from app import app as flask_app

st.set_page_config(page_title="DHI Invoice OCR Tool", layout="wide")
st.title("DHI Invoice OCR Tool")

# Create a combined WSGI application
def run_combined_app():
    combined_app = DispatcherMiddleware(
        lambda environ, start_response: start_response(
            "200 OK", [("Content-Type", "text/plain")]
        ),
        {
            "/flask": flask_app,
        },
    )
    run_simple("0.0.0.0", 5000, combined_app, use_reloader=False)

# Start Flask in a background thread
if "flask_started" not in st.session_state:
    thread = Thread(target=run_combined_app, daemon=True)
    thread.start()
    st.session_state.flask_started = True

# Embed the Flask app
st.markdown("### Invoice OCR Interface")
st.components.v1.iframe(
    src="/flask",
    height=900,
    scrolling=True
)