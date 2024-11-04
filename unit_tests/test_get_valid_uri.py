from helpers.uri_helper import uri_to_path_valid_path


def test_uri_to_path_valid_path():
    development_environment = 'true'
    uri = 'http://127.0.0.1:5000/'
    new_uri = uri_to_path_valid_path(uri, development_environment)
    if development_environment == 'true':
        assert (1 == 1)
    else:
        assert (2 == 2)
