## A2A

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A2A(Azure to AWS or AWS to Azure) is a cli tool that provides you service mappings for the most of the cloud offerings across the platforms.

# New Features!

  - Enter the service name and voila the corresponding service is output
  - Drag and drop images (requires your Dropbox account be linked)

### Tech

Dillinger uses a number of open source projects to work properly:

* [Python] - Oh surprise!
* [Scrappy] - Python based scraping utility


### Installation

```sh
$ pip install a2a
```

## Usage
```sh
$ a2a "Firewall"
SERVICE       URL                                                       CORRESPONDING SERVICES        CORRESPONDING URLS
------------  --------------------------------------------------------  ----------------------------  -------------------------------
['Firewall']  ['https://azure.microsoft.com/services/azure-firewall/']  ['Web Application Firewall']  ['https://aws.amazon.com/waf/']
```
### Development

Want to contribute? Great! Feel free to open an PR.

### Todos

 - Write Tests
 - Add Support for GCP

License
----

MIT


**Free Software, Hell Yeah!**
