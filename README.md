
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4123** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|406|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|406|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|406|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|469|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|384|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1987|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|66.196.238.178|3128|United States|Tomball|Logix|
|4|89.223.8.10|3128|Russia|St Petersburg|United Networks Ltd.|
|5|203.223.44.146|9812|Cambodia|Phnom Penh|Telecom Cambodia (T.C.)|
|6|186.96.100.61|999|Colombia|Bogotá|TV AZTECA SUCURSAL COLOMBIA|
|7|103.178.43.2|8181|Indonesia|Jakarta|PT Jaring Solusi Persada|
|8|194.233.86.75|7777|Singapore|Singapore|Contabo Asia Private Limited|
|9|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|10|178.93.59.48|8080|Ukraine|Kyiv|UKRTELECOM|
|11|183.81.156.130|8080|Indonesia|Kayu Manis|Internet Service Provider|
|12|103.66.196.218|23500|Indonesia|Bogor|PT. Mora Telematika Indonesia|
|13|5.9.201.70|3128|Germany|Falkenstein|Hetzner Online GmbH|
|14|159.65.133.175|31280|Singapore|Singapore|DigitalOcean, LLC|
|15|95.217.207.66|3128|Finland|Helsinki|Hetzner Online GmbH|
|16|181.209.124.10|999|Argentina|Benavidez|ARSAT - Empresa Argentina de Soluciones Satelitales S.A|
|17|129.159.138.196|8080|Israel|Jerusalem|Oracle Corporation|
|18|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|19|194.5.25.34|443|Singapore|Singapore|Mod Mission Critical LLC|
|20|187.94.211.60|8080|Brazil|Alto Caparao|Acesse Comunica??o Ltda|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

