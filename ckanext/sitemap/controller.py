'''
Controller for sitemap
'''
import logging

from ckan.lib.base import BaseController
from ckan.model import Session, Package
from ckan.lib.helpers import url_for
from lxml import etree
from pylons import config

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

log = logging.getLogger(__file__)

class SitemapController(BaseController):

    def view(self):
        root = etree.Element("urlset", nsmap={None: SITEMAP_NS})
        pkgs = Session.query(Package).all()
        for pkg in pkgs:
            url = etree.SubElement(root, 'url')
            loc = etree.SubElement(url, 'loc')
            pkg_url = url_for(controller='package', action="read", id = pkg.name)
            loc.text = config.get('ckan.site_url') + pkg_url
            lastmod = etree.SubElement(url, 'lastmod')
            lastmod.text = pkg.latest_related_revision.timestamp.strftime('%Y-%m-%d')
            for res in pkg.resources:
                url = etree.SubElement(root, 'url')
                loc = etree.SubElement(url, 'loc')
                loc.text = config.get('ckan.site_url') + url_for(controller="package", action="resource_read", id = pkg.name, resource_id = res.id)
                lastmod = etree.SubElement(url, 'lastmod')
                lastmod.text = res.created.strftime('%Y-%m-%d')
        return etree.tostring(root, pretty_print=True)
