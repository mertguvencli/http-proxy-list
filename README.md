
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3631** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|172|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|172|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|172|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|363|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|266|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1919|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|66.42.125.237|59394|United States|Elk Grove Village|The Constant Company|
|2|95.217.207.66|3128|Finland|Helsinki|Hetzner Online GmbH|
|3|66.42.125.237|59394|United States|Elk Grove Village|The Constant Company|
|4|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|5|203.150.113.41|8080|Thailand|Bangkok|Internet Thailand Company Ltd.|
|6|110.78.147.151|8080|Thailand|Ko Samui|CAT-BB|
|7|203.150.128.223|8080|Thailand|Watthana|Internet Thailand Company Ltd|
|8|103.6.11.138|9812|Cambodia|Kampong Thom|Telecom Cambodia (T.C.)|
|9|5.35.82.110|32132|Russia|Pushkino|INFOLINE|
|10|102.130.79.1|3128|South Africa|Johannesburg|Adnexus Celerity Networks (Proprietary) Limited|
|11|102.68.128.215|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|
|12|194.233.73.106|443|Singapore|Singapore|Contabo Asia Private Limited|
|13|200.52.148.194|999|Honduras|San Pedro Sula|Redes y Telecomunicaciones|
|14|66.42.125.237|59394|United States|Elk Grove Village|The Constant Company|
|15|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|16|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|17|194.233.69.41|443|Singapore|Singapore|Contabo Asia Private Limited|
|18|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|19|129.215.41.142|3128|United Kingdom|Edinburgh|University of Edinburgh|
|20|186.248.89.6|5005|Brazil|Ibirite|AMERICAN TOWER DO BRASIL-COMUNICA??O MULTIM?DIA LT|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

