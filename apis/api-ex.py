'''
common status codes include:

200: OK - The request has succeeded.
201: Created - The request has been fulfilled and a new resource has been created.
400: Bad Request - The server could not understand the request due to invalid syntax.
401: Unauthorized - The client must authenticate itself to get the requested response.
403: Forbidden - The client does not have access rights to the content.
404: Not Found - The server can not find the requested resource.
500: Internal Server Error - The server has encountered a situation it doesn't know how to handle.



'''
import requests

# Make a Get request to a URL
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # print the response content
    print(response.json())
else:
    # print an error message with the status code
    print(f"Error: Received status code {response.status_code}")