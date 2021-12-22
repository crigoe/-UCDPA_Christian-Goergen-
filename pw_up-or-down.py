from dax_supervised import *

new_close = input("Closing Pice: ")
new_open = input("Opening Price: ")
new_high = input("Highest Price: ")
new_low = input("Lowest Price: ")

X_new = np.array([new_close,new_open,new_high,new_low])
print(X_new)
dax_prediction = X_new.reshape(1,-1)

new_prediction = knn.predict(dax_prediction)
print(new_prediction)