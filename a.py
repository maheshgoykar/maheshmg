import requests
from datetime import datetime

def get_api_data(url):
    '''Return API data in JSON format.'''
    response = requests.get(url)
    try:
        if response.status_code == 200:
            # Extract JSON data from the response
            data = response.json()
            return data
        else:
            # for failed request
            print(f"Request failed with status code: {response.status_code}")
    except Exception as err:
        print(err)

def get_weather(api_data, date):
    ''' print weather data for input date'''
    temperatures = [str(data['main']['temp']) for data in api_data['list'] if (datetime.strptime(data['dt_txt'], "%Y-%m-%d %H:%M:%S")).strftime("%Y-%m-%d") == date ]
    if temperatures:
        print(f"Temp of the input date : {', '.join(temperatures)}")
    else:
     print("Temp data not available for the specified date.")

def get_wind_speed(api_data, date):
    ''' print wind data for input date'''
    
    wind_speed =  [str(data['wind']['speed']) for data in api_data['list'] if (datetime.strptime(data['dt_txt'], "%Y-%m-%d %H:%M:%S")).strftime("%Y-%m-%d") == date ]
    if wind_speed:
        print(f"Wind speed of the input date: {', '.join(wind_speed)}")
    else:
        print("Wind speed data not available for the specified date.")

def get_pressure(api_data, date):
    ''' print pressure data for input date'''
    
    pressure =  [str(data['main']['pressure']) for data in api_data['list'] if (datetime.strptime(data['dt_txt'], "%Y-%m-%d %H:%M:%S")).strftime("%Y-%m-%d") == date ]
    if pressure:
        print(f"Pressure of the input date: {', '.join(pressure)}")
    else:
        print("Pressure data not available for the specified date.")

def exit_function():
    ''' terminate the program '''
    
    print("Terminate")
    quit()

# url of api
url = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'
# get api data in json
api_data = get_api_data(url)

print("""Enter the option :
      1 -> Get weather
      2 -> Get Wind Speed
      3 -> Get Pressure
      0 -> Exit
      """)

# optins to function mapping dict
options = {
    1: get_weather,
    2: get_wind_speed,
    3: get_pressure,
    0: exit_function
}
terminate = True

# loop until input choice !=0
while (terminate):
    # input the choice/option
    option = int(input())
    selected_function = options.get(option, None)
    	
    if option == 0:
         selected_function()
    elif option in [1,2,3]:
        # input date
        date_input = input("Enter the date YYYY-MM-DD: ")
        # execute selected function
        selected_function(api_data, date_input)
    else:
        print("Invalid choice. Please try again.")
        
        
        