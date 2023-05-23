from django.shortcuts import render
import requests
import creds
# Create your views here.

def fetch(request):
    response = get_api_data(creds.api)
    return render(request,'index.html',{'response':response})

def get_api_data(api_key):
    url = creds.url  # Replace with the actual API endpoint
    headers = {
        "Authorization": "API_KEY {}".format(api_key),
        "Content-Type": "application/json"  # Adjust the content type if needed
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json
        # Process the data as needed
        return data
    else:
        # Handle the error response
        return None