# MLS_Project
Machine Learning and Statistics Module 52949 Project 

## Objective
In this project you must create a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to  
produce a model that accurately predicts wind turbine power output from wind speed  
values, as in the data set. You must then develop a web service that will respond with  
predicted power values based on speed values sent as HTTP requests. Your submission  
must be in the form of a git repository containing, at a minimum, the following items:  
1. Jupyter notebook that trains a model using the data set. In the notebook you  
should explain your model and give an analysis of its accuracy.  
2. Python script that runs a web service based on the model, as above.  
3. Dockerfile to build and run the web service in a container.  
4. Standard items in a git repository such as a README.  
To enhance your submission, you might consider developing and comparing more than  
one model.




Error: 

server py file : 2020-12-29 10:22:34.144085: I tensorflow/compiler/jit/xla_cpu_device.cc:41] Not creating XLA devices, tf_xla_enable_xla_devices not set
2020-12-29 10:22:34.147824: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations: AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
Solution: 
https://stackoverflow.com/a/52584016
Set environment variables before running.

Windows:

$ set TF_CPP_MIN_LOG_LEVEL=2
Linux/MacOS:

$ export TF_CPP_MIN_LOG_LEVEL=2

This worked for me.


