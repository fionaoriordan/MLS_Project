# MLS_Project  



GMIT Higher Diploma Data Analytics  
Machine Learning and Statistics Module 52954  
Assignment: ML Project  
Lecturer: Ian McLoughlin  
Student: Fiona O'Riordan  
Due Date: 01 January 2020  


![turbines.jpg](https://github.com/fionaoriordan/MLS_Project/blob/main/images/turbines.jpg)


## Objective  
Create a web service that uses machine learning to make predictions based on the data set power production available on Moodle. The goal is to  
produce a model that accurately predicts wind turbine power output from wind speed  values, as in the data set. The web service should respond with predicted power values based on speed values sent as HTTP requests. 

## Contents:
1. Models folder: 
* linearreg.pkl  
* polyreg.pkl  
* polyreg3.pkl  
* kerasmodel.h5  
2. Static Folder:  
* index.html  
3. .dockerignore  
4. .gitignore  
5. Dockerfile  
6. LICENSE  
7. projectmodels.ipynb  
8. README.md  
9. requirements.txt  
10. server.py  

## Overview  
This project consists of four models: Linear, Polynomial 2 Degrees, Polynomial 3 degrees and finally a Keras model.  Each of the four models predict power generated based on wind speed entered with different accuracy levels. The third model, polynomial with 3 Degrees, is a definite improvement on the the linear model and the Polynomial model with just 2 degrees. The Polynomial with 3 Degrees predictions are  closer to the actual power generated. However this model is not as accurate as the final model, Keras which is the most accurate model employed to predict power generated. This is especially true when wind speed values of 5 or less are encountered. Moreover, the keras model achieved the lowest (and best) RMSE value (see the jupyter notebook summary section)

However Keras still has some shortcomings for these low wind speeds, when wind speed is actually zero Keras does seem to overpredict ie not predict zero power generated. I am unclear about the line between overfiting occurs and inadequate values.

Finally, none of the models employed could include wind values greater than 24.5. There was limited data with wind speeds >= 24.5. But, all of the power generated values where zero for wind speeds => 24.5.  When I included these wind speed values in model training the predicted results where skewed for higher wind speeds so I decided to exclude all wind speed >= 24.5 and limit the model to predicting wind speeds of less than 24.5. This may be a major weakness in this project implementation.


## Cloning the repository  
Cloning allows you to create and use a copy of this repository on your local machine.  

In this repository.  
Click on the green button "Code". Select "Clone with HTTPS". Copy the URL.  
In your terminal on your machine navigate to your preferred directory (folder). Type git clone https://github.com/fionaoriordan/MLS_Project.git ( this is the URL you have copied).  
The repository is now installed  
Executing the repository  
In your terminal navigate to the the folder where you cloned this repository.  

## Executing this repository:  
#### Option 1. Using Docker  

- Install docker on your machine. (follow the instructions on https://docs.docker.com/get-docker/)  
- In your terminal navigate to your repository folder.  
- Execute the following commands:    
    * docker build . -t mlsprojectimage  
    * docker container ls -a (Note: this step is optional and just shows you the container you created)  
    * docker run -d -p 5000:5000 mlsprojectimage (Note: if this does not work then substitute mlsprojectimage with the container id listed in the previous step. This worked for me on a MAC )  
- In your browser navigate to http://0.0.0.0:5000/  

#### Option 2. Without Docker file  
1. In the repository directory in your terminal execute the following commands for your own particular operating system.  
- Linux terminal  
export FLASK_APP=server.py
python3 -m flask run  (I am guessing you should use Python 3.8.3  as I dont have access to LINUX I cant say for sure.)
-  Windows  
set FLASK_APP=server.py  
python -m flask run  
-  MAC
export FLASK_APP=server.py
flask run


## In the Browser
Enter a random speed wind of your choice from 0 to 24.5 and click on the desired model button or alternatively 'All Models' button. The application will predict the power generated from the wind speed entered for the particular model clicked or for all models depending on the button selected. 
  
Best Wishes, Fiona 










