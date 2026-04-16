FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for OCR & PDF Processing
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install Python requirements and gunicorn for production server
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

# Expose port (7860 is required by Hugging Face Spaces Docker)
EXPOSE 7860

# Ensure directories exist
RUN mkdir -p uploads_temp outputs

# Start the Flask app using Gunicorn WSGI server
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app", "--timeout", "120"]
