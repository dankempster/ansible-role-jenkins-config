import os

import testinfra
import testinfra.utils.ansible_runner
import xmlunittest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

host = testinfra.get_host('docker://' + os.environ['TARGET_HOST'])

config = host.file("/var/lib/jenkins/config.xml")

class MyTest(xmlunittest.XmlTestCase):

    def test_config_exists(self):
        assert config.exists

    def test_config_is_valid_xml(self):
        self.assertXmlDocument(config.content)

    def test_numExecutors_value(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './numExecutors/text()',
            ("2")
        )

    def test_useSecurity_value(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './useSecurity/text()',
            ("true")
        )

    def test_denyAnonymousReadAccess_value(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './authorizationStrategy/denyAnonymousReadAccess/text()',
            ('false')
        )

    def test_securityRealm_disableSignup_value(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './securityRealm/disableSignup/text()',
            ('true')
        )

    def test_securityRealm_enableCaptcha_value(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './securityRealm/enableCaptcha/text()',
            ('false')
        )

    def test_disableRememberMe_value(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './disableRememberMe/text()',
            ('false')
        )
