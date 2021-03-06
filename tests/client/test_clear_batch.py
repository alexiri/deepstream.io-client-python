from deepstreamio_client import Client


def test_clearing_batch():
    request = {
        'topic': 'record',
        'action': 'read',
        'recordName': 'some-record',
    }

    client = Client("http://url.com")
    client.start_batch().add_to_batch(request)

    assert client.start_batch().add_to_batch(request)._batch == [request]
    assert client.clear_batch()._batch == []
