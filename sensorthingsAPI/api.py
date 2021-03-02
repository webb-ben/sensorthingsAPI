#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ben Webb

import http.client
import os.path
import json

class httpHandler:
    def __init__(self, hostname, version):
        self._hostname = hostname
        self._conn = http.client.HTTPSConnection( self._hostname )
        self._version = version

    def _get_version(self):
        return self._version

    def _get_request(self):
        return self._request

    def _get_querystring(self):
        try:
            return '?' + self._querystring
        except AttributeError and TypeError:
            return False

    def _make_request(self, req):
        self._request = req

    def _make_querystring(self, qset):
        set = [''.join('$' + key + '=' + str(value)) for key, value in qset.items()]
        qs = '&'.join(set)
        self._querystring = qs

    def _make_path(self):
        path = os.path.join('/', self._get_version(), self._get_request())
        if self._get_querystring():
            path = ''.join((path, self._get_querystring()))
        return path

    def get(self, req, qs = None):
        self._make_request(req)
        if qs: self._make_querystring(qs)
        self._conn.request("GET", self._make_path())
        self._request, self._querystring = None, None

    def get_response(self):
        try:
            self._response = self._conn.getresponse()
        except http.client.ResponseNotReady:
            if not self._response:
                raise http.client.ResponseNotReady
        return self._response

    def get_status(self):
        return self.get_response().status

    def get_headers(self):
        return self.get_response().getheaders()

    def get_read(self):
        return json.loads(self.get_response().read())

    def get_dumps(self):
        return json.dumps(self.get_read(), indent=4, sort_keys=True)
