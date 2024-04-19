## What is this md?
This used to be my read-me before the final submission. This details my initial exploration throughout the semester as well as project changes and adjustments. I figured I would save this for documentation. 


### Project Change.
I changed my project from predicting Tesla accidents with weather to predicting crime rates with weather. I did this because I was struggling to find sufficient data for the teslas. 

### 4/3/2024 Project adjusted: (i emailed you about this on 3/31/2024)
I adjusted my previous notebooks to remove the crime rates and predict the overall weather conditions given the precipitation, temp_max, temp_min, and wind of a given day. I did this because I started to believe that the data I was using to predict crime rate had no correlation. I was unable to produce a model using any of the algorithms or features to achieve prediction powers better than a model that predicted the same answer for everything. 
During this change, I tried to make minimal adjustments (just replacing variables) to my original code and commented out any large sections where I replaced more than just variables so that you could see my original work. In addition to this, I updated the markdown cells to match the new data. 

## Initial thoughts and results when making the notebooks
All of these were wrote directly after i completed the given project milestone. Some information might have change or be wrong. 
### initial_exploration
In the initial_exploration notebook, I found correlations between the overall weather condition and temp_max, precipitation, and wind. These three attributes had a correlation around 0.2 each. temp_min was also a feature but only had a correlation of .04 so was left out. 

I managed to get the linear regression model down to a Mean Squared Error value of 0.68. This is not that great however with the data I have and what I am trying to predict, this is not unexpected due to the predicted feature not being an actual numeric value, but a state of weather ({'drizzle': 0, 'rain': 1, 'sun': 2, 'snow': 3, 'fog': 4}).

### Classifications
When creating the classifications notebook I was able to reach accuracies and f1 scores of around .75 using the decision tree model. Linear, sigmoid, and rbf all produced very similar values around .75 as well. I was unable to get anything out of clusters


### Milestone 3
In my final analysis, I added in a few models that performed similarly to privous models. The new models I made include a k means cluster, PCA,  and an adam neural net. The k means clusters did not perform well as my data does not appear to group well. The neural net achieved my highest accuracy of .84 and was able to regularly predict 3 types of days, sunny, rainy, and snowy, more than any previous models were able to do.
There were still two types of days that ended up unpredicted, foggy, and drizzly. I think this is more of an issue with the data because what differentiates rain from drizzle and fog often has to do with the differences between ground temp and wind. Since the model has no real way of knowing ground temp it might make it impossible for a model to predict fog. As for anomalous data, there are a few records in the set with abnormally high winds and precipitation that could affect the model's ability to predict. 
