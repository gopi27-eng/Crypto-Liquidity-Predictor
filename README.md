### 
Cryptocurrency Liquidity Predictor
Project Overview
This project presents a robust, machine learning-powered API for predicting cryptocurrency liquidity. It leverages a pre-trained Random Forest Regressor model to provide accurate liquidity forecasts based on key market indicators like price changes, volume, and market capitalization. The entire application is containerized with Docker, ensuring a portable, reproducible, and easily deployable solution for data scientists and developers.

Problem Statement
Cryptocurrency markets are known for their high volatility, where liquidity—the ease of buying or selling assets without significant price impact—plays a crucial role in market stability. A lack of liquidity can lead to sharp price fluctuations and instability.

This project addresses this by building a machine learning model to predict liquidity levels, helping traders and exchange platforms manage risks effectively by forecasting liquidity variations.

Key Features
Predictive API: A RESTful API built with Flask that accepts cryptocurrency data and returns a liquidity prediction.

Containerization: The entire application, including all dependencies and models, is containerized using Docker for easy deployment and portability.

Machine Learning Model: Utilizes a Random Forest Regressor trained on historical market data.

Tech Stack
Language: Python

Framework: Flask

Libraries: scikit-learn, pandas, numpy

Containerization: Docker

How to Run the Project
This project is designed to be run easily using Docker. Follow these two simple steps to get the application up and running on your local machine.

1. Build the Docker Image
First, you need to build the Docker image from the provided Dockerfile. Open your terminal in the root directory of this project and run the following command:

docker build -t crypto-predictor .

2. Run the Container
Once the image is built, you can run the container and map the application's port to your local machine.

docker run -p 5000:5000 crypto-predictor

The application will now be running at http://localhost:5000. You can interact with the API or use the provided index.html frontend to test the predictions.

Project Structure
app.py: The main Flask application that defines the API endpoints.

models/: Contains the trained machine learning model (Randomforest_Regression_model.pkl) and the TargetEncoder.pkl for data preprocessing.

data/: Includes the raw and preprocessed data used for training.

templates/: The frontend HTML file (index.html) for interacting with the API.

requirements.txt: Lists all the Python dependencies.

Dockerfile: The instructions for building the Docker image.

.dockerignore: Specifies files and folders to be excluded from the Docker build context.

Future Enhancements
Real-time Data: Integrate with a cryptocurrency exchange API to get real-time data for predictions.

Improved Model: Explore other machine learning models or deep learning approaches (e.g., LSTMs) to improve prediction accuracy.

Container Orchestration: Deploy the application using container orchestration tools like Kubernetes.
