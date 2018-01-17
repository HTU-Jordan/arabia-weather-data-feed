import pandas as pd
import requests
from datetime import datetime
import time

cache = "http://stations.arabiaweather.com:30000/weatherstation/updateweatherstation.php?"

def collect_request(cache):
	data_15sec = pd.read_csv("C:/Campbellsci/LoggerNet/CR1000_FifteenSec.dat", skiprows = 3)
	data_1hour = pd.read_csv("C:/Campbellsci/LoggerNet/CR1000_OneHour.dat", skiprows = 3)

	uid = "ID=********"
	pwd = "&PASSWORD=********"
	action = "&action=updateraw"
	dateutc = "&dateutc=now"
	windspeed = "&windspeed=" + str(data_15sec.iloc[0,2])
	winddir = "&winddir=" + str(data_15sec.iloc[0,3])
	solarradiation = "&solarradation=" + str(data_15sec.iloc[0,5])
	outtemp = "&outtemp=" + str(data_15sec.iloc[0,6])
	outhumi = "&outhumi=" + str(data_15sec.iloc[0,7])
	rainin = "&rainin=" + str(data_1hour.iloc[0,8])
	visibility = "&visibility=" + str(data_15sec.iloc[0,9]) 
	bar = "&relbaro=" + str(data_15sec.iloc[0,10] * 1.285)
	    
	request_string = cache + uid + pwd + action + dateutc + windspeed + winddir + solarradiation + outtemp + outhumi + rainin + visibility + bar
	return(request_string)



if __name__ == '__main__':
	starttime = time.time() 
	while True:   
		
		request_string = collect_request(cache)
		r = requests.get(request_string)
		print("-------------------------------------------------")
		print("Data was last sent on: " + str(datetime.now()))
		print("Status Code:", r.status_code)
		time.sleep(15.0 - ((time.time() - starttime) % 15.0))




