# cine.io python egg

[![Build Status](https://travis-ci.org/cine-io/cineio-python.svg?branch=master)](https://travis-ci.org/cine-io/cineio-python)

The [python egg](https://pypi.python.org/pypi/cine_io) for [cine.io](cine.io).

## Installation

install cine_io via pip:

    pip install cine_io

## Usage

### Initialization

```python
import cine_io
client = cine_io.Client({"secretKey": "CINE_IO_SECRET_KEY"})
```

### Methods

#### Projects

To get data about your project:

```python
project = client.project.get()
# => cine_io.Project
```

To update your project:

```python
project = client.project.update({"name": 'new project name'})
# => cine_io.Project
```

To delete your project:

```python
deleted_at = client.project.delete()
# => String of datetime when the project was deleted
```

#### Streams

To get all your streams:

```python
streams = client.streams.index()
# => [cine_io.Stream, …]
```

To get a specific stream:

```python
stream = client.streams.get('STREAM_ID')
# => cine_io.Stream
```

To create a new stream:

```python
stream = client.streams.create()
# => cine_io.Stream
```

```python
# you can optionally pass params
# params
#  name: 'a stream name'
#  record: True|False (default False). record: True will save recordings of all streaming sessions

stream = client.streams.create({"name": 'new stream name'})
# => cine_io.Stream
```

To update a specific stream:

```python
# params:
#  'name': 'some stream name'
#  record: True|False (updating a stream from true to false will not delete old stream recordings)
stream = client.streams.update('STREAM_ID', params)
# => cine_io.Stream
```

To fetch the [Flash Media Live Encoder](http://www.adobe.com/products/flash-media-encoder.html) profile for a stream:

```python
stream = client.streams.fmle_profile('STREAM_ID')
# => String of profile contents
```

To delete a stream:

```python
stream = client.streams.delete('STREAM_ID')
# => String of datetime when the stream was deleted
```

#### Stream Recordings

To get all the recordings of stream:

```python
recordings = client.streams.recordings.index('STREAM_ID')
# => [cine_io.StreamRecording, …]
```

To delete a recordings of stream:

```python
recordings = client.streams.recordings.delete('STREAM_ID', 'recordingName')
# => String of datetime when the stream recording was deleted
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
