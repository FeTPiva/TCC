import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping

#https://towardsdatascience.com/building-a-deep-learning-model-using-keras-1548ca149d37

#input e output
x=np.array(([0.024472049684408,0.024472049684408,0.008281573498964804, 0.3],[0,0.04040404040,0.006734006734, 0.1],[0.07290533188248095,0.04570184983677911, 0.018498367791077257, 0.4 ], [0.024472049684408,0.024472049684408,0.008281573498964804, 0.3],[0,0.04040404040,0.006734006734, 0.1],[0.07290533188248095,0.04570184983677911, 0.018498367791077257, 0.4 ]), dtype=float)
y=np.array(([1., 0.,1., 1.,0., 1.]), dtype=float)
y=to_categorical(y)
xteste=np.array(([0.08254963427377221, 0.0355276907000104496, 0.02298850574126436, 0.3]), dtype=float)

n_cols=x.shape[1]

#print(n_cols)

model = Sequential()

model.add(Dense(10, activation='relu', input_shape=(n_cols,)))
model.add(Dense(5, activation='relu'))
model.add(Dense(2, activation='softmax'))


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


early_stopping_monitor = EarlyStopping(patience=3)


model.fit(x, y, epochs=30, validation_split=0.001, callbacks=[early_stopping_monitor])


print(model.predict(xteste))
