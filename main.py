from fastapi import FastAPI
import uvicorn
from utils import *
from flex import *

app = FastAPI()

@app.get("/")
async def index():
    return {"message" : "Hello World"}

@app.get("/return")
async def retval(param:str=None):
	return{"msg":param}

@app.get("/api/closeRes")
async def closeRes(lat:float,lng:float,num_res:int):
	data = read_gsheet()
	dist = find_dist((lat,lng),data[['lat','lng']].values)
	min_arg = np.argsort(dist)[:num_res]
	data_out = data.iloc[min_arg]
	data_out['dist'] = dist[min_arg]

	return list(data_out.reset_index().drop(columns=['Location_query','lat','lng']).to_dict(orient='index').values())

@app.get("/api/closeRes10")
async def closeRes10(p_latitude:float,p_longitude:float):
	num_res=10
	data = read_gsheet()
	dist = find_dist((p_latitude,p_longitude),data[['lat','lng']].values)
	min_arg = np.argsort(dist)[:num_res]
	data_out = data.iloc[min_arg]
	data_out['dist'] = dist[min_arg]

	return data_out.reset_index().drop(columns=['Location_query','lat','lng']).to_dict(orient='index')

@app.get("/api/closeRes10_line_location")
async def closeRes10_bn(p_latitude:str,p_longitude:str):
	num_res=10
	lat = locate_cut(p_latitude)
	lng = locate_cut(p_longitude)
	data = read_gsheet()
	dist = find_dist((lat,lng),data[['lat','lng']].values)
	min_arg = np.argsort(dist)[:num_res]
	data_out = data.iloc[min_arg]
	data_out['dist'] = dist[min_arg]

	return data_out.reset_index().drop(columns=['Location_query','lat','lng']).to_dict(orient='index')

@app.get("/api/getRes")
async def getRes(place:str,food_cate:str,num:int = 3):
	"""
	Get data by string place
	- **place** Place of location ex.สยามพารากอน
	- **food_cate** Food category ex.อาหารญี่ปุ่น, อาหารเจ
	- **num** Number of restaurang to return (int)
	"""
	lat,lng = place2location(place)
	data = read_gsheet()
	data = data[(data['categories_1']==food_cate) | (data['categories_2']==food_cate) | (data['categories_3']==food_cate)]
	dist = find_dist((lat,lng),data[['lat','lng']].values)
	min_arg = np.argsort(dist)[:num]
	data_out = data.iloc[min_arg]
	data_out['dist'] = dist[min_arg]
	return data_out.reset_index().drop(columns=['Location_query']).to_dict(orient='index')

@app.get("/api/flex")
async def call_flex():
	return get_flex()

if __name__ == "__main__" :
    uvicorn.run("main:app",host="0.0.0.0")
