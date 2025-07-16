#Dockerfile is a set of instructions for creating an image that can run your application. For Python + FastAPI we need a base image
#(lightweight but has Python)
#Install dependencies (from requirements.txt)
#Copy our application code into the container
#Define the startup command (uvicorn app.main:app --reload)

#We copy requirements.txt first because Docker builds layers from top to bottom and caches each layer. 
#If requirements.txt doesn't change, Docker reuses the cached layer (so it doesn't reinstall dependencies everytime you change your code)
#If we copied the whole app first, any code change would invalidate the cache, forcing a reinstall of all dependencies and leads to slow builds. 

#Use a slim Python base image for smaller size
FROM python:3.11-slim

#Set working directory inside the container
WORKDIR /app

#Copy requirements.txt first for caching
COPY requirements.txt .

#Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code 
COPY . .

#Command to run FastAPI using Uvicorn 0.0.0.0 means Listen on all available network interfaces inside the container. 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

