import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../cine_io'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
import json
import cine_io
from mock import patch, Mock

fake_project = {"id": "PROJECT_ID", "name": "PROJECT_NAME"}
fake_stream_1 = {"id": "STREAM1_ID", "password": "STREAM1_PASSWORD"}
fake_stream_2 = {"id": "STREAM2_ID", "password": "STREAM2_PASSWORD"}
fake_fmle_profile = {"content": "<flashmedialiveencoder_profile></flashmedialiveencoder_profile>"}

def stub_response(mock_urlopen, response):
  a = Mock()
  a.read.side_effect = [json.dumps(response)]
  mock_urlopen.return_value = a

class CineIOTestCase(unittest.TestCase):
  def setUp(self):
    self.client = cine_io.Client({"secretKey": "CINE_IO_SECRET_KEY"})

class ConfigTest(CineIOTestCase):
  def runTest(self):
    self.assertEqual(self.client.config, {"secretKey": "CINE_IO_SECRET_KEY"})

class GetProjectTest(CineIOTestCase):
  @patch('cine_io.urllib2.urlopen')
  def runTest(self, mock_urlopen):
    stub_response(mock_urlopen, fake_project)
    project = self.client.project.get()
    self.assertIsInstance(project, cine_io.Project)
    self.assertEqual(project.id, 'PROJECT_ID')
    self.assertEqual(project.name, 'PROJECT_NAME')

class StreamsIndexTest(CineIOTestCase):
  @patch('cine_io.urllib2.urlopen')
  def runTest(self, mock_urlopen):
    stub_response(mock_urlopen, [fake_stream_1, fake_stream_2])
    streams = self.client.streams.index()
    self.assertEqual(len(streams), 2)
    self.assertIsInstance(streams[0], cine_io.Stream)
    self.assertEqual(streams[0].id, 'STREAM1_ID')
    self.assertEqual(streams[1].id, 'STREAM2_ID')

class StreamGetTest(CineIOTestCase):
  @patch('cine_io.urllib2.urlopen')
  def runTest(self, mock_urlopen):
    stub_response(mock_urlopen, fake_stream_1)
    stream = self.client.streams.get('STREAM1_ID')
    self.assertIsInstance(stream, cine_io.Stream)
    self.assertEqual(stream.id, 'STREAM1_ID')
    self.assertEqual(stream.password, 'STREAM1_PASSWORD')

class StreamFmleProfileTest(CineIOTestCase):
  @patch('cine_io.urllib2.urlopen')
  def runTest(self, mock_urlopen):
    stub_response(mock_urlopen, fake_fmle_profile)
    profile = self.client.streams.fmle_profile('538f79dddfd24d0a00647085')
    self.assertTrue(profile.find("flashmedialiveencoder_profile") != -1)

class StreamCreateTest(CineIOTestCase):
  @patch('cine_io.urllib2.urlopen')
  def runTest(self, mock_urlopen):
    stub_response(mock_urlopen, fake_stream_2)
    stream = self.client.streams.create()
    self.assertIsInstance(stream, cine_io.Stream)
    self.assertEqual(stream.id, 'STREAM2_ID')
    self.assertEqual(stream.password, 'STREAM2_PASSWORD')
