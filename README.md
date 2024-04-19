[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/7lKBcjfN)
# 44-566 machine-learning project
Repo for all project documents
Project Change.
I changed my project from predicting Tesla accidents with weather to predicting crime rates with weather. I did this because I was struggling to find sufficient data for the teslas. 

4/3/2024 Project adjusted: (i emailed you about this on 3/31/2024)
I adjusted my previous notebooks to remove the crime rates and predict the overall weather conditions given the precipitation, temp_max, temp_min, and wind of a given day. I did this because I started to believe that the data I was using to predict crime rate had no correlation. I was unable to produce a model using any of the algorithms or features to achieve prediction powers better than a model that predicted the same answer for everything. 
During this change, I tried to make minimal adjustments (just replacing variables) to my original code and commented out any large sections where I replaced more than just variables so that you could see my original work. In addition to this, I updated the markdown cells to match the new data. 

In the initial_exploration notebook, I found correlations between the overall weather condition and temp_max, precipitation, and wind. These three attributes had a correlation around 0.2 each. temp_min was also a feature but only had a correlation of .04 so was left out. 

I managed to get the linear regression model down to a Mean Squared Error value of 0.68. This is not that great however with the data I have and what I am trying to predict, this is not unexpected due to the predicted feature not being an actual numeric value, but a state of weather ({'drizzle': 0, 'rain': 1, 'sun': 2, 'snow': 3, 'fog': 4}).

When creating the classifications notebook I was able to reach accuracies and f1 scores of around .75 using the decision tree model. Linear, sigmoid, and rbf all produced very similar values around .75 as well.

In my final analysis, i added in a few models that performed similarly to privous models. The new models i made include a k means cluster, PCA,  and a adam neural net. The k means clusters did not preform well as my data does not appear to group well. The PCA achived the highest accuracy with .788 however still struggled to predict features besides sunny and rainny as did privous models. The nueural net achived a slighly lower accuracy of .84 but was able to regularly predict 3 types of days, sunny rainny and snowy, more than any previous models were able to do. There were still two types of days that ended up unpredicted, foggy and drizzley. I think this is more of an issue with the data because what differentiates rain from drizzle and fog often has to do with the differences between ground temp and wind. Since the model has no real way of knowing ground temp it might make it impossible for a model to predict fog. As for anomalous data, there are a few records in the set with abnormally high winds and precipitation that could possibly affect the model's ability to predict. 

