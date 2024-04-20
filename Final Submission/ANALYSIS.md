# Analysis
### Models Used
I used a number of models throughout this project but the most effective ones were neuralnets. Decision trees and SVMs preformed relitively similarly. The features I used with these models were temp_max, precipitaion, and wind. I did some test with my data set with and without the temp_min feature and found that it had a minimal impact on most models so i left it out on them. Most of these models would only predict sun or rain for days as the distribution was skewed. I tryed to reduce the number of cases for sun and rain to see if i could get it to predict somthing else but this did not work as it would either still predict sun or rain, or it wouldnt have enough data to predict anything. 

For decision trees, validation scores were around .75
SVM - linear, sigmoid, and rbf validation scores were around .70
Notebook containing them

Along with these I tryed Nural nets. However i tried temp_min feature agian and found that it allowed the neural net to detect days when it snowed. However, even the neural net wouldnt predict fog, or drizzle.

Neural Net - scores around .85

After seeing all of my models fail to predict fog or drizzle i wanted to know what would happen if I just dropped them from the data set. The results were as follows

Neural Net - scores around .95

With this i knew my model was doing a fair job predicting sun, rain, and snow so I tried to create features that would help it predict fog and drizzle, the previous days tempreture, and tried it out in a notebook (its a bit messy as it is a modifyed version of milestone 3) but the results were nothing of note and I haven't managed to predict fog or drizzle yet. 

I think one of the limitations to my results was the lack of fog (5), drizzle (53), and snow (23) instances.

Portal back to [ReadMe](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge?tab=readme-ov-file#analysis)
