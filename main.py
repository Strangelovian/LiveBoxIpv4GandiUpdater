import logging, settings, livebox, gandi

settings.init()

logger = logging.getLogger('updatewan')

ipv4WanAddress = livebox.V4WanAddress()

if ipv4WanAddress != None:
    if gandi.shouldUpdateWanV4Address(ipv4WanAddress):
        logger.info('zone update is needed')
        gandi.doUpdateWanV4Address(ipv4WanAddress)
    else:
        logger.info('zone is up to date')
else:
    logger.error('cannot retrieve livebox wan v4 address')

