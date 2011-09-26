from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig

class beastCachePolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import beast.cache
        xmlconfig.file('configure.zcml', beast.cache, context=configurationContext)

BEASTCACHE_POLICY_FIXTURE = beastCachePolicy()
BEASTCACHE_POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(BEASTCACHE_POLICY_FIXTURE,), name="beastbrowser:Integration")