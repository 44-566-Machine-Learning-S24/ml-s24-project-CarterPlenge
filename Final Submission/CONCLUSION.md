# Conclusion
### Model performance
A majority of the models I made struggled with the distribution of data often failing to predict fog, snow, and drizzle. The most effective model I was able to create was a neural net with scores around .85. However, if you drop the features for fog and drizzle, the performance improved to scores around .95. 

### Feature Importance
The most important features in my data were precipitation and temp_max. I also believe temp_min to be important. While a majority of models' performance didn't change with temp_min. It was the feature that allowed neural nets to predict snow days. 

### Challenges encountered
The biggest challenge I faced was the models not even trying to predict fog, snow, and drizzle. This is largely due to the imbalanced dataset.

### Future Directions
For future directions, I think it would be beneficial to look for more ways to differentiate fog and drizzle. 



Portal back to [ReadMe](https://github.com/44-566-Machine-Learning-S24/ml-s24-project-CarterPlenge/tree/master?tab=readme-ov-file#conclusion)
