---
title: http://any23.apache.org/build-src.html
source_url: http://any23.apache.org/build-src.html
date_collected: '2025-06-19'
license: Fair Use
---

This project has retired. For details please refer to its
[Attic page](https://attic.apache.org/projects/any23.html).








Apache Any23 – Apache Any23 - Build from sources



[![Apache Any23: Anything to Triples](images/logo-any23.png)](index.html)

[![Apache Any23](http://www.apache.org/images/feather-small.gif)](http://www.apache.org/)

---

* [Apache](https://www.apache.org/ "Apache")/
* [Any23](index.html "Any23")/
* Apache Any23 - Build from sources [![](./images/accessories-text-editor.png "Edit")](https://github.com/apache/any23/tree/master/src/site/apt/build-src.apt)
* | Last Published: 2022-03-03
* Version: 2.8-SNAPSHOT

* Apache Any23
* [Introduction](index.html "Introduction")
* [Downloads](download.html "Downloads")
* [Install](install.html "Install")
* Documentation
* [Getting Started](getting-started.html "Getting Started")
* [Supported Formats](supported-formats.html "Supported Formats")
* [Extractors](extractors.html "Extractors")
* [Configuration](configuration.html "Configuration")
* [REST Service](service.html "REST Service")
* [Any23 Plugins](any23-plugins.html "Any23 Plugins")
* [APIs Doc](apidocs/index.html "APIs Doc")
* [Developers Guide](developers.html "Developers Guide")
  + [Build from sources](#)
  + [Data Extraction](dev-data-extraction.html "Data Extraction")
  + [Data Conversion](dev-data-conversion.html "Data Conversion")
  + [Validation and Fixing](dev-validation-fix.html "Validation and Fixing")
  + [XPath Extractor](dev-xpath-extractor.html "XPath Extractor")
  + [Microformat Extractors](dev-microformat-extractors.html "Microformat Extractors")
  + [Microdata Extractor](dev-microdata-extractor.html "Microdata Extractor")
  + [CSV Extractor](dev-csv-extractor.html "CSV Extractor")
  + [HowTo Release](release-howto.html "HowTo Release")
* Project Documentation
* [Project Information](project-info.html "Project Information")
* [Project Reports](project-reports.html "Project Reports")
* Misc
* [Acknowledgements](acknowledgements.html "Acknowledgements")
* [PoweredBy](poweredby.html "PoweredBy")
* ASF
* [How Apache Works](http://www.apache.org/foundation/how-it-works.html "How Apache Works")
* [Foundation](http://www.apache.org/foundation/ "Foundation")
* [Sponsoring Apache](http://www.apache.org/foundation/sponsorship.html "Sponsoring Apache")
* [Thanks](http://www.apache.org/foundation/thanks.html "Thanks")

---

[![Built by Maven](./images/logos/maven-feather.png)](http://maven.apache.org/ "Built by Maven")



## Build Apache Any23 from sources

This page describes how to build **Apache Any23**.

### Access a Snapshot Version

For the latest snapshot please checkout the code from the public Git repository and build the library. Checkout the code from Github:

```
$ git clone https://github.com/apache/any23.git
```

### Build **Apache Any23**

The following instructions describe how to build the library with [Maven 3.x.y+](http://maven.apache.org/). For specific information about Maven see:  Go to the any23 folder:

```
$ cd any23/
```

and execute the following command:

```
any23$ mvn clean install
```

This will install the **Apache Any23** artifact and its dependencies in your local M2 repository.

### Generate Documentation

To generate the project site locally execute the following command from the any23 dir:

```
any23$ MAVEN_OPTS='-Xmx1024m' mvn clean site
```

You can speed up the site generation process specifying the offline option ( -o ), but it works only if all the involved plugin dependencies has been already downloaded in the local M2 repository:

```
any23$ MAVEN_OPTS='-Xmx1024m' mvn -o clean site
```

If you're interested in generating the Javadoc enriched with navigable UML graphs, you can activate the umlgraphdoc profile. This profile relies on [Graphviz](http://www.graphviz.org/) that must be installed in your system.

```
any23$ MAVEN_OPTS='-Xmx256m' mvn -P umlgraphdoc clean site
```

---



Apache Any23, Apache, the Apache feather logo, and the Apache Any23 project logos are trademarks of The Apache Software Foundation. All other marks mentioned may be trademarks or registered trademarks of their respective owners.
