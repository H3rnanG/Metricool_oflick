import requests

def add_image(img):
    url = "https://app.metricool.com/api/utils/upload"
    files = {'picture': open(img, 'rb')}
    params = {
        'blogId': '3122965',
        'userId': '2487252',
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'es',
        'Cookie': 'SPRING_SECURITY_REMEMBER_ME_COOKIE=c29jaWFsQGFsbWFxdWludGEuY29tOjE3MTYwNDgzMzM3MTU6ZWI1YzBjM2JiMWY5YWM2NzBjY2FlNDUyZTg3MTE3ZmY; JSESSIONID=86C0B73C5EB5DFBF8200D326BE604430; _mcool-att-0=eyJsU291cmNlIjoiR1RNQmxvY2tlZCIsImxNZWRpdW0iOiJHVE1CbG9ja2VkIiwibExhbmRpbmciOiJHVE1CbG9ja2VkIiwibExhbmRpbmdDZyI6IkdUTUJsb2NrZWQiLCJsVmlzaXRlZCI6IkdUTUJsb2NrZWQiLCJsVmlzaXRlZENnIjoiR1RNQmxvY2tlZCJ9; crisp-client%2Fsession%2F15b0c028-f728-4a4f-add2-7657188bddac=session_0d338feb-c684-41c3-b6b2-ee453fe9b428; crisp-client%2Fsocket%2F15b0c028-f728-4a4f-add2-7657188bddac=1; AWSALB=5ArbP+P91cs3YETvOw4TBf5PtuHyOKgFVsods/paQGq9xLYeJOkaV6aYRuL8JDUL8Ym78nVm9FTOb36ByIWgpIIOFmnsY0uXgR4t1SVhuuXruqr/1/YfE94AOxzL; AWSALBCORS=5ArbP+P91cs3YETvOw4TBf5PtuHyOKgFVsods/paQGq9xLYeJOkaV6aYRuL8JDUL8Ym78nVm9FTOb36ByIWgpIIOFmnsY0uXgR4t1SVhuuXruqr/1/YfE94AOxzL',
        'Origin': 'https://app.metricool.com',
        'Referer': 'https://app.metricool.com/planner/calendar?blogId=3122965&userId=2487252',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Gpc': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
        'X-Mc-Auth': 'WMQKMHBPKWSTXBSVXTNCAXOOPMQFWHBVRBTHDXIIXOBJLSIOTKFFJYVWOSCYYWHP',
    }

    response = requests.post(url, files=files, params=params, headers=headers)

    if response.status_code == 200:
        print("Image uploaded successfully")
        return response.text
    else:
        print("Status code:", response.status_code)
        print("Response body:", response.text)
