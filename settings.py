import logging, logging.handlers, configparser, sys, os

def init(rcfile):
    global GANDI_API_KEY, GANDI_ZONE_ID, GANDI_XMLRPC_URL

    try:
        config = configparser.ConfigParser()
        config.read(rcfile)
        GANDI_API_KEY = config['gandi']['api_key']
        GANDI_ZONE_ID = int(config['gandi']['zone_id'])
        GANDI_XMLRPC_URL = config['gandi']['xml_rpc_url']
        
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
        
        splat = os.path.splitext(config['log']['path'])
        handler = logging.handlers.RotatingFileHandler(splat[0] + ".debug" + splat[1], maxBytes=10*1024, backupCount=10)
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)
        root.addHandler(handler)
        
        handler = logging.handlers.RotatingFileHandler(config['log']['path'], maxBytes=10*1024, backupCount=1)
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)
        root.addHandler(handler)
        
    except:
        print('init error:', sys.exc_info()[0])
        raise
