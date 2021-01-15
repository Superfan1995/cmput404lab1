import requests

# third script
response = requests.get('https://raw.githubusercontent.com/Superfan1995/cmput404lab1/main/lab1.py')

f = open("new_lab1.py", "w")
f.write(response.text)
f.close()

print(response.text)