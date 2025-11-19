# Import packages
import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Load the model into memory
with open("./iris.pkl","rb") as model_pkl:
    knn = pickle.load(model_pkl)

# Test data
new_record = np.array([[1.2, 1.6, 1.8, 2.4]])
predict_result = knn.predict(new_record)

# Print result to the console
print('Predicted result for observation ' + str(new_record) + ' is: ' + str(predict_result))