import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

USAhousing = pd.read_csv('Data/USA_Housing.csv')
# print(USAhousing.head())
# print(USAhousing.info())
# print(USAhousing.describe())
# print(USAhousing.columns)
# sns.pairplot(USAhousing).savefig('pairplot.png')
# sns.distplot(USAhousing['Price']) # посмотреть, как это вывести

x = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=101)

from sklearn.linear_model import LinearRegression
im = LinearRegression()
im.fit(X_train, y_train)
print(im.intercept_)
print(im.coef_)
coeff_df = pd.DataFrame(im.coef_, x.columns, columns = ['Coefficient'])
print(coeff_df)
prediction = im.predict(X_test)
print(prediction)
plt.show(plt.scatter(y_test, prediction))

from sklearn import metrics
print('MAE: ', metrics.mean_absolute_error(y_test, prediction))
