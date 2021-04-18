from urllib.request import urlopen
from urllib.error import HTTPError, URLError
try:
    html = urlopen('https://github.com/annzc/hello.git')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')
