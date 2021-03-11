import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import torch
import torch.nn as nn
import torch.nn.functional as F


data = pd.read_csv('./data/clean_data.csv')

data.head()

classes = list(data['genre'].unique())
#create dictionary of classes and the numerical number associated with each class.
target_dict = {classes[i]:i for i in range(len(classes))}

#change target from strings to ints.

data['genre'] = data['genre'].replace(target_dict)
X = data.drop(columns=['id','genre'])
y = np.array(data['genre'])

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)

sc = StandardScaler()

X_train_sc = sc.fit_transform(X_train)
X_test_sc = sc.transform(X_test)

X_train_t = torch.tensor(X_train_sc).float()
y_train_t = torch.tensor(y_train).long()

X_test_t = torch.tensor(X_test_sc).float()
y_test_t = torch.tensor(y_test).long()

class MultiClassModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.h1 = nn.Linear(25, 32)
        self.h2 = nn.Linear(32, 64)
        self.h3 = nn.Linear(64, 64)
        self.h4 = nn.Linear(64, 128)
        self.h5 = nn.Linear(128, 128)
        #self.h6 = nn.Linear(128, 128)
        self.out = nn.Linear(128, 15)

    def forward(self, X):
        X = F.relu(self.h1(X))
        X = F.relu(self.h2(X))
        X = F.relu(self.h3(X))
        X = F.relu(self.h4(X))
        X = F.relu(self.h5(X))
        #X = F.relu(self.h6(X))
        return self.out(X)


model = MultiClassModel()

loss_fn = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=.001)

#%%
train_loss = []
testing_loss = []
train_accuracy = []
test_accuracy = []
batch_size = 512
training_size = X.shape[0]
for epoch in range(150):
    with torch.no_grad():
        test_pred = model(X_test_t)
        test_loss = loss_fn(test_pred,y_test_t)
        testing_loss.append(test_loss.item())
        train_pred = model(X_train_t)
        loss = loss_fn(train_pred, y_train_t)
        train_loss.append(loss.item())
        train_accuracy.append((train_pred.argmax(axis=1) == y_train_t).float().mean())
        test_accuracy.append((test_pred.argmax(axis=1) == y_test_t).float().mean())
    for batch_idx in range(0, training_size, batch_size):
        # zero out the optimizer's gradients
        optimizer.zero_grad()

        # Create X_batch and y_batch
        X_batch = X_train_t[batch_idx:batch_idx + batch_size]
        y_batch = y_train_t[batch_idx:batch_idx + batch_size]

        # get predictions and loss
        pred = model(X_batch)

        loss = loss_fn(pred, y_batch)
        # back propagate
        loss.backward()

        # step
        optimizer.step()


plt.plot(train_loss, color='red')
plt.plot(testing_loss, color= 'blue')
plt.show()


plt.plot(train_accuracy, color= 'purple')
plt.plot(test_accuracy, color= 'cyan')
plt.show()