Cryptocurrency Liquidity Prediction API
Project Description
This project provides a robust, containerized API for predicting cryptocurrency liquidity based on historical and real-time market data. The core of the application is a machine learning model, specifically a Random Forest Regressor, trained to predict future liquidity values.

The entire application is packaged within a Docker container, ensuring a consistent and reproducible environment for deployment and scaling.

Key Features
Machine Learning Model: Utilizes a pre-trained scikit-learn Random Forest model for accurate liquidity prediction.

RESTful API: Provides a clean and accessible API endpoint (/predict) for making predictions.

Data Preprocessing: The API handles the necessary data encoding and transformation, allowing users to send raw categorical data directly.

Dockerized Environment: The entire application runs inside a Docker container, simplifying setup and deployment.

Technologies
Python: The core programming language.

Flask: A lightweight web framework for building the API.

scikit-learn: The machine learning library used for the model and preprocessing.

Pandas & NumPy: Essential libraries for data manipulation.

Docker: Used to package the application and its dependencies into a single, portable image.

Getting Started
To run this application, you must have Docker installed on your machine.

Clone the Repository:

git clone [https://github.com/your-username/your-project.git](https://github.com/your-username/your-project.git)
cd your-project




Verify Files: Ensure the project directory contains the following files and directories:

app.py (The Flask application)

Dockerfile (The build instructions for Docker)

requirements.txt (List of Python dependencies)

model/ (This directory should contain your Randomforest_Regression_model.pkl and encoder.pkl files)

Build the Docker Image:
From your terminal, navigate to the project's root directory and run the following command to build the Docker image.

docker build -t crypto-predictor .




Run the Docker Container:
After the build is complete, run the container and map the internal port 5000 to your machine's port 5000.

docker run -p 5000:5000 crypto-predictor




The Flask API should now be running and accessible at http://localhost:5000.

API Endpoint
The application exposes a single endpoint for predictions.

POST /predict

Description: Accepts a JSON payload of input features and returns a predicted liquidity value.

Headers: Content-Type: application/json

Request Body (JSON):

{
  "Time": 1715011200,
  "Asset_ID": 1,
  "Open": 29000.0,
  "High": 30000.0,
  "Low": 28500.0,
  "Volume": 15000.0,
  "Count": 5000,
  "VWAP": 29250.0
}




Example curl command:

curl -X POST -H "Content-Type: application/json" -d '{ "Time": 1715011200, "Asset_ID": 1, "Open": 29000.0, "High": 30000.0, "Low": 28500.0, "Volume": 15000.0, "Count": 5000, "VWAP": 29250.0 }' http://localhost:5000/predict




Input Features
The API endpoint expects a JSON payload with the following features:

Time (Integer): The timestamp of the market data, in Unix time.

Asset_ID (Integer): A unique identifier for the cryptocurrency asset.

Open (Float): The opening price of the asset during a time window.

High (Float): The highest price of the asset during a time window.

Low (Float): The lowest price of the asset during a time window.

Volume (Float): The total volume traded for the asset during a time window.

Count (Integer): The number of trades for the asset during a time window.

VWAP (Float): Volume-Weighted Average Price, which is the average price weighted by volume.

Project Structure
crypto-predictor/
├── app.py
├── data/
├── Dockerfile
├── requirements.txt
├── README.md
├── scripts/
└── notebooks/
└── model/
    ├── RandomForest_Regression_model.pkl
    └── encoder.pkl

