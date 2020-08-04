## A2A


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

A2A(Azure to AWS or AWS to Azure) is a cli tool that provides you service mappings for the most of the cloud offerings across the platforms.

As a DevOps/SRE engineer who works multi-cloud, this handy tool gives the correct service mappings between Azure and AWS.
This can be pretty useful who is new to any of the clouds or coming from experience with a specific cloud .

# Features!

  - Enter the service name and voila the corresponding service in the appropriate cloud platform is shown
  - Service name can be from any platform(AWS/Azure)
  - Don't need to go to https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services everytime to check for mappings

### Tech

A2A uses a number of open source projects to work properly:

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

$ a2a "Codebuild"
SERVICE        URL                                    CORRESPONDING SERVICES    CORRESPONDING URLS
-------------  -------------------------------------  ------------------------  ------------------------------------------------
['CodeBuild']  ['https://aws.amazon.com/codebuild/']  ['DevOps']                ['https://azure.microsoft.com/services/devops/']
```

### Development

Want to contribute? Great! Feel free to open an PR.

### Todos

 - Write Tests
 - Add Support for GCP ( https://cloud.google.com/docs/compare/azure )

License
----

MIT


**Free Software, Hell Yeah!**
