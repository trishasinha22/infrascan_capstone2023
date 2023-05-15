import requests
from bs4 import BeautifulSoup

def csrf_scanner(url1):
    target_url = url1.get('url1')
    # Define the list of HTTP methods to test
    http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

    # Send a GET request to the target URL
    response = requests.get(target_url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the HTML forms in the response
    forms = soup.find_all('form')

    # Loop through each form
    for form in forms:
        # Get the form action attribute
        form_action = form.get('action')

        # Loop through each HTTP method
        for http_method in http_methods:
            # Send a request to the form action URL using the current HTTP method
            if http_method == 'GET':
                # If the HTTP method is GET, append the form data to the URL
                form_data = {}
                for input_field in form.find_all('input'):
                    input_name = input_field.get('name')
                    input_value = input_field.get('value')
                    if input_name:
                        form_data[input_name] = input_value
                response = requests.get(target_url + form_action, params=form_data)
            else:
                # If the HTTP method is not GET, send a request with the form data
                form_data = {}
                for input_field in form.find_all('input'):
                    input_name = input_field.get('name')
                    input_value = input_field.get('value')
                    if input_name:
                        form_data[input_name] = input_value
                response = requests.request(http_method, target_url + form_action, data=form_data)

            # Check if the response contains any indications of a CSRF vulnerability
            if 'CSRF' in response.text:
                return f'Possible CSRF vulnerability found, HTTP method: {http_method}'
            else:
                return "CSRF vulnerability Not found"

#csrf_scanner('http://testphp.vulnweb.com/artists.php?artist=1')
