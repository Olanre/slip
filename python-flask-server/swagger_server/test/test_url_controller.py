# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.url import URL  # noqa: E501
from swagger_server.models.ur_ls import URLs  # noqa: E501
from swagger_server.test import BaseTestCase

"""
Do not edit I will make my changes here
"""

class TestUrlController(BaseTestCase):
    """UrlController integration test stubs"""

    def test_delete_url(self):
        """Test case for delete_url

        Deletes an encoded url
        """
        response = self.client.open(
            '/v2/url/{tiny_url}'.format(tiny_url='tiny_url_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_encode_url(self):
        """Test case for encode_url

        Encode a new url
        """
        response = self.client.open(
            '/v2/url/'.format(long_url='long_url_example'),
            method='POST',
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_urls(self):
        """Test case for get_all_urls
        Why Hello there
        Gets the list of all encoded urls
        """
        response = self.client.open(
            '/v2/url/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_long_url_by_id(self):
        """Test case for get_long_url_by_id
        Why Hello there
        Extract a URL entry by the given tiny URL
        """
        response = self.client.open(
            '/v2/url/{tiny_url}'.format(tiny_url='tiny_url_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        


if __name__ == '__main__':
    import unittest
    unittest.main()
