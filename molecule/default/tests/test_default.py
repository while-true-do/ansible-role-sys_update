import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dep_pkg(host):
    if host.system_info.distribution == "CentOS":
        pkg = host.package('yum-utils')

        assert pkg.is_installed

    if host.system_info.distribution == "RedHat":
        pkg = host.package('yum-utils')

        assert pkg.is_installed

    if host.system_info.distribution == "Fedora":
        pkg = host.package('tracer')

        assert pkg.is_installed
