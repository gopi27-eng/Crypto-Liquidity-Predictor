# Use an official Python runtime as a parent image
# We use a lightweight version for a smaller container size
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
# We do this step first to leverage Docker's build cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
# This includes app.py and the models directory
COPY app.py .
COPY models/ ./models/
COPY data/ ./data/

# Expose the port on which the Flask app will run
EXPOSE 5000

# Define the command to run the application
# This is the same command you use to run it locally
CMD ["python", "app.py"]
