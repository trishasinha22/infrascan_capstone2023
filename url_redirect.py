import requests

def check_url(url1, max_redirects=10):
    url= url1.get('url1')
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code in [301, 302, 303, 307, 308]:
            if max_redirects > 0:
                return check_url({'url': response.headers['Location']}, max_redirects-1)
            else:
                return "Max redirects exceeded"
        else:
            return "URL is not redirecting"
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return "Cannot reach the URL"


"""URL https://trip.uber.com/"""