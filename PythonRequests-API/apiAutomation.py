import json
import requests

#Get Request
from requests import ReadTimeout
from urllib3.exceptions import ReadTimeoutError

print("------GET call with reqres.com---------\n")
response = requests.get("https://reqres.in/api/users?page=2")

#Response can be printed in 3 ways
print("-----Response can be printed in 3 ways-------\n")
print("Response can printed using CONTENT : ", response.content)
print("Response can printed using TEXT : ", response.text)
print("Response can printed using JSON : ", response.json())

#status code
print("------Status code-------")
print("Status code is : ",response.status_code)

#Assertion
assert  response.status_code==200,"Assertion failed"
print("Assertion successfull ")

#Printing - headers,cookies,encoding,url
print("--------Headers,cookies,encoding and URL has been printed-------")
print("Headers are : ",response.headers)
print("Specfic header retrieval : ",response.headers.get("Content-Type"))#pass the key here!!!
print("Cookies are : ",response.cookies)
print("Encoding is : ",response.encoding)
print("Url is : ",response.url)

#Assertion to the response body.
resp=response.json()
print("In json format :",resp)
emailId=resp['data'][0]['email']#this is how we have to write json path with exact this syntax.
print(emailId)
assert emailId=="michael.lawson@reqres.in" , "Assertion failed"
assert emailId.endswith("lawson@reqres.in")

#Different ways of calling an api - requests.get(url,params=none,kwargs)
#url - https://reqres.in/api/users?page=2
print("---------Get call by using param variable in url with dictionaries---------")
url="https://reqres.in/api/users"#question mark is need not to be passed as we have passed in params
dict={
"page":2
}
rsp=requests.get(url,params=dict)
print("By passing query param response : ",rsp.json())
print("Url is : " ,rsp.url)

#***************************************************************************************#

#HTTP method - POST.
print("------------Post call for reqres.in by passing payload as dictionary---------")
url="https://reqres.in/api/users"
payload={
    "name": "Sharath",
    "job": "SDET"
}
response = requests.post(url,data=payload)
print(response.status_code)
print(response.json())

#validation
assert response.status_code==201,"Assertion failed need to check"
rsp=response.json()
assert rsp['name']=='Sharath' , "Assertion failed"
assert rsp['job']=='SDET',"Assertion failed"

#using json file
print("------------Post call for reqres.in by passing payload as json file---------")
file=open("/Users/sharath.bc/PycharmProjects/PythonPractice1/PythonRequests-API/payload.json","r")
jsonfile=file.read()
jsonobj=json.loads(jsonfile)#Deserialises the json to python object.
response=requests.post(url,data=jsonobj)#we can even pass the ["id": "11223"] as well.
print(response.json())

#*****************************************************************#

#PUT method
print("---------------PUT call---------------")
url="https://reqres.in/api/users/2"
putPayload={
    "name":"Sharath",
    "job":"SDET"
}
rsp=requests.put(url,data=putPayload)
print(rsp.json())
#valodation
assert rsp.status_code==200,"status code Assertion failed"
assert rsp.json()['name']=="Sharath","name Assertion failed"

#************************************************************************#

#PATCH method
print("---------------PATCH call---------------")
url="https://reqres.in/api/users/2"
putPayload={
    "name":"Sharath",
    "job":"SDET"
}
rsp=requests.patch(url,data=putPayload)
print(rsp.json())
#valodation
assert rsp.status_code==200,"status code Assertion failed"
assert rsp.json()['name']=="Sharath","name Assertion failed"

#*****************************************************************#

#DELETE call
print("---------------Delete call--------------")
url="https://reqres.in/api/users?"
param={
    "page":2
}
rsp=requests.delete(url,params=param)
print(rsp.status_code)
assert rsp.status_code==204,"Assertion failed"

#********************************************************************#

#How to make an API fail with timeout.
print("-----------------------Timeout scenario---------------")
url="http://httpbin.org/delay/5"
try:
    response=requests.get(url,timeout=3)
except TimeoutError :
    print("timeoutError handled",response.status_code)
except ReadTimeoutError :
    print("timeoutError handled",response.status_code)
except ReadTimeout :
    print("timeoutError handled",response.status_code)
#Handled almost all the timeout to capture the status code but some other status code is printed.

#****************************************************************#

#Handling the authentication.
print("-----------------------Handling the authentication POSITIVE SCENARIO--------------")
response=requests.get("http://the-internet.herokuapp.com/basic_auth",auth=('admin','admin'))
print("FOR THE RIGHT CREDENTIALS WE WILL GET : " ,response.status_code)

print("-----------------------Handling the authentication NEGATIVE SCENARIO--------------")
response=requests.get("http://the-internet.herokuapp.com/basic_auth",auth=('SHARATH','admin'))
print("FOR THE WRONG CREDENTIALS WE WILL GET : ",response.status_code)

#*****************************************************************#