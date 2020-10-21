import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import geopy.distance as ps
from geopy.geocoders import Nominatim
import gspread

def read_gsheet():
    worksheet = get_gsheet("https://docs.google.com/spreadsheets/d/1amqQT5t6WK1pu7FCxn-Gf5cwGxagqOK17TNHVMHYqtY")
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


def user_db_update(customer_id,lat,lng,food_cate) :
    worksheet = get_gsheet("https://docs.google.com/spreadsheets/d/1QzLXE_VCjXebBCBQX-scbeA9qIUaSmTkEsEwZI9Oiao")
    results = worksheet.get_all_records()
    df = pd.DataFrame(results)
    user_check = df.where(df['uid'] == str(customer_id)).dropna()
    if len(user_check) == 1 :
        cellRow = user_check.index.values[0] + 2
        update_row = 'B'+str(cellRow)+':D'+str(cellRow)
        worksheet.update(update_row,[[lat,lng,food_cate]])

    else :
        cellRow = len(df) + 2
        update_row = 'A'+str(cellRow)+':D'+str(cellRow)
        worksheet.update(update_row,[[customer_id,lat,lng,food_cate]])

def user_db_res(customer_id):
    worksheet = get_gsheet("https://docs.google.com/spreadsheets/d/1QzLXE_VCjXebBCBQX-scbeA9qIUaSmTkEsEwZI9Oiao")
    results = worksheet.get_all_records()
    df = pd.DataFrame(results)
    user_check = df.where(df['uid'] == str(customer_id)).dropna()
    if len(user_check) == 1 :
        return user_check[['lat','lng','food_cate']].values
    else :
        return None
    

def get_gsheet(url):
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_url(url)
    worksheet = sheet.get_worksheet(0)
    return worksheet