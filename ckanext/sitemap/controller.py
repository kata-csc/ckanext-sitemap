'''
Controller for sitemap
'''
import logging

from ckan.lib.base import BaseController
from ckan.model import Session, Package
from ckan.lib.helpers import url_for
from lxml import etree
from pylons import config, response
from pylons.decorators.cache import beaker_cache

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

XHTML_NS = "http://www.w3.org/1999/xhtml"

log = logging.getLogger(__file__)

locales = config.get('ckan.locales_offered', '').split()


class SitemapController(BaseController):

    @staticmethod
    def _create_language_alternatives(link, url):
        '''
        Create links (elements) for every language in locales_offered in .ini file
        :param link: string containing the link, eg. /dataset/xyz
        :param url: root node
        '''
        for lang in locales:
            attrib = {"rel": "alternate", "hreflang": lang, "href":
                      config.get('ckan.site_url') + '/' + lang + link}
            etree.SubElement(url, '{http://www.w3.org/1999/xhtml}link', attrib)

    @beaker_cache(expire=3600*24, type="dbm", invalidate_on_startup=True)
    def _render_sitemap(self):
        root = etree.Element("urlset", nsmap={None: SITEMAP_NS, 'xhtml': XHTML_NS})
        pkgs = Session.query(Package).filter(Package.type=='dataset').filter(Package.private!=True).\
            filter(Package.state=='active').all()
        log.debug(pkgs)
        for pkg in pkgs:
            url = etree.SubElement(root, 'url')
            loc = etree.SubElement(url, 'loc')
            pkg_url = url_for(controller='package', action="read", id=pkg.name)
            loc.text = config.get('ckan.site_url') + pkg_url
            lastmod = etree.SubElement(url, 'lastmod')
            lastmod.text = pkg.latest_related_revision.timestamp.strftime('%Y-%m-%d')
            self._create_language_alternatives(pkg_url, url)
            for res in pkg.resources:
                url = etree.SubElement(root, 'url')
                loc = etree.SubElement(url, 'loc')
                loc.text = config.get('ckan.site_url') + url_for(controller="package", action="resource_read",
                                                                 id=pkg.name, resource_id=res.id)
                lastmod = etree.SubElement(url, 'lastmod')
                self._create_language_alternatives(url_for(controller="package", action="resource_read",
                                                           id=pkg.name, resource_id=res.id), url)
                lastmod.text = res.created.strftime('%Y-%m-%d')
        response.headers['Content-type'] = 'text/xml'
        return etree.tostring(root, pretty_print=True)

    def view(self):
        return self._render_sitemap()

