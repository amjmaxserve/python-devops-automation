import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "title": "updated title",
    "body": "updated body",
}

# Make a PUT request to update the post
response = requests.put(url, json=data)

# check if the request was successful
if response.status_code == 200:
    print("Post updated successfully!")
    print("Response:", response.json())
else:
    print("Failed to update the post. Status code:", response.status_code)


# Make a DELETE request to delete the post
delete_response = requests.delete(url)

# Check if the delete request was successful
if delete_response.status_code == 200:
    print("Post deleted successfully!")
else:
    print("Failed to delete the post. Status code:", delete_response.status_code)
