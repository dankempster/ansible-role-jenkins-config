import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_jenkins_is_configured(host):
    f = host.file('/var/lib/jenkins/config.xml')

    assert f.exists
    assert f.user == 'jenkins'
    assert f.group == 'jenkins'
    assert f.mode == 0644

def test_jenkins_location_is_configured(host):
    f = host.file('/var/lib/jenkins/jenkins.model.JenkinsLocationConfiguration.xml')

    assert f.exists
    assert f.user == 'jenkins'
    assert f.group == 'jenkins'
    assert f.mode == 0644

def test_jenkins_CLI_is_configured(host):
    f = host.file('/var/lib/jenkins/jenkins.CLI.xml')

    assert f.exists
    assert f.user == 'jenkins'
    assert f.group == 'jenkins'
    assert f.mode == 0644


def test_jenkins_Shell_is_configured(host):
    f = host.file('/var/lib/jenkins/hudson.tasks.Shell.xml')

    assert f.exists
    assert f.user == 'jenkins'
    assert f.group == 'jenkins'
    assert f.mode == 0644
