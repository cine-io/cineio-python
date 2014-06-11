import requests
BASE_URL = 'https://www.cine.io/api/1/-'

class Project:
  def __init__(self, data):
    for key, value in data.items():
      setattr(self, key, value)

class Stream:
  def __init__(self, data):
    for key, value in data.items():
      setattr(self, key, value)

class ProjectsHandler:
  def __init__(self, client):
    self.client = client

  def get(self):
    payload = {'secretKey': self.client.config['secretKey']}
    url = BASE_URL + '/project'
    r = requests.get(url, params=payload)
    return Project(r.json())

class StreamsHandler:
  def __init__(self, client):
    self.client = client

  def index(self):
    payload = {'secretKey': self.client.config['secretKey']}
    url = BASE_URL + '/streams'
    r = requests.get(url, params=payload)
    return map(Stream, r.json())

  def get(self, id):
    payload = {'secretKey': self.client.config['secretKey'], 'id': id}
    url = BASE_URL + '/stream'
    r = requests.get(url, params=payload)
    return Stream(r.json())

  def fmle_profile(self, id):
    payload = {'secretKey': self.client.config['secretKey'], 'fmleProfile': 'true', 'id': id}
    url = BASE_URL + '/stream'
    r = requests.get(url, params=payload)
    return r.json()['content']

  def create(self):
    payload = {'secretKey': self.client.config['secretKey']}
    url = BASE_URL + '/stream'
    r = requests.post(url, data=payload)
    return Stream(r.json())

class Client:

  def __init__(self, config):
    self.config = config
    self.project = ProjectsHandler(self)
    self.streams = StreamsHandler(self)
