SOURCES = [
    {
        "id": "free-proxy-list.net",
        "url": "https://free-proxy-list.net",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "us-proxy.org",
        "url": "https://www.us-proxy.org",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxydb.net",
        "url": "http://proxydb.net",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": None,
                "port": None,
                "combined": "Proxy",
            },
        }
    },
    {
        "id": "free-proxy-list.com",
        "url": "https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 1,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxy-list.download",
        "url": "https://www.proxy-list.download/HTTP",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "vpnoverview.com",
        "url": "https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxyscan.io",
        "url": "https://www.proxyscan.io",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "Ip Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxylist.geonode.com",
        "url": "https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https",
        "method": "GET",
        "parser": {
            "json": {
                "data": "data",
                "ip": "ip",
                "port": "port",
            },
        }
    },
    {
        "id": "proxyscrape.com",
        "url": "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/clarketm/proxy-list",
        "url": "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
]
