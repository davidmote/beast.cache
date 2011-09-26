import unittest2 as unittest
from beast.cache.testing import BEASTCACHE_POLICY_INTEGRATION_TESTING
from plone.app.testing import applyProfile

from Products.CMFCore.utils import getToolByName

class TestSetup(unittest.TestCase):
    
    layer = BEASTCACHE_POLICY_INTEGRATION_TESTING

    def test_should_fail(self):
        self.fail()