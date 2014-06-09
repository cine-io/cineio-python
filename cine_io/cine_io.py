import urllib2
import urllib
import json
from StringIO import StringIO
BASE_URL = 'https://www.cine.io/api/1/-'

class Project:
  def __init__(self, data):
    for key, value in data.iteritems():
      setattr(self, key, value)

class Stream:
  def __init__(self, data):
    for key, value in data.iteritems():
      setattr(self, key, value)

class ProjectsHandler:
  def __init__(self, client):
    self.client = client

  def get(self):
    params = {'secretKey': self.client.config['secretKey']}
    req = urllib2.Request(BASE_URL + '/project?' + urllib.urlencode(params))
    response = urllib2.urlopen(req)
    return Project(json.loads(response.read()))

class StreamsHandler:
  def __init__(self, client):
    self.client = client

  def index(self):
    params = {'secretKey': self.client.config['secretKey']}
    req = urllib2.Request(BASE_URL + '/streams?' + urllib.urlencode(params))
    response = urllib2.urlopen(req)
    return map(Stream, json.loads(response.read()))

  def get(self, id):
    params = {'secretKey': self.client.config['secretKey'], 'id': id}
    req = urllib2.Request(BASE_URL + '/stream?' + urllib.urlencode(params))
    response = urllib2.urlopen(req)
    return Stream(json.loads(response.read()))

  def fmle_profile(self, id):
    params = {'secretKey': self.client.config['secretKey'], 'fmleProfile': 'true', 'id': id}
    req = urllib2.Request(BASE_URL + '/stream?' + urllib.urlencode(params))
    response = urllib2.urlopen(req)
    return json.loads(response.read())['content']

  def create(self):
    url = BASE_URL + '/stream'
    params = {'secretKey': self.client.config['secretKey']}
    req = urllib2.Request(url, urllib.urlencode(params))
    response = urllib2.urlopen(req)
    return Stream(json.loads(response.read()))

class Client:

  def __init__(self, config):
    self.config = config
    self.project = ProjectsHandler(self)
    self.streams = StreamsHandler(self)
