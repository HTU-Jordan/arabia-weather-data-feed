# Arabia Weather Data Feed

## Station Link on Arabia Weather
<http://stations.arabiaweather.com/station/mgzmi788>

## Sending the Data  
Open `send_data.py` to see the code that sends data every 15 seconds to ArabiaWeather.  
Username and password have been replaced with ********.  

It does the following:  
1. Read the data from file.  
2. Construct a __string__ that contains the desired data.  
3. __SEND__ the string as an __HTTP GET REQUEST__.  
