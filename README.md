
# Profit Prediction App

This app predicts the profit based on the product line and quantity using a pre-trained Decision Tree model. It also generates a summarized analysis using AI.

---

## Table of Contents

- [Installation Instructions](#installation-instructions)
- [Running the Code Locally](#running-the-code-locally)
- [Docker Setup](#docker-setup)
- [Deploy with Render](#deploy-with-render)
- [GitHub Actions for CI/CD](#github-actions-for-cicd)

---

## Installation Instructions

To get started with the `Profit Prediction App`, follow these instructions.

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/profit-prediction-app.git
cd profit-prediction-app
```

### Step 2: Install Dependencies

Create a virtual environment to isolate the project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Now install the required dependencies by running:

```bash
pip install -r requirements.txt
```

This will install the necessary Python libraries such as Streamlit, pandas, scikit-learn, and others.

### Step 3: Set up the `.env` File
Create a `.env` file in the root directory of the project to store your API keys.

```env
GROQ_API_KEY=your_api_key_here
```

Make sure to replace `your_api_key_here` with your actual API key.

---

## Running the Code Locally

To run the app locally, make sure you have all the dependencies installed and the `.env` file is set up correctly.

Start the Streamlit app with the following command:

```bash
streamlit run app.py
```

Once the app is running, you can visit it on `http://localhost:8501` in your browser.

---

## Docker Setup

### Step 1: Build the Docker Image

To containerize the app with Docker, make sure you have Docker installed on your machine.

Build the Docker image by running the following command:

```bash
docker build -t profit-prediction-app .
```

### Step 2: Run the Docker Container

After the image is built, you can run the container:

```bash
docker run -p 8501:8501 profit-prediction-app
```

This will make the app available on `http://localhost:8501` in your browser.

---

## Deploy with Render

Render is a platform that allows you to deploy your apps easily. Follow the steps below to deploy the app using Docker on Render.

### Step 1: Push the Code to GitHub

1. Initialize a git repository (if not already done):
   ```bash
   git init
   ```
2. Commit and push the code to GitHub.

### Step 2: Set up Render

1. Sign up for a Render account (if you don't have one) at [Render](https://render.com/).
2. After logging in, click on **New Web Service**.
3. Connect your GitHub repository by selecting it from the available options.
4. Select the **Docker** option when asked for the service type.
5. Set the environment variables (like `GROQ_API_KEY`) in the Render dashboard.

### Step 3: Deploy

Click **Deploy** and Render will automatically build and deploy the application using the `Dockerfile`.

---

## GitHub Actions for CI/CD

To automate the deployment process, you can use GitHub Actions to build and deploy your app to Render.

### Step 1: Create a GitHub Actions Workflow

1. Inside your repository, navigate to `.github/workflows` (create the folders if they don’t exist).
2. Create a new file named `deploy.yml` in the `.github/workflows` directory.

Add the following YAML configuration for GitHub Actions:

```yaml
name: Deploy to Render

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
        
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

      - name: Build Docker image
        run: |
          docker build -t profit-prediction-app .

      - name: Push Docker image to Render
        env:
          RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}
        run: |
          curl -X POST https://api.render.com/v1/services/<your_service_id>/deploy \
          -H "Authorization: Bearer $RENDER_API_KEY"
```

### Step 2: Add Render API Key to GitHub Secrets

1. Go to your GitHub repository.
2. Navigate to **Settings > Secrets**.
3. Add a new secret with the name `RENDER_API_KEY` and set its value to your Render API key.

### Step 3: Push Changes to GitHub

Push your changes to the `main` branch, and the GitHub Actions workflow will automatically run to deploy the app to Render.

---

## Summary

You now have everything set up to:
- Run the app locally with Streamlit.
- Dockerize the app for easy deployment.
- Deploy the app to Render using GitHub Actions for CI/CD.

