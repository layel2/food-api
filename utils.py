import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import geopy.distance as ps
from geopy.geocoders import Nominatim
import gspread

def read_gsheet():
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(credentials)

    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1amqQT5t6WK1pu7FCxn-Gf5cwGxagqOK17TNHVMHYqtY")
    worksheet = sheet.get_worksheet(0)
    results = worksheet.get_all_records()
    
    return pd.DataFrame(results)


def find_dist(src,des_list):
    dist = []
    for des in des_list :
        dist.append(ps.distance(src, des).km)
    return np.array(dist)

def locate_cut(locastr):
    return float(locastr.split('=')[1].split(')')[0])

def place2location(place:str):
    geolocator = Nominatim(user_agent="app1")
    return geolocator.geocode(place)[1]