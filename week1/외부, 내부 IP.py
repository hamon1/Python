''' 자시의 컴퓨터의 외부 및 내부 IP를 확인할 수 있는 코드를 만들어본다.
가상 환경 등으로 내부의 IP가 변경되더라도 정확한 IP를 찾을 수 있는 방법에 대해서도
알아본다. '''

import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부 IP: ", in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ",out_addr)
