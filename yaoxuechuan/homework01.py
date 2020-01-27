import requests
import  sys
def  test(url_test):
    payload={'page':'1','count':'2'}
    urltest=url_test
    req=requests.post(urltest,data=payload, verify=False)
    print(req.url)
    print(type(req.text))

    print(type(req.json()))

    print(req.headers)

urlname=sys.argv[1]

test(urlname)
# test_url="https://api.github.com/repos/clairyin/homework/contents"
# win_url="J:/xew1.txt"
# with open(win_url, 'rb') as f:
#     print(f.readlines())
# def  get_git():
#
#     req=requests.get(test_url)
#     #print(req.text)
#     print(req.json())
#
#     file = open(win_url, 'rb')
#     files = {'file': file}
#     requests.post(test_url,)
# get_git()