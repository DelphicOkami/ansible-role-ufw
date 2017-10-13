import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ufw_installed(host):
    ufw = host.package("ufw")
    assert ufw.is_installed


def test_ufw_is_enabled(host):
    ufw = host.service("ufw")
    assert ufw.is_enabled
