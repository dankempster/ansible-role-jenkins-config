import os

import testinfra
import testinfra.utils.ansible_runner
import xmlunittest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_git_plugin_is_installed(host):
    f = host.file('/var/lib/jenkins/plugins/git.jpi')

    assert f.exists


host = testinfra.get_host('docker://' + os.environ['TARGET_HOST'])

config = host.file(
    "/var/lib/jenkins/hudson.plugins.git.GitSCM.xml"
)


class GitConfigTest(xmlunittest.XmlTestCase):

    def test_git_config_name(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './globalConfigName/text()',
            ("John Smith")
        )

    def test_git_config_email(self):
        self.assertXpathValues(
            self.assertXmlDocument(config.content),
            './globalConfigEmail/text()',
            ("john@example.com")
        )
