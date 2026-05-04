import numpy as np
data = np.random.randn(1000)
print(data.mean(), data.std())
print(%timeit np.random.randn(10000))
%%time
model.fit(X_train, y_train, epochs=10)
print(%matplotlib inline)
