'''
Tests for sitemap.
'''

import logging
import unittest
import mock
from StringIO import StringIO
import json

from ckan.model import Session, Package, User
import ckan.model as model
from ckan.tests import CreateTestData
from ckan.lib.helpers import url_for
from ckan.logic.auth.get import package_show
from ckan.tests.functional.base import FunctionalTestCase

log = logging.getLogger(__file__)

class TestSitemap(FunctionalTestCase, unittest.TestCase):
    
    @classmethod
    def setup_class(cls):
        """
        Remove any initial sessions.
        """
        Session.remove()
        CreateTestData.create()
        cls._first = True
        cls._second = False

    @classmethod
    def teardown_class(cls):
        """
        Tear down, remove the session.
        """
        CreateTestData.delete()
        Session.remove()

    def test_controller(self):
        url = url_for(controller="ckanext.sitemap.controller:SitemapController", action='view')
        cont = self.app.get(url)
        self.assert_(cont.response.status == "200 OK")

