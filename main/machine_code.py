import numpy as np
import pandas
from sklearn.linear_model import LinearRegression
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_FILE_PATH = os.path.join(BASE_DIR, 'main', 'dataset.csv')

data=pandas.read_csv(CSV_FILE_PATH)
model=LinearRegression()
model.fit(data[['Total Subscribers','Total Videos']],data.TotalViews)
