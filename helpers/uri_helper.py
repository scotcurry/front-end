def uri_to_path_valid_path(uri, development_environment):

    protocol = uri[0:8]
    if development_environment == 'true':
        if uri[0:7] == 'http://':
            next_slash = uri.find('/', 8)
            host_portion = uri[7:next_slash]
            uri_to_return = 'http://{0}'.format(host_portion)
            return uri_to_return
        return uri
    if development_environment != 'true' and protocol != 'https://':
        if uri[0:7] == 'http://':
            next_slash = uri.find('/', 8)
            host_portion = uri[7:next_slash]

            uri_to_return = 'https://{0}/frontend'.format(host_portion)
            return uri_to_return
