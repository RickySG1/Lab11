import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth


username = input("Please Enter Username: ")
password = getpass ("Please Enter Password: ")


authurl = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"


payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

token = requests.request("POST", authurl, headers=headers, data=payload)


payload2={}
headers2 = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2MTIzZGEzMTdiM2FhOTA2ZWQwYjJiMzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTYzNjkzNTIxOCwiaWF0IjoxNjM2OTMxNjE4LCJqdGkiOiJjNTFkMzE3Zi0yZGFjLTQyY2ItODcxNC1iOTZlNjNjMjJhYzEiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.yIR1rOrrNYSTbgbp-RqE3wtbIbe473woEz7A0VFe1XVExNTEGpb3v7z6BsXnombhh9CqFizAFD62rVfcQN5rN1r-CSeBQX5PD0edFJCT5qKXiGhnpgKs7DO379MVC9f1B0ASFcCayJmN-WmapLE4wE6AQ9FM9yq-cC7w18l87xijSrxRbVgwMhHq1-yIy9apS5Zl_SwAvLO29B4WiObuxnDvmiiAz7Di9OwtUbNe2JpdBY_iz4-0kCC6qtT-OlV2yKVLRIq-EmU_r7rOGJ5gXmgh9l5xrciTH4NOvsns6y7v37vvn096vfWdgc_hr94NTcwm2_gvlb3Qlll4Doe77A',
  }

list = requests.request("GET", url, headers=headers2, data=payload2)


print(list.text)

