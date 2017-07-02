import xmlrpc.client, pprint, logging, settings

logger = logging.getLogger('gandi')
pp = pprint.PrettyPrinter(indent=4)

def shouldUpdateWanV4Address(wanV4Adress):
    api = xmlrpc.client.ServerProxy(settings.GANDI_XMLRPC_URL)
    logger.debug(api.version.info(settings.GANDI_API_KEY))
    logger.debug(pp.pformat(api.domain.zone.list(settings.GANDI_API_KEY)))

    A_records = api.domain.zone.record.list(settings.GANDI_API_KEY, settings.GANDI_ZONE_ID, 0, { 'type' : ['A']})
    logger.debug(pp.pformat(A_records))

    for A_record in A_records:
        if A_record['value'] != wanV4Adress:
            logger.info('wan v4 address' + wanV4Adress + 'mismatch with zone record' + A_record)
            return True

    return False

def doUpdateWanV4Address(wanV4Adress):
    api = xmlrpc.client.ServerProxy(settings.GANDI_XMLRPC_URL)
    logger.debug(api.version.info(settings.GANDI_API_KEY))

    new_version_id = api.domain.zone.version.new(settings.GANDI_API_KEY, settings.GANDI_ZONE_ID)
    new_A_records = api.domain.zone.record.list(settings.GANDI_API_KEY, settings.GANDI_ZONE_ID, new_version_id, { 'type' : ['A']})
    
    for new_A_record in new_A_records:
        api.domain.zone.record.update(
            settings.GANDI_API_KEY,
            settings.GANDI_ZONE_ID,
            new_version_id,
            {
                'id': new_A_record['id']
            },
            {
                'name': new_A_record['name'],
                'type': new_A_record['type'],
                'value': wanV4Adress,
                'ttl': new_A_record['ttl']
            }
        )

    api.domain.zone.version.set(settings.GANDI_API_KEY, settings.GANDI_ZONE_ID, new_version_id)

    
