# Use the official Python
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the app using uvicorn
CMD ["uvicorn", "03_model_serving:app", "--host", "0.0.0.0", "--port", "8000"]

