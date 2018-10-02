

class Endpoints:
    # This class contains a list of the REQUIRED keyword arguments for each API url endpoint that's implemented.
    def __init__(self):
        # Currently only GET request endpoints are supported
        # TODO: Add endpoints for POST, PUT, DELETE requests and implement them in grapi.py
        self._endpoints = {
            "/api/alerts/callbacks": [],
            "/api/alerts/callbacks/types": [],
            "/api/alerts/conditions": [],
            "/api/alerts/conditions/types": [],
            "/api/streams/alerts": [],
            "/api/streams/alerts/paginated": ["skip", "limit"],
            "/api/cluster": [],
            "/api/cluster/inputstates": [],
            "/api/cluster/jobs": [],
            "/api/cluster/system/loggers": [],
            "/api/cluster/system/loggers/subsystems": [],
            "/api/count/total": [],
            "/api/dashboards": [],
            "/api/api-docs": [],
            "/api/filters/blacklist": [],
            "/api/system/indexer/cluster/health": [],
            "/api/system/indexer/cluster/name": [],
            "/api/system/indexer/failures": [],
            "/api/system/indexer/failures/count": [],
            "/api/system/indexer/indices": [],
            "/api/system/indexer/indices/closed": [],
            "/api/system/indexer/indices/open": [],
            "/api/system/indexer/indices/reopened": [],
            "/api/system/indexer/overview": [],
            "/api/roles": [],
            "/api/search/universal/absolute": ["query", "from", "to", "fields"],
            "/api/search/universal/absolute/export": ["query", "from", "to", "fields"],
            "/api/search/universal/absolute/fieldhistogram": ["query", "from", "to", "field", "interval"],
            "/api/search/universal/absolute/histogram": ["query", "from", "to", "interval"],
            "/api/search/universal/absolute/stats": ["query", "from", "to", "field"],
            "/api/search/universal/absolute/terms": ["query", "from", "to", "field"],
            "/api/search/universal/absolute/terms-histogram": ["query", "from", "to", "field", "size", "interval"],
            "/api/search/universal/absolute/termsstats": ["query", "from", "to", "order", "key_field", "value_field"],
            "/api/search/decorators": [],
            "/api/search/decorators/available": [],
            "/api/search/universal/keyword": ["query", "keyword", "fields"],
            "/api/search/universal/keyword/export": ["query", "keyword", "fields"],
            "/api/search/universal/keyword/fieldhistogram": ["query", "keyword", "field", "interval"],
            "/api/search/universal/keyword/histogram": ["query", "keyword", "interval"],
            "/api/search/universal/keyword/stats": ["query", "keyword", "field"],
            "/api/search/universal/keyword/terms": ["query", "keyword", "field"],
            "/api/search/universal/keyword/terms-histogram": ["query", "keyword", "field", "interval", "size"],
            "/api/search/universal/keyword/termsstats": ["query", "keyword", "order", "key_field", "value_field"],
            "/api/search/universal/relative": ["query", "range", "fields"],
            "/api/search/universal/relative/export": ["query", "range", "fields"],
            "/api/search/universal/relative/fieldhistogram": ["query", "range", "field", "interval"],
            "/api/search/universal/relative/histogram": ["query", "range", "interval"],
            "/api/search/universal/relative/stats": ["query", "range", "field"],
            "/api/search/universal/relative/terms": ["query", "range", "field"],
            "/api/search/universal/relative/terms-histogram": ["query", "range", "field", "size"],
            "/api/search/universal/relative/termsstats": ["query", "range", "order", "key_field", "value_field"],
            "/api/search/saved": [],
            "/api/sources": ["range"],
            "/api/streams": [],
            "/api/streams/enabled": [],
            "/api/system": [],
            "/api/system/jvm": [],
            "/api/system/locales": [],
            "/api/system/threaddump": [],
            "/api/system/authentication/config": [],
            "/api/system/bundles": [],
            "/api/system/cluster/node": [],
            "/api/system/cluster/nodes": [],
            "/api/system/cluster_config": [],
            "/api/system/cluster/stats": [],
            "/api/system/cluster/stats/elasticsearch": [],
            "/api/system/cluster/stats/mongo": [],
            "/api/system/cluster/traffic": [],
            "/api/system/codecs/types/all": [],
            "/api/system/configuration": [],
            "/api/system/debug/events/cluster": [],
            "/api/system/debug/events/local": [],
            "/api/system/deflector": [],
            "/api/system/fields": [],
            "/api/system/gettingstarted": [],
            "/api/system/grok": [],
            "/api/system/indices/ranges": [],
            "/api/system/indices/index_sets": ["skip", "limit"],
            "/api/system/indices/index_sets/stats": [],
            "/api/system/indices/retention/strategies": [],
            "/api/system/indices/rotation/strategies": [],
            "/api/system/inputstates": [],
            "/api/system/inputs": [],
            "/api/system/inputs/types": [],
            "/api/system/inputs/types/all": [],
            "/api/system/jobs": [],
            "/api/system/journal": [],
            "/api/system/ldap/groups": [],
            "/api/system/ldap/settings": [],
            "/api/system/ldap/settings/groups": [],
            "/api/system/lbstatus": [],
            "/api/system/loggers": [],
            "/api/system/loggers/messages/recent": [],
            "/api/system/loggers/subsystems": [],
            "/api/system/lookup/adapters": ["sort"],
            "/api/system/lookup/caches": ["sort"],
            "/api/system/lookup/tables": ["sort"],
            "/api/system/lookup/types/adapters": [],
            "/api/system/lookup/types/caches": [],
            "/api/system/messageprocessors/config": [],
            "/api/system/messages": [],
            "/api/system/metrics": [],
            "/api/system/metrics/names": [],
            "/api/system/notifications": [],
            "/api/system/outputs": [],
            "/api/system/outputs/available": [],
            "/api/system/permissions": [],
            "/api/system/plugins": [],
            "/api/system/serviceManager": [],
            "/api/system/sessions": [],
            "/api/system/stats": [],
            "/api/system/stats/fs": [],
            "/api/system/stats/jvm": [],
            "/api/system/stats/network": [],
            "/api/system/stats/os": [],
            "/api/system/stats/process": [],
            "/api/system/throughput": [],
            "/api/users": []
        }

    def check(self, keys, endpoint):
        print(endpoint)
        print(self._endpoints[endpoint])
        if not set(self._endpoints[endpoint]).issubset(set(keys)):
            raise ValueError("Minimum required arguments missing for this API endpoint.\n" +
                             "Given: {0}\n" +
                             "Required: {1}\n".format(keys, self._endpoints))
        else:
            return True
