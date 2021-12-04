import urllib.request
import urllib.parse

URL = "www.baidu.com"



data = {



}
Request = urllib.request.Request(data)
content = urllib.request.urlopen(Request).encode("utf-8")
print(content)
