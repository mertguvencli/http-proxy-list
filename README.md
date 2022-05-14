
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3603** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|215|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|215|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|215|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|354|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|312|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1854|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|2|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|3|176.119.134.142|23500|Spain|Puerto Serrano|Electro Puerto SUR SL|
|4|62.78.84.219|3128|Russia|Kalachinsk|LLC Milecom|
|5|185.83.144.222|3128|Turkey|Merkezefendi|Netinternet Datacenter|
|6|188.0.147.102|3128|Kazakhstan|Almaty|JSC "KazTransCom"|
|7|185.135.193.38|3128|Poland|Lodz|M3.NET Sp. zoo Sp. K.|
|8|46.246.84.5|8080|Sweden|Stockholm|Portlane Network|
|9|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|10|5.53.16.185|18080|Russia|Surgut|Metroset Ltd|
|11|181.224.207.21|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|12|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|13|203.76.114.197|8080|Bangladesh|Dhaka|Link3 Technologies Limited|
|14|167.172.239.13|3128|United States|Clifton|DigitalOcean, LLC|
|15|66.117.2.68|3128|United States|Los Angeles|Corporate Colocation Inc|
|16|66.117.2.126|3128|United States|Los Angeles|Corporate Colocation Inc|
|17|102.130.79.1|3128|South Africa|Johannesburg|Adnexus Celerity Networks (Proprietary) Limited|
|18|139.99.88.19|8080|Singapore|Singapore|OVH SAS|
|19|190.8.39.182|8080|Dominican Republic|Santo Domingo Este|Trilogy Dominicana, S.A.|
|20|45.189.254.10|999|Mexico|Alvarado|Tracered SA De CV|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

