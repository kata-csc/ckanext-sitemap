'''
Sitemap plugin for CKAN
'''

from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IRoutes

class SitemapPlugin(SingletonPlugin):
    implements(IRoutes, inherit=True)

    def before_map(self, map):
        controller='ckanext.sitemap.controller:SitemapController'
        map.connect('sitemap', '/sitemap', controller=controller, action='view')
        return map
        
