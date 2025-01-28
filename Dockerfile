# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit uses
EXPOSE 8501

# Define environment variable for Streamlit to run on port 8501
ENV STREAMLIT_SERVER_PORT=8501

# Run the Streamlit app when the container starts
CMD ["streamlit", "run", "app.py"]
