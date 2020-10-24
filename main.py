from fastapi import FastAPI
import uvicorn
from utils import *
#from flex import *
from flex2 import *

app = FastAPI()

@app.get("/")
async def index():
    return {"message" : "Hello World"}

@app.get("/return")
async def retval(param:str=None):
	return{"msg":param}

@app.get("/api/getRes")
async def getRes(place:str,food_cate:str,num:int = 9,customer_id:str=None):
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
	if customer_id is not None :
		user_db_update(customer_id,lat,lng,food_cate)
	return get_flex(data_out.reset_index().to_dict(orient='index'),num)


@app.get('/api/getedlocation')
async def getedLocation(p_latitude: str, p_longitude: str):
    headers = {'Response-Type': 'intent'}
    return_json = {
        'intent': "in_getedlocation"
    }
    print(p_longitude)
    return JSONResponse(content=return_json, headers=headers)


@app.get('/api/getResGPS')
async def getResByShare(p_latitude: str, p_longitude: str, food_cate: str, num: int = 9, customer_id:str=None):
    lat = float(p_latitude)
    lng = float(p_longitude)
    print(type(lat))
    print(type(lng))
    data = read_gsheet()
    food_cate = food_cate
    data = data[(data['categories_1'] == food_cate) | (
        data['categories_2'] == food_cate) | (data['categories_3'] == food_cate)]
    dist = find_dist((lat, lng), data[['lat', 'lng']].values)
    min_arg = np.argsort(dist)[:num]
    data_out = data.iloc[min_arg]
    data_out['dist'] = dist[min_arg]
    if customer_id is not None :
        user_db_update(customer_id,lat,lng,food_cate)
    return get_flex(data_out.reset_index().to_dict(orient='index'), num)


@app.get("/api/getRes_location")
def getRes_location(p_latitude:float,p_longitude,food_cate:str,num:int = 9,customer_id:str=None):
	return getRes_location_fn(p_latitude=p_latitude,p_longitude=p_longitude,
						food_cate=food_cate,num=num,customer_id=customer_id)

def getRes_location_fn(p_latitude:float,p_longitude,food_cate:str,num:int = 9,customer_id:str=None):
	lat,lng = p_latitude,p_longitude
	data = read_gsheet()
	data = data[(data['categories_1']==food_cate) | (data['categories_2']==food_cate) | (data['categories_3']==food_cate)]
	dist = find_dist((lat,lng),data[['lat','lng']].values)
	min_arg = np.argsort(dist)[:num]
	data_out = data.iloc[min_arg]
	data_out['dist'] = dist[min_arg]
	if customer_id is not None :
		user_db_update(customer_id,lat,lng,food_cate)
	return get_flex(data_out.reset_index().to_dict(orient='index'),num)

@app.get("/api/getUser_res")
async def getUser_random(customer_id:str):
	num = 9
	read_data = user_db_res(customer_id)
	data = read_gsheet()
	if read_data is None :
		data = data.sample(frac=1)
		return get_flex(data.reset_index().to_dict(orient='index'),num)
	lat,lng,food_cate = read_data[0]
	dist = find_dist((lat,lng),data[['lat','lng']].values)
	min_arg = np.argsort(dist)[:30]
	data_out = data.iloc[min_arg].sample(frac=1).iloc[:num]
	#data_out['dist'] = dist[min_arg]
	return get_flex(data_out.reset_index().to_dict(orient='index'),num)


@app.get("/api/flex")
async def call_flex():
	return get_flex_test()

if __name__ == "__main__" :
    uvicorn.run("main:app",host="0.0.0.0")
