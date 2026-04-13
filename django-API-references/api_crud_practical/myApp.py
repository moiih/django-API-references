import requests
import json


# This will be treated as a Python Application that will
# use this 'crud_api' that we have created to a extract or post
# some data into the database (via API)

# This app can be present anywhere in the system but we have made it 
# inside the project just for our convinience.

# This "myApp.py" file has no internal relation with this API project.
# It is only using the services provided by this API for its own use.
# And here it is a Python file but this can be any application
# (may be Java, PHP, Android, IOS or any other application) that wants 
# to make use of this API for retrieving, fetching or writing some 
# data into the database.


URL = "http://127.0.0.1:8080/student-api/"

# We are passing the "(id = None)" becz if initial nothing will be passing as 
# parameter during the function call then by default the "id" will be "None"
# and all the data will be fetched.
# But if some parameter or value is passing to the function at function call 
# then only data associated with "id" passed as the parameter will be displayed.

def get_data(id = None):
    data = {}           
    # This "data = {}" is used so that if "id" is None then 
    # [ variable "data" Referenced Before Assignment ] error will not occur
    # as data is already initalized as empty.
    
    if id is not None:        
        data = {'id': id}

    json_data = json.dumps(data)    # Converting (dict-type) 'data' into 'JSON' Format bu "dumps()" method.

    r = requests.get(url = URL, data = json_data)   # Creating object of 'GET' request    

    data = r.json()     # Getting (or storing) data obtained from above 'get' request

    print('\n', data)     # Finally printing it on the the console(terminal)
    print('\nStatus Code:', r.status_code)  # It will provide the status of the request (in status-code)
    print('\nRequest Headers:', r.headers)  # It will provide useful information about the request, such as, 'Content-Type', etc.
    print('\nRequest Headers(Content-Type):', r.headers['content-type'])  # To get selected information in 'headers'.

get_data()   # Calling Function For Getting Data From API



def post_data():
    data=  {                # This 'data' is not 'JSON' data. Its a 'Dictionary' (dict-type)
        'name': 'Ashwin',
        'roll': 309,
        'city': 'Chennai'
    }

    json_data = json.dumps(data)   
    r = requests.post(url = URL, data = json_data)  # This time the request is of type 'POST' (rest is same)
    data = r.json()
    print(data)

# post_data()   # Calling Function For Posting(Creating) Data In The Dabase Through API



def update_data():
    data = {
        'id': 1,
        'name': 'David',
        'city': 'Bangalore'
    }
    # Some bug(problem) is present in this code that even if I assign some 'Integer' value to 'name' field here
    # then it is still updating it('name' field) without showing any error.

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_data()   # Function Call For Updating Data In The Dabase Through API



def delete_data():
    data = { 'id': 8 }
    
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)    
    data = r.json()
    
    print(data)
    print('\nStatus Code:', r.status_code, end='\n\n')  # It will provide the status of the request (in status-code)
    print('\nRequest Headers:', r.headers, end='\n\n')  # It will provide useful information about the request, such as, 'Content-Type', etc.

# delete_data()   # Function Call For Deleting Data From The Dabase Using API


