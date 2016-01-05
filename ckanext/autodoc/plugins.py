#!/usr/bin/env python
# encoding: utf-8
import ckan.plugins as p


class AutodocPlugin(p.SingletonPlugin):
    p.implements(p.IRoutes)
    p.implements(p.IConfigurer)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')

    def before_map(self, map):
        map.connect(
            'list',
            '/api/current/list',
            controller='ckanext.autodoc.controllers:APIExtController',
            action='list'
        )

        return map

    def after_map(self, map):
        # Required by the IRoutes interface.
        return map
