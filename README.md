
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3425** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|131|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|131|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|131|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|284|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|204|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1854|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|3|185.105.108.208|8080|Netherlands|Amsterdam|Serverius|
|4|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|5|102.130.79.1|3128|South Africa|Johannesburg|Adnexus Celerity Networks (Proprietary) Limited|
|6|167.172.239.13|3128|United States|Clifton|DigitalOcean, LLC|
|7|190.8.39.182|8080|Dominican Republic|Santo Domingo Este|Trilogy Dominicana, S.A.|
|8|181.224.207.21|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|9|139.99.88.19|8080|Singapore|Singapore|OVH SAS|
|10|93.185.123.154|3128|Italy|Pove del Grappa|Omegacom S.R.L.S.|
|11|91.208.184.19|3128|Moldova|Chisinau|Alexhost SRL|
|12|185.83.144.222|3128|Turkey|Merkezefendi|Netinternet Datacenter|
|13|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|14|190.109.18.65|8080|Colombia|Medellín|Columbus Networks Colombia|
|15|125.25.32.131|8080|Thailand|Chiang Mai|TOT Public Company Limited|
|16|183.89.166.203|8080|Thailand|Bang Lamung|Triple T Broadband Public Company Limited|
|17|23.234.213.157|6666|United States|Santa Clarita|Multacom Corporation|
|18|183.88.177.96|8080|Thailand|Ban Du Phong|Triple T Broadband Public Company Limited|
|19|176.56.107.227|51528|Spain|Elche|Aire Networks|
|20|45.189.254.10|999|Mexico|Alvarado|Tracered SA De CV|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

