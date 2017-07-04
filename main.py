import logging, argparse, settings, livebox, gandi

parser = argparse.ArgumentParser(description='ipv4 wan address updater')
parser.add_argument('--rc-file', help='path to the resource configuration file location', required=True)
args = parser.parse_args()

settings.init(args.rc_file)

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

