#! /usr/bin/python3

import requests

receive = requests.get("http://localhost:5000")

print("====HTTP Response Status=====")
print(receive.status_code)
print('-----------------------------\n')

print("====HTTP Response Header=====")
print(receive.headers)
print('-----------------------------\n')

print("====HTTP Response Body=====")
print(receive.content)
print('-----------------------------\n')
