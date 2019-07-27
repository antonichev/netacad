import urllib.parse
import requests

api_key = 'Put your Consumer Key here'
URL = 'http://www.mapquestapi.com/directions/v2/route'

start_point = input('Enter Starting Location ("quit" to finish): ')

if (start_point != 'quit'):
    destination_point = input('Enter Destination: ')

    PARAMS = {'key':api_key, 'from':start_point, 'to':destination_point, 'unit':'k'}

    response = requests.get(url = URL, params = PARAMS)

    data = response.json()

    status_code = data['info']['statuscode']

    if (status_code == 0):
        route = data['route']
        maneuvers = route['legs'][0]['maneuvers']
        separator = '\n' + '=' * 50

        print('\n')
        print('API Status: 0 = A successful route call')
        print('Directions from ' + start_point + ' to ' + destination_point)
        print('\n')

        print('Trip Duration: ' + route['formattedTime'])
        print('Kilometers: ' + str(route['distance']))
        print('Fuel Used (Ltr): ' + str(route['fuelUsed']))

        print(separator)

        for item in maneuvers:
            print(item['narrative'] + '(' + str(item['distance']) + ' km)')

        print(separator)
    else:
        error_message = data['info']['messages'][0]
        print('ERROR! API status: ' + str(status_code) + ' = ' + error_message)