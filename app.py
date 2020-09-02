import uuid
import time
import requests
import urllib.parse as ur
import webbrowser
from hashlib import sha1
import hmac
import base64
import xmltodict
import json
from flask import Flask, request


# Class to store info about trips
class Trip:
    id = ''
    relative_url = ''
    start_date = ''
    end_date = ''
    trip_name = ''
    address = ''
    city = ''
    state = ''
    country = ''
    latitude = ''
    longitude = ''

    def __init__(self, filename):
        self.id = Trip.get_data(self, 'one_trip_info', 'id')
        self.relative_url = Trip.get_data(self, filename=filename, object='relative_url')
        self.start_date = Trip.get_data(self, filename=filename, object='start_date')
        self.end_date = Trip.get_data(self, filename=filename, object='end_date')
        self.trip_name = Trip.get_data(self, filename=filename, object='display_name')
        self.address = Trip.get_location(self, filename=filename, object='address')
        self.city = Trip.get_location(self, filename=filename, object='city')
        self.state = Trip.get_location(self, filename=filename, object='state')
        self.country = Trip.get_location(self, filename=filename, object='country')
        self.latitude = str(Trip.get_location(self, filename=filename, object='latitude'))
        self.longitude = str(Trip.get_location(self, filename=filename, object='longitude'))

    # method to get data
    def get_data(self, filename, object):
        with open(str(filename) + '.json', 'r', encoding='utf-8') as jsonData:  # открываем файл на чтение
            dictData = json.load(jsonData)  # загружаем из файла данные в словарь data

        data = dictData["Response"]["Trip"][str(object)]
        return data

    # method to get location data
    def get_location(self, filename, object):
        with open(str(filename) + '.json', 'r', encoding='utf-8') as jsonData:  # открываем файл на чтение
            dictData = json.load(jsonData)  # загружаем из файла данные в словарь data

        data = dictData["Response"]["Trip"]["PrimaryLocationAddress"][str(object)]
        return data

    def toString(self):
        return ('Id: ' + self.id +
                '\nRelative_url: ' + self.relative_url +
                '\nStart date: ' + self.start_date +
                '\nEnd date: ' + self.end_date +
                '\nTrip name: ' + self.trip_name +
                '\nAddress: ' + self.address +
                '\nCity: ' + self.city +
                '\nState: ' + self.state +
                '\nCountry: ' + self.country +
                '\nLatitude: ' + self.latitude +
                '\nLongitude: ' + self.longitude)


# Class to store info about hotels
class Hotel:
    id = ''
    trip_id = ''
    is_client_travaler = ''
    relative_url = ''
    display_name = ''
    supplier_conf_num = ''
    supplier_name = ''
    is_purchased = ''
    is_tripit_booking = ''
    number_guests = ''
    number_rooms = ''
    start_date = ''
    start_time = ''
    start_timezone = ''
    start_uts_offset = ''
    end_date = ''
    end_time = ''
    end_timezone = ''
    end_uts_offset = ''
    adress = ''
    guest_name = ''
    guest_tiket_num = ''

    def __init__(self, filename):
        self.id = Hotel.get_data(self, filename, 'id')
        self.trip_id = Hotel.get_data(self, filename, 'trip_id')
        self.is_client_travaler = Hotel.get_data(self, filename, 'is_client_traveler')
        self.display_name = Hotel.get_data(self, filename, 'display_name')
        self.supplier_conf_num = Hotel.get_data(self, filename, 'supplier_conf_num')
        self.supplier_name = Hotel.get_data(self, filename, 'supplier_name')
        self.is_purchased = Hotel.get_data(self, filename, 'is_purchased')
        self.is_tripit_booking = Hotel.get_data(self, filename, 'is_tripit_booking')
        self.number_guests = Hotel.get_data(self, filename, 'number_guests')
        self.number_rooms = Hotel.get_data(self, filename, 'number_rooms')
        self.start_date = Hotel.get_more_data(self, filename, "StartDateTime", "date")
        self.start_time = Hotel.get_more_data(self, filename, "StartDateTime", "time")
        self.start_timezone = Hotel.get_more_data(self, filename, "StartDateTime", "timezone")
        self.start_uts_offset = Hotel.get_more_data(self, filename, "StartDateTime", "utc_offset")
        self.end_date = Hotel.get_more_data(self, filename, "EndDateTime", "date")
        self.end_time = Hotel.get_more_data(self, filename, "EndDateTime", "time")
        self.end_timezone = Hotel.get_more_data(self, filename, "EndDateTime", "timezone")
        self.end_uts_offset = Hotel.get_more_data(self, filename, "EndDateTime", "utc_offset")
        self.adress = Hotel.get_more_data(self, filename, "Address", "address")
        self.guest_name = Hotel.get_more_data(self, filename, "Guest", "first_name")
        self.guest_tiket_num = Hotel.get_more_data(self, filename, "Guest", "ticket_num")

    # method to get data
    def get_data(self, filename, object):
        with open(str(filename) + '.json', 'r', encoding='utf-8') as jsonData:  # открываем файл на чтение
            dictData = json.load(jsonData)  # загружаем из файла данные в словарь data

        data = dictData["Response"]["LodgingObject"][str(object)]
        return data

    # method to get more data
    def get_more_data(self, filename, object1, object2):
        with open(str(filename) + '.json', 'r', encoding='utf-8') as jsonData:  # открываем файл на чтение
            dictData = json.load(jsonData)  # загружаем из файла данные в словарь data

        data = dictData["Response"]["LodgingObject"][object1][object2]
        return data

    def toString(self):
        return ('Id: ' + self.id +
                '\nRelative_url: ' + self.relative_url +
                '\nStart date: ' + self.start_date +
                '\nEnd date: ' + self.end_date +
                '\nIs_client_travaler: ' + self.is_client_travaler +
                '\nDisplay_name: ' + self.display_name +
                '\nUpplier_conf_num: ' + self.supplier_conf_num +
                '\nSupplier_name: ' + self.supplier_name +
                '\nIs_purchased: ' + self.is_purchased +
                '\nIs_tripit_booking: ' + self.is_tripit_booking +
                '\nNumber_guests: ' + self.number_guests +
                '\nNumber_rooms: ' + self.number_rooms +
                '\nStart_date: ' + self.start_date +
                '\nStart_time: ' + self.start_time +
                '\nStart_timezone: ' + self.start_timezone +
                '\nStart_uts_offset: ' + self.start_uts_offset +
                '\nEnd_date: ' + self.end_date +
                '\nEnd_time: ' + self.end_time +
                '\nEnd_timezone: ' + self.end_timezone +
                '\nEnd_uts_offset: ' + self.end_uts_offset +
                '\nAdress: ' + self.adress +
                '\nGuest_name: ' + self.guest_name +
                '\nGuest_tiket_num: ' + self.guest_tiket_num
                )


# just to keep in memory
class Result:
    result = ' '


# class to set up a server preferences
class UserData:
    callback_url = ''
    consumer_key = ''
    consumer_secret = b''

    def __init__(self, url, key, secret):
        self.callback_url = url
        self.consumer_key = key
        self.consumer_secret = bytes(secret, 'utf-8')


app = Flask(__name__)

"""
JUST FOR TEST, MUST BE REPLACED WITH VALID SECRET KEY AND URL 
"""
user_data = UserData(url='http://localhost:5000/callback', key='863459f1d1c128bc5b3f0406b869783a709325d4',
                     secret='e67d341d8566155a8459d86ad9f82fba37a5dbd2')

# First authentication
url = 'https://api.tripit.com/oauth/request_token'

# oauth_signature
"""
Нам необходимо выполнять HMAC-SHA1 (или RSA-SHA1) с ключем, который формируется так: 
urlencode("<oauth_consumer_secret>&<oauth_token_secret>") — 
(на данном этапе oauth_token_secret еще не получен, поэтому он будет пустым) 
и базовой строкой, которая составляется следующим образом: 
"<метод запроса>&<urlencode(адрес запроса)>&<urlencode(key_sort(параметры запроса))>"
"""
params = {
    'oauth_consumer_key': str(user_data.consumer_key),
    'oauth_nonce': str(uuid.uuid4()),
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_timestamp': str(int(time.time())),
    'oauth_version': '1.0',
}

token_secret = b''

encoded_params = '&'.join(['%s=%s' % (item[0], item[1]) for item in sorted(params.items())])

oauth_request_base = ('POST' + '&' + ur.quote_plus(url) + '&' + ur.quote_plus(encoded_params)).encode('utf-8')
oauth_signature = base64.b64encode(
    hmac.new(user_data.consumer_secret + b'&' + token_secret, oauth_request_base, sha1).digest())

params['oauth_signature'] = oauth_signature

oauth_header = 'OAuth ' + ', '.join(
    ['%s="%s"' % (item[0], ur.quote_plus(item[1])) for item in sorted(params.items())])

Result.result = requests.post(url, headers={'Authorization': oauth_header}).text

urlForAuth = 'https://www.tripit.com/oauth/authorize?' + str(
    Result.result.split('&')[0]) + '&oauth_callback=' + str(user_data.callback_url)
# Open our link in web browser
webbrowser.open(urlForAuth)


# OAuth 1.0 authorization 'get' request
# Return json file with full request
def authorize_get_request(url):
    authorized_token_key = Result.result.split('=')[1].split('&')[0]
    authorized_token_secret = Result.result.split('&')[1].split('=')[1]
    params = {
        'oauth_consumer_key': user_data.consumer_key,
        'oauth_token': str(authorized_token_key),
        'oauth_nonce': str(uuid.uuid4()),
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_timestamp': str(int(time.time())),
        'oauth_version': '1.0'
    }
    # making oauth_signature
    token_secret = bytes(authorized_token_secret, 'utf-8')

    encoded_params = '&'.join(['%s=%s' % (item[0], item[1]) for item in sorted(params.items())])

    oauth_request_base = ('GET' + '&' + ur.quote_plus(url) + '&' + ur.quote_plus(encoded_params)).encode('utf-8')
    oauth_signature = base64.b64encode(
        hmac.new(user_data.consumer_secret + b'&' + token_secret, oauth_request_base, sha1).digest())

    params['oauth_signature'] = oauth_signature

    oauth_header = 'OAuth ' + ', '.join(
        ['%s="%s"' % (item[0], ur.quote_plus(item[1])) for item in sorted(params.items())])

    # getting data and converting html to json
    list = xmltodict.parse(requests.get(url, headers={'Authorization': oauth_header}).text)
    jsonData = json.dumps(list)

    return jsonData


# callback after user authorized
@app.route('/callback')
def callback():
    token = request.args.get('oauth_token')
    secret = Result.result.split('&')[1].split('=')[1]
    url = 'https://api.tripit.com/oauth/access_token'

    params = {
        'oauth_consumer_key': str(user_data.consumer_key),
        'oauth_nonce': str(uuid.uuid4()),
        'oauth_signature_method': 'HMAC-SHA1',
        'oauth_timestamp': str(int(time.time())),
        'oauth_token': str(token),
        'oauth_token_secret': str(secret),
        'oauth_version': '1.0'
    }

    # making oauth_signature
    token_secret = bytes(secret, 'utf-8')

    encoded_params = '&'.join(['%s=%s' % (item[0], item[1]) for item in sorted(params.items())])

    oauth_request_base = ('POST' + '&' + ur.quote_plus(url) + '&' + ur.quote_plus(encoded_params)).encode('utf-8')
    oauth_signature = base64.b64encode(
        hmac.new(user_data.consumer_secret + b'&' + token_secret, oauth_request_base, sha1).digest())

    params['oauth_signature'] = oauth_signature

    oauth_header = 'OAuth ' + ', '.join(
        ['%s="%s"' % (item[0], ur.quote_plus(item[1])) for item in sorted(params.items())])

    Result.result = requests.post(url, headers={'Authorization': oauth_header}).text

    time.sleep(5)

    # test page (can be deleted)
    webbrowser.open('http://127.0.0.1:5000/info')

    return 'Redirecting on http://localhost:5000/info'


# method write list of "any object" information to trip_info.json
# Possible objects: trip, object, points_program
def get_list_trips(object):
    url = 'https://api.tripit.com/v1/list/' + str(object)

    jsonData = authorize_get_request(url)

    with open(object + "_info.json", "w") as file:
        file.write(jsonData)

    print('List of flights was successfully received and data was saved in trip_info.json')

    return 'List of flights was successfully received and data was saved in trip_info.json'


# method write information about one trip by id to one_trip_info.json
# object is one of the following strings:
# air, activity, car, cruise, directions, lodging, mapm note, rail, restaurant, transport, trip
def get_one_trip(object, id):
    url = 'https://api.tripit.com/v1/get/' + str(object) + '/id/' + str(id)

    jsonData = authorize_get_request(url)

    with open("one_" + object + "_info.json", "w") as file:
        file.write(jsonData)

    print('Info about a flight was successfully received and Data was saved in one_trip_info.json')

    return 'Info about a flight was successfully received and Data was saved in one_trip_info.json'


# test page to show that something work :)
@app.route('/info')
def info():
    object = 'object'
    filename = object + '_info'
    get_list_trips('object')
    test_hotel: Hotel
    test_trip: Trip
    if object.__eq__('object'):
        test_hotel = Hotel(filename)
    else:
        test_trip = Trip(filename)
        get_one_trip('trip', str(test_trip.id))

    # file to show that methods are working correctly
    with open(object + ".txt", "w") as file:
        file.write(test_hotel.toString())

    print('Data was successfully saved in trip object.txt\nHotel Info:\n' + test_hotel.toString())

    return 'Data was successfully saved'


# Starting server on Flask
if __name__ == '__main__':
    app.run(debug='True')
