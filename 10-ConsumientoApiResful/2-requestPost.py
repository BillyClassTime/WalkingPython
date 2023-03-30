import requests
u={'Nombre':'Billy','Apellidos':'Vanegas'}
r=requests.post('http://postman-echo.com/post',data=u)
print(r.text)