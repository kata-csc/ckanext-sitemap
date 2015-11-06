Sitemap is a CKAN extension which will provide sitemap.xml which will inform search engines about available
URLs. Note that this extension doesn't provide any modifications to robots.txt provided by CKAN so without any
modifications the URL exclusion provided by robots.txt is in use.

Installation
============

You can install the extension with:

`pip install -e git://github.com/kata-csc/ckanext-sitemap.git#egg=ckanext-sitemap`

Requirements
============

* libxml2 and libxslt C libraries prior to installation

* Tested with CKAN 2.4.1