from django.shortcuts import render
import numpy as np
import pandas
from sklearn.linear_model import LinearRegression
import os


def predictor(request):

  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  CSV_FILE_PATH = os.path.join(BASE_DIR, 'main', 'dataset.csv')

  data=pandas.read_csv(CSV_FILE_PATH)
  model=LinearRegression()
  model.fit(data[['Total Subscribers','Total Videos']],data.TotalViews)

  subscribers=(request.POST.get('subscribers'))
  videos=(request.POST.get('videos'))
  views=0
  income=0

  if subscribers!=None and videos!=None:
    views=model.predict([[float(subscribers),float(videos)]])
    income=(views/1000)*300
    views = round(views[0], 2)
    income = round(income[0], 2)

  else:
     views=0
     income=0

  return render(request, 'main/home.html',{'views':views,'income':income})