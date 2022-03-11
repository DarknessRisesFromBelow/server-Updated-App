import requests

ver = 1.09
serverAddress = "http://192.168.1.15:8080/update{}".format(ver)
a = requests.get(serverAddress).content

a = str(a)
a = a.replace("b'", "")
a = a.replace("'", "")

print(a)
