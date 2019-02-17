import os

import testinfra
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_git_plugin_is_installed(host):
    f = host.file('/var/lib/jenkins/jobs/seed-job.xml')

    assert not f.exists
