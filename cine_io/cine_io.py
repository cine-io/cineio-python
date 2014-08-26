import requests
from .version import __version__
BASE_URL = 'https://www.cine.io/api/1/-'

HEADERS = {
  'User-Agent': "cineio-python version-" + __version__
}

class Project:
  def __init__(self, data):
    for key, value in data.items():
      setattr(self, key, value)

class Stream:
  def __init__(self, data):
    for key, value in data.items():
      setattr(self, key, value)

class StreamRecording:
  def __init__(self, data):
    for key, value in data.items():
      setattr(self, key, value)

class ProjectsHandler:
  def __init__(self, client):
    self.client = client

  def index(self):
    payload = {'masterKey': self.client.config['masterKey']}
    url = BASE_URL + '/projects'
    r = requests.get(url, params=payload, headers=HEADERS)
    return list(map(Project, r.json()))

class ProjectHandler:
  def __init__(self, client):
    self.client = client

  def get(self):
    payload = {'secretKey': self.client.config['secretKey']}
    url = BASE_URL + '/project'
    r = requests.get(url, params=payload, headers=HEADERS)
    return Project(r.json())

  def delete(self):
    payload = {'secretKey': self.client.config['secretKey']}
    url = BASE_URL + '/project'
    r = requests.delete(url, params=payload, headers=HEADERS)
    return r.json()['deletedAt']

  def update(self, payload):
    payload['secretKey'] = self.client.config['secretKey']
    url = BASE_URL + '/project'
    r = requests.put(url, params=payload, headers=HEADERS)
    return Project(r.json())

class StreamsHandler:
  def __init__(self, client):
    self.client = client
    self.recordings = StreamRecordingsHandler(client)

  def index(self):
    payload = {'secretKey': self.client.config['secretKey']}
    url = BASE_URL + '/streams'
    r = requests.get(url, params=payload, headers=HEADERS)
    return list(map(Stream, r.json()))

  def get(self, id):
    payload = {'secretKey': self.client.config['secretKey'], 'id': id}
    url = BASE_URL + '/stream'
    r = requests.get(url, params=payload, headers=HEADERS)
    return Stream(r.json())

  def update(self, id, payload):
    payload['secretKey'] = self.client.config['secretKey']
    payload['id'] = id
    url = BASE_URL + '/stream'
    r = requests.put(url, params=payload, headers=HEADERS)
    return Stream(r.json())

  def delete(self, id):
    payload = {'secretKey': self.client.config['secretKey'], 'id': id}
    url = BASE_URL + '/stream'
    r = requests.delete(url, params=payload, headers=HEADERS)
    return r.json()['deletedAt']

  def fmle_profile(self, id):
    payload = {'secretKey': self.client.config['secretKey'], 'fmleProfile': 'true', 'id': id}
    url = BASE_URL + '/stream'
    r = requests.get(url, params=payload, headers=HEADERS)
    return r.json()['content']

  def create(self, payload=None):
    if (payload is None):
      payload = {}
    payload['secretKey'] = self.client.config['secretKey']
    url = BASE_URL + '/stream'
    r = requests.post(url, data=payload)
    return Stream(r.json())


class StreamRecordingsHandler:
  def __init__(self, client):
    self.client = client

  def index(self, id):
    payload = {'secretKey': self.client.config['secretKey'], 'id': id}
    url = BASE_URL + '/stream/recordings'
    r = requests.get(url, params=payload, headers=HEADERS)
    return list(map(StreamRecording, r.json()))

  def delete(self, id, recording_name):
    payload = {'secretKey': self.client.config['secretKey'], 'id': id, 'name': recording_name}
    url = BASE_URL + '/stream/recording'
    r = requests.delete(url, params=payload, headers=HEADERS)
    return r.json()['deletedAt']

class Client:

  def __init__(self, config):
    self.config = config
    self.project = ProjectHandler(self)
    self.projects = ProjectsHandler(self)
    self.streams = StreamsHandler(self)
