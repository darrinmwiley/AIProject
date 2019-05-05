import csv
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, mutual_info_classif
import urllib
import json

def fetch(i):
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches1.json"
    urllib.request.urlretrieve(url,'matches1.json')
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches2.json"
    urllib.request.urlretrieve(url,'matches2.json')
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches3.json"
    urllib.request.urlretrieve(url,'matches3.json')
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches4.json"
    urllib.request.urlretrieve(url,'matches4.json')
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches5.json"
    urllib.request.urlretrieve(url,'matches5.json')
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches6.json"
    urllib.request.urlretrieve(url,'matches6.json')
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches7.json"
    urllib.request.urlretrieve(url,'matches7.json')
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches8.json"
    urllib.request.urlretrieve(url,'matches8.json')
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches9.json"
    urllib.request.urlretrieve(url,'matches9.json')
    url = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches10.json"
    urllib.request.urlretrieve(url,'matches10.json')
