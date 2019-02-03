import os

import testinfra
import testinfra.utils.ansible_runner
import xmlunittest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

host = testinfra.get_host('docker://' + os.environ['TARGET_HOST'])

config = host.file(
    "/var/lib/jenkins/jenkins.model.JenkinsLocationConfiguration.xml"
)


class LocationConfigXmlTest(xmlunittest.XmlTestCase):

    def test_config_exists(self):
        assert config.exists

    def test_config_is_valid_xml(self):
        self.assertXmlDocument(config.content)

    def test_adminAddress_value(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './adminAddress/text()',
            ("admin@example.com")
        )

    def test_jenkinsUrl_value(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './jenkinsUrl/text()',
            ("http://localhost:8080")
        )
