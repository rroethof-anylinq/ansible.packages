def test_htop_is_installed(host):
    pkg = host.package("htop")

    assert pkg.is_installed