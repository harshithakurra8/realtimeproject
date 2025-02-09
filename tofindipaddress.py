from requests import get
ip = get('https://api.ipify.org').text
print("======IP Address======")
print(f"My IP Address is:{ip}")
print("=====**********=======")