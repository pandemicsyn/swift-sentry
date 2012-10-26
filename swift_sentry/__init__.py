import eventlet
import logging

def sentry_logger(conf, name, log_to_console, log_route, fmt, logger,
                  adapted_logger):
    sentry_dsn = conf.get('log_sentry_dsn', None)
    sentry_log_level = getattr(logging,
                               conf.get('log_sentry_level',
                                        'ERROR').upper(),
                               logging.ERROR)
    if sentry_dsn:
        raven_logging = eventlet.import_patched('raven.handlers.logging')
        sentry = raven_logging.SentryHandler(sentry_dsn)
        sentry.setLevel(sentry_log_level)
        logger.addHandler(sentry)
