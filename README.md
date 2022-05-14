
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3881** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|209|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|209|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|209|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|452|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|301|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2045|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|145.40.68.200|10000|Netherlands|Amsterdam|Packet Host, Inc.|
|3|102.130.79.1|3128|South Africa|Johannesburg|Adnexus Celerity Networks (Proprietary) Limited|
|4|171.6.73.89|8080|Thailand|Bang Lamung|Triple T Broadband Public Company Limited|
|5|175.136.8.148|3128|Malaysia|Marabu|Tmnet, Telekom Malaysia Bhd.|
|6|62.78.84.219|3128|Russia|Kalachinsk|LLC Milecom|
|7|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|8|176.56.107.234|33911|Spain|Elche|Aire Networks|
|9|185.135.193.38|3128|Poland|Lodz|M3.NET Sp. zoo Sp. K.|
|10|91.208.184.19|3128|Moldova|Chisinau|Alexhost SRL|
|11|210.245.52.58|8080|Vietnam|Hanoi|FPT Telecom Company|
|12|45.5.57.122|8080|Peru|Jesus Maria|Satelital Telecomunicaciones S.A.C|
|13|165.90.225.15|3389|South Africa|Roodepoort|MIA Telecoms|
|14|167.172.239.13|3128|United States|Clifton|DigitalOcean, LLC|
|15|201.174.239.18|8080|Mexico|Ciudad Juárez|Transtelco Inc|
|16|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|17|95.217.207.66|3128|Finland|Helsinki|Hetzner Online GmbH|
|18|183.88.177.96|8080|Thailand|Ban Du Phong|Triple T Broadband Public Company Limited|
|19|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|20|85.195.104.71|80|Germany|Frankfurt am Main|Host Europe GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

