import requests
import lib.constants as constants


def send_http_request(method: str, url: str, headers: object = None, params: object = None, data: object = None):
    """
    Send a request to the given url and return the response object.
    :param method: GET | POST | PUT | DELETE | OPTIONS
    :param url: The URL endpoint to request
    :param headers: The request headers to submit
    :param params: The request parameters to append to the URL
    :param data: The request data to send
    :return: The response object
    """
    # Default init
    if headers is None:
        headers = dict()
    if params is None:
        params = dict()
    if data is None:
        data = dict()
    # Default parameters
    if "limit" not in params and method == "GET":
        params['limit'] = constants.default_limit_per_page
    # Set appropriate access token according to request type
    if constants.access_token_header_key not in headers:
        headers[constants.access_token_header_key] = constants.project_read_token if method == "GET" else constants.project_write_token

    print(f'send_http_request -> method: {method}, url: {url}, params: {params}, data: {data}')

    try:
        response = requests.request(method, constants.base_url + url, headers=headers, params=params, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'send_http_request -> HTTP error occurred: {http_err}')
        exit()
    except Exception as err:
        print(f'send_http_request -> An error occurred: {err}')
        exit()
