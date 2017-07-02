import logging, configparser, sys, os

def init():
    global GANDI_API_KEY, GANDI_ZONE_ID, GANDI_XMLRPC_URL

    rc = os.path.expanduser("~") + "/" + ".updatewanv4rc"
    config = configparser.ConfigParser()

    try:
        config.read(rc)
        GANDI_API_KEY = config['gandi']['api_key']
        GANDI_ZONE_ID = int(config['gandi']['zone_id'])
        GANDI_XMLRPC_URL = config['gandi']['xml_rpc_url']
        logging.basicConfig(
            filename=config['log']['path'],
            format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
            level=logging.DEBUG)
    except:
        print('init error:', sys.exc_info()[0])
        raise
