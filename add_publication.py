import requests

def create_publication(publication_data):
    url = 'https://app.metricool.com/api/v2/scheduler/posts?blogId=3122965&userId=2487252&userToken=SXNJIHXHNBFGALOJAABIUAJNRNFKSMPIYHAEVJVALPIKWSYUWITKXAFBYSMWJAIA'
    x = requests.post(url, json=publication_data)

    print(x.text)
