import requests

def get_content(url,pms):
    r =requests.get(url,params=pms)
    print(r.status_code)
    print(r.url)
    print(r.content)
    return r


get_content("https://www.youtube.com/watch","c2gSzYLJ8sY&list=RDc2gSzYLJ8sY")
