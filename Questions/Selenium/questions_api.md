1.What is API testing?
Explanation of API (Application Programming Interface) testing and its purpose in software development.

2.How is API testing different from UI testing?

Clarification on the distinctions between API testing and UI testing, 
emphasizing that API testing focuses on the backend services and their functionality.

3.What are the key benefits of API testing?
Discussion on the advantages of API testing, such as faster test execution, better test coverage, and early detection of issues.

4.Explain the main types of API testing.
Differentiating between types of API testing, including Unit Testing, Integration Testing, and End-to-End (E2E) Testing.

5.What is an API endpoint?
Definition and explanation of API endpoints, which are specific URLs or URIs that represent the entry point for a web service.

6.What is the difference between REST and SOAP? 
Comparison of REST (Representational State Transfer) and SOAP (Simple Object Access Protocol) as two different web service architectures.

7.What is an HTTP status code, and can you name a few common ones?
Explanation of HTTP status codes and examples of common ones like 200 OK, 404 Not Found, and 500 Internal Server Error.

8.What is the purpose of the "Authorization" header in API requests?
Clarification on the role of the "Authorization" header in API requests, typically used for authentication and security.

9.What are the common authentication methods used in API testing?
Explanation of authentication methods such as API keys, OAuth, and basic authentication commonly used in API testing.

10.What is JSON and how is it used in API responses?
Overview of JSON (JavaScript Object Notation) as a data interchange format and its usage in API responses.

11.Explain the term "Swagger" in the context of API testing.
Description of Swagger (OpenAPI Specification) as a tool for API documentation and testing.

12.What is Postman, and how can it be used in API testing?
Introduction to Postman as an API development and testing tool, including the creation of requests and running collections.

13.What is the purpose of API versioning?
Explanation of API versioning and its importance in maintaining backward compatibility while introducing changes to APIs.

14.What is load testing, and why is it important for APIs?
Definition of load testing in the context of APIs and its significance in evaluating the system's performance under varying loads.

15.Can you explain the concept of mocking in API testing?
Discussion on API mocking, where simulated responses are provided during testing to mimic real API behavior.

-------------------------------------------------------------------
Popular status codes : 

HTTP status codes are three-digit numbers returned by a server in response to a client's request made to the server. 
They provide information about the result of the request and are grouped into different classes. 
Here are some popular and commonly encountered HTTP status codes:

1xx Informational Responses:
100 Continue: The server has received the request headers and the client should proceed to send the request body.

2xx Success:
200 OK:
The request was successful, and the server has returned the requested data.

201 Created:
The request was successful, and a new resource was created as a result.

204 No Content:
The server successfully processed the request, but there is no additional content to send in the response.
[Successful Update or Deletion:,Successful POST Request without Response Body:]

3xx Redirection:
301 Moved Permanently:
The requested resource has been permanently moved to a new location.

302 Found (or 303 See Other):
The requested resource has been temporarily moved to a different location.

4xx Client Errors:
400 Bad Request:
The server could not understand the request due to invalid syntax or other client-side error.

401 Unauthorized:
The request requires user authentication.

403 Forbidden:
The server understood the request, but it refuses to authorize it.

404 Not Found:
The requested resource could not be found on the server.

5xx Server Errors:
500 Internal Server Error:
A generic error message indicating that an unexpected condition was encountered on the server.

502 Bad Gateway:
The server, while acting as a gateway or proxy, received an invalid response from an inbound server.

503 Service Unavailable:
The server is not ready to handle the request. Common causes include a temporary overloading or maintenance of the server.

#2. Different http methods and how to use them using the python requests ?

HTTP methods (also known as HTTP verbs) define the actions that can be performed on a resource. 
In Python, the requests library is commonly used for making HTTP requests. Here's how you can use various HTTP methods with the requests library:

1. GET Method:
The GET method is used to retrieve data from a specified resource.
[
import requests

# Example GET request
response = requests.get("https://api.example.com/data")
print(response.text)

]
2.POST Method:
The POST method is used to submit data to be processed to a specified resource.
[
import requests
# Example POST request with data
data = {"key1": "value1", "key2": "value2"}
response = requests.post(url="https://api.example.com/submit", data=data)
print(response.text)
]

3.PUT Method:
The PUT method is used to update a resource or create a new resource if it does not exist.
[
import requests
# Example PUT request with data
data = {"key1": "updated_value1", "key2": "updated_value2"}
response = requests.put("https://api.example.com/update", data=data)
print(response.text)
]

4.DELETE Method:
The DELETE method is used to request the removal of a resource.
[
import requests
# Example DELETE request
response = requests.delete("https://api.example.com/remove")
print(response.text)
]

5.PATCH Method:
The PATCH method is used to apply partial modifications to a resource.
[
import requests
# Example PATCH request with data
data = {"key1": "patched_value1"}
response = requests.patch("https://api.example.com/modify", data=data)
print(response.text)
]

6.HEAD Method:
The HEAD method is similar to GET but is used to retrieve only the headers of a resource, not the actual content.
[
import requests

# Example HEAD request
response = requests.head("https://api.example.com/resource")
print(response.headers)
]

7.OPTIONS:
The OPTIONS method is used to describe the communication options for the target resource.

[
import requests

url = "https://api.example.com/options"
response = requests.options(url)
print(response.status_code)
print(response.headers)
]

#3. Common Python requests and fetching the same : 

[
import requests

# API endpoint URL
url = "https://api.example.com/data"

# Authentication credentials (if required)
username = "your_username"
password = "your_password"
auth = (username, password)

# Payload (data to be sent with the request)
params = {"key1": "value1", "key2": "value2"}
payload = {"key1": "value1", "key2": "value2"}

# Make a GET request with authentication and payload
response = requests.get(url, auth=auth, params=params,data=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON content
    json_response = response.json()

    # Iterate through the JSON response using a for loop
    for item in json_response:
        print("Key:", item["key"])
        print("Value:", item["value"])
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
    print(response.text)

]

#4. Iteration through the loop : 

[
import requests

# API endpoint URL
url = "your_api_endpoint_here"

# Make a GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_response = response.json()

    #Iterate through all objects in the "objects" array
    for obj in json_response.get("objects", []):
        #if not none
        if objects:
        #Access the "port_in_status" and "phone_number" keys
        port_in_status = obj.get("port_in_status", None)
        phone_number = obj.get("phone_number", None)

        # Print the values
        print(f"Port_in_status: {port_in_status}, Phone_number: {phone_number}")

else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
    print(response.text)

]

code explanation : 
json_response.get("objects", []): 
This part retrieves the value associated with the key "objects" from the json_response dictionary. 
The .get() method is used to handle the case where the key may not exist in the dictionary. 
If the key is not present, it returns an empty list [] as the default value.

for obj in ...:: 
This initiates a for loop that iterates through each object in the "objects" array. 
The variable obj represents each individual object in the array during each iteration.

port_in_status = obj.get("port_in_status", None): 
Inside the loop, this line attempts to access the value associated with the key "port_in_status" within the current object (obj). 
The .get() method is used again to handle the case where the key may not exist. If the key is present, it retrieves the value; otherwise, it assigns None as the default value.