import sys, os, time
testdir = os.path.dirname(__file__)
srcdir = '../cine_io'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
import json
import cine_io
from mock import patch, Mock

fake_project = {"id": "PROJECT_ID", "name": "PROJECT_NAME"}
fake_project_2 = {"id": "SECOND_PROJECT_ID", "name": "SECOND_PROJECT_NAME"}
delete_project = {"id": "PROJECT_ID", "deletedAt": "2014-06-11T23:36:59.287Z"}
delete_stream = {"id": "STREAM_ID", "deletedAt": "2014-06-11T23:39:20.824Z"}
delete_stream_recording = {"deletedAt": "2014-06-11T23:40:20.824Z"}
fake_project_update = {"id": "PROJECT_ID", "name": "new project name"}
fake_stream_1 = {"id": "STREAM1_ID", "password": "STREAM1_PASSWORD", "record": False}
fake_stream_1_update = {"id": "STREAM1_ID", 'name': 'new stream name', "record": False}
fake_stream_with_name = {"id": "STREAM3_ID", 'name': 'new stream name', "record": False}
fake_stream_with_record = {"id": "STREAM3_ID", "record": True}
fake_stream_2 = {"id": "STREAM2_ID", "password": "STREAM2_PASSWORD", "record": False}
fake_fmle_profile = {"content": "<flashmedialiveencoder_profile></flashmedialiveencoder_profile>"}
fake_stream_recording_1 = {"name": "STREAM1_RECORDING_1_NAME", "url": "STREAM1_RECORDING_1_URL"}
fake_stream_recording_2 = {"name": "STREAM1_RECORDING_2_NAME", "url": "STREAM1_RECORDING_2_URL"}

def stub_response(mock_requests, response):
  a = Mock()
  a.json.side_effect = [response]
  mock_requests.return_value = a

class CineIOTestCase(unittest.TestCase):
  def setUp(self):
    self.client = cine_io.Client({"secretKey": "CINE_IO_SECRET_KEY"})
    self.masterClient = cine_io.Client({"masterKey": "CINE_IO_MASTER_KEY"})

class ConfigTest(CineIOTestCase):
  def runTest(self):
    self.assertEqual(self.client.config, {"secretKey": "CINE_IO_SECRET_KEY"})

class IndexProjectsTest(CineIOTestCase):
  @patch('cine_io.requests.get')
  def runTest(self, mock_requests):
    stub_response(mock_requests, [fake_project, fake_project_2])
    projects = self.masterClient.projects.index()
    self.assertEqual(len(projects), 2)
    self.assertIsInstance(projects[0], cine_io.Project)
    self.assertEqual(projects[0].id, 'PROJECT_ID')
    self.assertEqual(projects[1].id, 'SECOND_PROJECT_ID')
    self.assertEqual(projects[0].name, 'PROJECT_NAME')

class GetProjectTest(CineIOTestCase):
  @patch('cine_io.requests.get')
  def runTest(self, mock_requests):
    stub_response(mock_requests, fake_project)
    project = self.client.project.get()
    self.assertIsInstance(project, cine_io.Project)
    self.assertEqual(project.id, 'PROJECT_ID')
    self.assertEqual(project.name, 'PROJECT_NAME')

class UpdateProjectTest(CineIOTestCase):
  @patch('cine_io.requests.put')
  def runTest(self, mock_requests):
    stub_response(mock_requests, fake_project_update)
    project = self.client.project.update({'name': 'new project name'})
    self.assertIsInstance(project, cine_io.Project)
    self.assertEqual(project.id, 'PROJECT_ID')
    self.assertEqual(project.name, 'new project name')

class DeleteProjectTest(CineIOTestCase):
  @patch('cine_io.requests.delete')
  def runTest(self, mock_requests):
    stub_response(mock_requests, delete_project)
    deleted_time = self.client.project.delete()
    self.assertEqual(deleted_time, '2014-06-11T23:36:59.287Z')

class PeerGenerateIdentitySignature(CineIOTestCase):
  @patch('time.time')
  def runTest(self, mock_requests):
    mock_requests.return_value = 1420261680.958718
    response = self.client.peer.generate_identity_signature("Thomas")
    self.assertEqual(response['identity'], 'Thomas')
    self.assertEqual(response['signature'], '17b3c8404d89f92799a1bdb955e6f28f0a318646')
    self.assertEqual(response['timestamp'], 1420261680)

class StreamsIndexTest(CineIOTestCase):
  @patch('cine_io.requests.get')
  def runTest(self, mock_requests):
    stub_response(mock_requests, [fake_stream_1, fake_stream_2])
    streams = self.client.streams.index()
    self.assertEqual(len(streams), 2)
    self.assertIsInstance(streams[0], cine_io.Stream)
    self.assertEqual(streams[0].id, 'STREAM1_ID')
    self.assertEqual(streams[1].id, 'STREAM2_ID')

class StreamsIndexWithNameTest(CineIOTestCase):
  @patch('cine_io.requests.get')
  def runTest(self, mock_requests):
    stub_response(mock_requests, [fake_stream_1, fake_stream_2])
    streams = self.client.streams.index({"name": 'my name'})
    self.assertEqual(len(streams), 2)
    self.assertIsInstance(streams[0], cine_io.Stream)
    self.assertEqual(streams[0].id, 'STREAM1_ID')
    self.assertEqual(streams[1].id, 'STREAM2_ID')

class StreamGetTest(CineIOTestCase):
  @patch('cine_io.requests.get')
  def runTest(self, mock_requests):
    stub_response(mock_requests, fake_stream_1)
    stream = self.client.streams.get('STREAM1_ID')
    self.assertIsInstance(stream, cine_io.Stream)
    self.assertEqual(stream.id, 'STREAM1_ID')
    self.assertEqual(stream.password, 'STREAM1_PASSWORD')

class StreamDeleteTest(CineIOTestCase):
  @patch('cine_io.requests.delete')
  def runTest(self, mock_requests):
    stub_response(mock_requests, delete_stream)
    deleted_time = self.client.streams.delete('STREAM_ID')
    self.assertEqual(deleted_time, '2014-06-11T23:39:20.824Z')

class StreamUpdateTest(CineIOTestCase):
  @patch('cine_io.requests.put')
  def runTest(self, mock_requests):
    stub_response(mock_requests, fake_stream_1_update)
    stream = self.client.streams.update('STREAM1_ID', {'name': 'new stream name'})
    self.assertIsInstance(stream, cine_io.Stream)
    self.assertEqual(stream.id, 'STREAM1_ID')
    self.assertEqual(stream.name, 'new stream name')

class StreamFmleProfileTest(CineIOTestCase):
  @patch('cine_io.requests.get')
  def runTest(self, mock_requests):
    stub_response(mock_requests, fake_fmle_profile)
    profile = self.client.streams.fmle_profile('538f79dddfd24d0a00647085')
    self.assertTrue(profile.find("flashmedialiveencoder_profile") != -1)

class StreamCreateTest(CineIOTestCase):
  @patch('cine_io.requests.post')
  def runTest(self, mock_requests):
    stub_response(mock_requests, fake_stream_2)
    stream = self.client.streams.create()
    self.assertIsInstance(stream, cine_io.Stream)
    self.assertEqual(stream.id, 'STREAM2_ID')
    self.assertEqual(stream.password, 'STREAM2_PASSWORD')
    self.assertEqual(stream.record, False)

class StreamCreateWithNameTest(CineIOTestCase):
  @patch('cine_io.requests.post')
  def runTest(self, mock_requests):
    stub_response(mock_requests, fake_stream_with_name)
    stream = self.client.streams.create({'name': 'new stream name'})
    self.assertIsInstance(stream, cine_io.Stream)
    self.assertEqual(stream.id, 'STREAM3_ID')
    self.assertEqual(stream.name, 'new stream name')
    self.assertEqual(stream.record, False)

class StreamCreateWithRecordTest(CineIOTestCase):
  @patch('cine_io.requests.post')
  def runTest(self, mock_requests):
    stub_response(mock_requests, fake_stream_with_record)
    stream = self.client.streams.create({'record': True})
    self.assertIsInstance(stream, cine_io.Stream)
    self.assertEqual(stream.id, 'STREAM3_ID')
    self.assertEqual(stream.record, True)

class StreamRecordingsIndexTest(CineIOTestCase):
  @patch('cine_io.requests.get')
  def runTest(self, mock_requests):
    stub_response(mock_requests, [fake_stream_recording_1, fake_stream_recording_2])
    recordings = self.client.streams.recordings.index("STREAM1_ID")
    self.assertEqual(len(recordings), 2)
    self.assertIsInstance(recordings[0], cine_io.StreamRecording)
    self.assertEqual(recordings[0].name, 'STREAM1_RECORDING_1_NAME')
    self.assertEqual(recordings[1].url, 'STREAM1_RECORDING_2_URL')

class StreamRecordingsDeleteTest(CineIOTestCase):
  @patch('cine_io.requests.delete')
  def runTest(self, mock_requests):
    stub_response(mock_requests, delete_stream_recording)
    deleted_time = self.client.streams.recordings.delete("STREAM1_ID", "NAME")
    self.assertEqual(deleted_time, '2014-06-11T23:40:20.824Z')
