from setuptools import setup, find_packages

name = "swift-sentry"

setup(
    name = name,
    version = '0.0.1',
    license = 'Apache License (2.0)',
    description = 'Exception tracking for OpenStack Swift using Sentry',
    keywords = "openstack swift sentry",
    author = "Florian Hines",
    author_email = "syn@ronin.io",
    url='http://github.com/pandemicsyn/swift-sentry',
    packages = find_packages(),
    classifiers = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.6',
                   'Environment :: No Input/Output (Daemon)',
                   'Environment :: OpenStack',],
    install_requires = [],
    )
