# DATA
## What I did with the data
The target variable for this project was 'weather'. This was a categorical feature that contained the given weather that day. Since this catagorie was non numerical, I applied a mapping to it to convert them all into integers so the computer could process it. 
In additon to that I also added the two variables prev_temp_max and prev_temp_min. I added these features because I thought they would be useful when i came to predicting fog, as fog is often formed by the tempeture difference between the ground and air combined with little to no wind. 

## Describing the data
My data had a very uneven distribution of data points with almost all of the records either being rainy or drizzly as can be seen in the histogram below. 

![image](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge/assets/124809586/419f41fc-f224-4b57-880c-33bebc1d56a7)

above image can be found in [[this notebook](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge/blob/master/initial_exploration.ipynb)]

When clustering the data, the algorithm seemed to split the data set in half based on temp Max, then include all of the data points with high precipitation in a different cluster.

![image](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge/assets/124809586/2f324a73-70b5-481d-adb0-cf239f16d3bd)

![image](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge/assets/124809586/90e0c185-2e62-41df-9fa6-3ec2b28682c5)

