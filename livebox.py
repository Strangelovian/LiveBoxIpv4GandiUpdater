import http.client, urllib, json, logging

logger = logging.getLogger('livebox')

def V4WanAddress():
    params = '''{"service":"NMC","method":"getWANStatus","parameters":{}}'''
    headers = { "Content-type": "application/x-sah-ws-4-call+json" }
    conn = http.client.HTTPConnection("livebox")
    conn.request("POST", "/ws", params, headers)
    response = conn.getresponse()

    if response.getcode() == 200:
        liveBoxWanStatus = json.loads(response.read().decode('utf-8'))
        logger.debug(json.dumps(liveBoxWanStatus, sort_keys=True, indent=4))

        if 'data' in liveBoxWanStatus:
            data = liveBoxWanStatus['data']
            if 'IPAddress' in data:
                wanIpv4 = data['IPAddress']
                logger.info("wan ipv4: " + wanIpv4)
                return wanIpv4

    return None 
