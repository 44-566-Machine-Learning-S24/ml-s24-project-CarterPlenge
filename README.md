[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/7lKBcjfN)
# 44-566 machine-learning project
Repo for all project documents
Project Change.
I changed my project from predicting Tesla accidents with weather to predicting crime rates with weather. I did this because I was struggling to find sufficient data for the teslas. 

In the initial_exploration notebook, I found correlations between the weather attributes but there didnt appear to be any visible correlation between weather conditions and crime rate. I only found a correlation after I started using linear regression. 

I managed to get the linear regression model down to a ~.09 mean squared error value. compared to the unpredictable model that could get a ~.22 mean squared error value. So while i didnt find any strong correlations at first because the model was able to predict crime rates with relative accuracy I believe there is a correlation between the weather conditions of a day and the number of crimes committed that day. 

This model takes in weather conditions and tries to predict the number of crimes that will be committed that day. I decided to make this model because i thought that differences in weather conditions might affect people's minds and how they act. 

When creating the classifications notebook I was unable to get any good models that predicted the number of crimes that would happen with given weather conditions. I was able to make a model that predicted the overall weather with weather conditions. For my models that predicted weather conditions, I found decision trees to be better than SVM due to some categories having low sample sizes. 
