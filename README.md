# cine.io python egg

[![Build Status](https://travis-ci.org/cine-io/cineio-python.svg?branch=master)](https://travis-ci.org/cine-io/cineio-python)

The python egg for [cine.io](cine.io).

## Installation

> I haven't registered cine_io as an egg yet on: https://pypi.python.org/pypi

Add this line to your application's Gemfile:

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

To fetch the [Flash Media Live Encoder](http://www.adobe.com/products/flash-media-encoder.html) profile for a stream:

```python
stream = client.streams.fmle_profile('STREAM_ID')
# => String of profile contents
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
