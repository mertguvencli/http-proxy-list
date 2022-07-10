
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3598** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|509|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|509|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|509|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|0|🚫|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|211|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|117|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1913|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|5|45.152.188.246|3128|United States|Ashburn|Sprint|
|6|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|7|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|8|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|9|181.78.12.46|7070|Colombia|Chapinero|IFX Networks Argentina S.R.L|
|10|191.97.60.126|999|Peru|Chiclayo|Internexa Peru S.A|
|11|157.185.145.59|59394|United States|Los Angeles|Quantil Networks Inc|
|12|178.124.189.174|3128|Belarus|Minsk|Republican Unitary Telecommunication Enterprise Beltelecom|
|13|45.184.73.114|40033|Brazil|Queimadas|A2 TELECOM PROVEDOR DE INTERNET LTDA|
|14|152.32.218.99|8000|Singapore|Singapore|UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED|
|15|190.85.253.142|8080|Colombia|Bogotá|Telmex Colombia S.A.|
|16|195.154.70.151|3128|France|Paris|Online S.A.S.|
|17|45.172.108.41|999|Argentina|Caucete|GPS SANJUAN SRL.|
|18|101.51.243.157|8080|Thailand|Ban Ang Sila|TOT Public Company Limited|
|19|36.90.62.119|8080|Indonesia|Blitar|PT. Telekomunikasi Indonesia|
|20|80.235.9.243|3128|Estonia|Viimsi|Telia Eesti AS|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

