from datetime import datetime, timedelta
import requests
import json


city_coords = {
    'galway': ('53.270668', '-9.056790'),
    'oslo': ('59.913868', '10.752245'),
    'london': ('51.507351', '-0.127758')
}

measurements = {
    'temperature': 'temperature_2m_max',
    'rain': 'rain_sum',
    'windspeed': 'windspeed_10m_max'
}

def weather(message):
    message = message.lower()

    if len(message) > 0:
        if len(message.split(' ')) > 1:
            city = message.split(' ')[0]
            measure = message.split(' ')[1]
        else:
            city = message
            measure = ""

        if city in city_coords.keys():
            if len(measure) > 0:
                if measure in measurements.keys():
                    date_yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
                    params = {
                        'latitude': city_coords[city][0],  # You need to update this
                        'longitude': city_coords[city][1], # ... and this
                        'start_date': date_yesterday,
                        'end_date': date_yesterday,
                        'timezone': 'GMT',
                        'daily': measurements[measure]
                    }

                    response = requests.get('https://api.open-meteo.com/v1/forecast', params=params).json()
                    return response["daily"][measurements[measure]][0]
                else:
                    return "Invalid Measurement"
            else:
                date_yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
                params = {
                    'latitude': city_coords[message][0],  # You need to update this
                    'longitude': city_coords[message][1], # ... and this
                    'start_date': date_yesterday,
                    'end_date': date_yesterday,
                    'timezone': 'GMT',
                    'daily': 'temperature_2m_max'
                }

                response = requests.get('https://api.open-meteo.com/v1/forecast', params=params).json()
                return response["daily"]["temperature_2m_max"][0]
            
        else:
            return "Invalid City!"
    else:
        # For challenge 3.1, you'll need to get the longitude and latitude for Galway
        # and put them in the params below.

        date_yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        daily_params = ['temperature_2m_max']
        params = {
            'latitude': 53.270668,  # You need to update this
            'longitude': -9.056790, # ... and this
            'start_date': date_yesterday,
            'end_date': date_yesterday,
            'timezone': 'GMT',
            'daily': daily_params
        }

        response = requests.get('https://api.open-meteo.com/v1/forecast', params=params).json()
        return response["daily"]["temperature_2m_max"][0]


