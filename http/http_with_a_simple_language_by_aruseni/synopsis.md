# HTTP with a simple language. *By aruseni*

[Source](https://habr.com/ru/post/215117/)


## Acronyms

* HTTP - HyperText Transport Protocol.
* HTTPS - HyperText Transfer Protocol Secure.
* URI - Uniform Resource Identifier.


## References

* [RFC2616 Specification](https://tools.ietf.org/html/rfc2616)


## Futher reading

* [OSI](https://en.wikipedia.org/wiki/OSI_model)
* SOAP
* XML-RPC
* WebDAV
* REST
* HTTPS
* SSL
* TLS


HTTP (HyperText Transport Protocol) is protocol initially intended for transfering hypertext documents. It is an application-layer protocol (high or 7th layer) according to OSI. Current protocol version is 1.1, specification is RFC2616. HTTP is used as a transport for other apllied protocols: SOAP, XML-RPC and WebDAV. Many API are using HTTP for transfering data in any format, e.g. XML or JSON. HTTP works over TCP/IP connection and uses 80 TCP port by default or any other TCP port if desired.


## Request

Request cosists of two parts: start string and headers.

```
Method URI HTTP/Version
Header: Value
...
Header: Value
```

* `Method` - any string according to HTTP 1.1 specification, but most of cases standart names are used, like `GET` and `POST`.  
* `URI` (Uniform Resource Identifier) - path to document or asterisk symbol (*) if not applicable.  
* `Version` - HTTP protocol version.  
* `Header` - Header name. Header `Host` is only one required header. It is used by the server to understand what address is used to connect. It is required because the server doesn't know what the connection address was, but it can serve a number of sites with different addresses (domain names).  
* `Value` - Header value.

Connect with PuTTy on Windows 10 with following settings:
* Host Name: `google.com`.
* Port: `80`.
* Connection type: `Raw`.
* Close window on exit: `Never`.

```
GET / HTTP/1.1
Host: www.google.com

```

Carriage Return (CR, \r) and Line Feed (LF, \n) symbols are used in the end of each line. After last header these symbols go twice.


## Response

```
HTTP/Version Status Code Reason Phrase
Header: Value
...
Header: Value

Body

```

* `Version` - HTTP protocol version.
* `Status Code` - Code of three numbers, like `200`.
* `Code Reason` - Status Code explanation.
* `Header` - Header name.
* `Value` - Header value.
* `Body` - Body content.

HTTPS (HyperText Transfer Protocol Secure) - secure extension of HTTP protocol to pack transfering data into SSL or TLS protocols. It uses 443 TCP port by default.
