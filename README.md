# This repository was part of an older version of Etsin which is no longer in use. For the newest version of Etsin, see https://github.com/CSCfi/etsin-finder/

Sitemap is a CKAN extension which will provide sitemap.xml which will inform search engines about available
URLs. Note that this extension doesn't provide any modifications to robots.txt provided by CKAN so without any
modifications the URL exclusion provided by robots.txt is in use.

The extension has been tested with CKAN 2.4.1


Installation
============

Activate your CKAN virtualenv:

    source /usr/lib/ckan/default/bin/activate

Install ckanext-sitemap:

    pip install -e git://github.com/kata-csc/ckanext-sitemap.git#egg=ckanext-sitemap

Install its dependencies (you will also need the `libxml2` and `libxslt` C libraries):

    pip install -r /usr/lib/ckan/default/src/ckanext-sitemap/requirements.txt

Add ckanext-sitemap to your CKAN configuration file (e.g. `/etc/ckan/default/production.ini`):

    ckan.plugins = ... sitemap

Finally, restart CKAN:

    sudo service apache2 restart


Usage
=====

Once installation is complete and you have restarted CKAN the sitemap will be available at `/sitemap.xml`.

