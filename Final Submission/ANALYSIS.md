# Analysis
### Models Used
I used several models throughout this project but the most effective ones were neuralnets. Decision trees and SVMs performed relatively similarly. The features I used with these models were temp_max, precipitation, and wind. I did some tests with my data set with and without the temp_min feature and found that it had a minimal impact on most models so I left it out on them. Most of these models would only predict sun or rain for days as the distribution was skewed. I tried to reduce the number of cases for sun and rain to see if I could get it to predict something else but this did not work as it would either still predict sun or rain, or it wouldn't have enough data to predict anything.
I linked the notebook where the models are located to the name of the model. There are more notes about them and thoughts about them in there but they aren't very pretty and the core parts are all here. 

For decision trees, validation scores were around .75

SVM-linear, sigmoid, and rbf validation scores were around .70

[Notebook](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge/blob/master/classification.ipynb) containing them

Along with these, I tried Nural nets. However, I tried the temp_min feature again and found that it allowed the neural net to detect days when it snowed. However, even the neural net wouldn't predict fog, or drizzle.

[Neural Net](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge/blob/master/Milestone%203.ipynb) - scores around .85

After seeing all of my models fail to predict fog or drizzle I wanted to know what would happen if I just dropped them from the data set. The results were as follows

[Neural Net](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge/blob/master/Milestone%203.ipynb) - scores around .95

With this I knew my model was doing a fair job predicting sun, rain, and snow so I tried to create features that would help it predict fog and drizzle, the previous day's temperature, and tried it out in a [notebook](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge/blob/master/Final%20Submission/Milestone%203%20revised.ipynb) (it's messy as it is a modified version of milestone 3 and the comparison was done by having both, this notebook and notebook 3, open at the same time) but the results were nothing of note and I haven't managed to predict fog or drizzle yet. I think this is mainly due to the lack of fog (5), drizzle (53), and snow (23) instances. While I did make a model that predicted snow, drizzle would be difficult to differentiate between the two largest categories, sun and rain, and fog only has 5 instances. 

### Future Improvements
Something that I think could be improved upon is detecting drizzle. There are 53 instances of it but it is difficult to separate from sun and rain. It might be possible to apply some sort of transformation that would separate them more. 

Portal back to [ReadMe](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge?tab=readme-ov-file#analysis)
