# app/main.py

#Import the FastAPI class from the fastapi package
from fastapi import FastAPI

#Create an instance of the FastAPI application
#This object is the core of your API-it handles routes, middleware, and configuration
app = FastAPI()

#Define a GET endpoint for the root URL ("/")
#This is a simple health check or welcome route
@app.get("/")
def read_root():
    #This function returns a JSON response when someone accesses "/"
    return {"message": "Welcome to the AI-Powered Job Tracker API"}