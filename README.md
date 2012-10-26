# Swift Sentry

#### Exception tracking for OpenStack Swift deployments using [python-raven](https://github.com/getsentry/raven-python) and [Sentry](https://github.com/getsentry/sentry)

Using swift-sentry via Swift's custom log handler hook you can capture/track exceptions on a local Sentry instance or via [http://getsentry.com](http://getsentry.com) (if you don't wish to host your own Sentry server)

## Requirements

- Swift => 1.7.5
- python-raven => 2.7 (using the eventlet+http(s) transport)

## Configuration

Sentry support is enabled using the custom log handlers hook. To enable it for a service
(proxy-server, account-server, container-server, object-server, etc) simple add
the following lines to the [DEFAULT] (or a subsection) section of the config:

    log_custom_handlers = swift_sentry.sentry_logger
    # The sentry DSN to use - be sure to use an eventlet transport
    log_sentry_dsn = eventlet+http://3f712c8421d40fc:d8aff88e0e506@sentry.yourdomain.com:someport/2
    #Optionally change the log level at which entries are reported
    #log_sentry_level = ERROR

## Installation/Building packages

Installing via setup.py:

    git clone git@github.com/pandemicsyn/swift-sentry.git
    cd swift-sentry
    python setup.py install

Building a debian package with [stdeb](https://github.com/astraw/stdeb "stdeb"):

    git clone git@github.com:pandemicsyn/swift-sentry.git
    cd swift-sentry
    python setup.py --command-packages=stdeb.command bdist_deb
    dpkg -i deb_dist/python-swift-sentry_0.0.X-1_all.deb
    
