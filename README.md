
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3591** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|128|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|128|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|128|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|262|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|195|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1851|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.76.13.167|59394|United States|Piscataway|The Constant Company|
|2|155.138.232.110|59394|United States|Atlanta|The Constant Company|
|3|45.76.13.167|59394|United States|Piscataway|The Constant Company|
|4|144.217.75.65|8800|Canada|Beauharnois|OVH SAS|
|5|88.84.209.24|3128|Russia|Elektrostal|Flex Ltd.|
|6|45.63.69.252|59394|United States|Elk Grove Village|The Constant Company|
|7|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|8|200.7.10.158|8080|Brazil|Itumbiara|Conexao Telematica LTDA|
|9|102.223.49.74|8080|Chad|N'Djamena|SOCIETE DIGITAL COM SA/AG|
|10|155.138.232.110|59394|United States|Atlanta|The Constant Company|
|11|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|12|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|13|38.130.249.129|999|United States|Dallas|Cogent Communications|
|14|45.63.69.252|59394|United States|Elk Grove Village|The Constant Company|
|15|160.226.240.213|8080|South Africa|Bloemfontein|Iclix (PTY) Ltd|
|16|186.96.116.12|999|Colombia|Flandes|TV AZTECA SUCURSAL COLOMBIA|
|17|103.209.36.56|8080|India|Mumbai|Syscon Infoway Pvt. Ltd.|
|18|181.224.207.20|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|19|190.181.16.206|999|Bolivia|La Paz|AXS Bolivia S. A.|
|20|138.0.89.154|999|Colombia|Belén|Dobleclick Software E Ingeneria|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

