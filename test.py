#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ben Webb

from sensorthingsAPI.api import *
# import os, ssl
# if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
#     ssl._create_default_https_context = ssl._create_unverified_context

def main():
    hostname = 'airquality-frost.k8s.ilt-dmz.iosb.fraunhofer.de'
    version = 'v1.0'

    conn = httpHandler(hostname, version)

    req = 'Locations'
    qs = {'top': 1, 'skip': 5}
    conn.get(req, qs)
    print( conn.get_dumps() )

    req = 'Things(3)'
    conn.get(req)
    print( conn.get_dumps() )


if __name__ == '__main__':
    main()
