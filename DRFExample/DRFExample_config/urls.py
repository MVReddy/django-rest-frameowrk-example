"""DRFExample URL Configuration

The `urlpatterns` list routes URLs to views.

This module will dynamically add the `urls` modules of all `INSTALLED_APPS` which specify `AUTO_INCLUDE = True`.
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from DRFExample import views
from importlib import import_module
import logging

LOGGER_NAME = 'DRFExample'


def add_urls_package(package, app_name, patterns):
    logger = logging.getLogger(LOGGER_NAME)
    logger.debug('Attempting to add url package from {app}'.format(app=app_name))
    try:
        module = import_module(package.__name__ + '.root_urls')
        logger.debug('root_urls found in url package')
    except:
        logger.error('Failed to add url package', exc_info=True)
        return
    add_urls_module(module, app_name, patterns)


def add_urls_module(module, app_name, patterns):
    auto_include = getattr(module, 'AUTO_INCLUDE', False)
    if auto_include:
        namespace = getattr(module, 'namespace', app_name)
        root_url = getattr(module, 'root_url', app_name)
        patterns.append(url(r'^{0}/'.format(root_url), include(module, namespace=namespace)))

        logger = logging.getLogger(LOGGER_NAME)
        logger.debug('{app} is using a module with namespace of {n}'.format(app=app_name, n=namespace))


def add_urls(app_name, patterns):
    try:
        urls_module = import_module(app_name + '.urls')
    except:
        if 'django.' not in app_name:
            logger = logging.getLogger(LOGGER_NAME)
            logger.error('No urls for {a}'.format(a=app_name), exc_info=True)
        return
    is_package = hasattr(urls_module, '__path__')
    if is_package:
        add_urls_package(urls_module, app_name, patterns)
    else:
        add_urls_module(urls_module, app_name, patterns)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('snippets.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

for app in settings.INSTALLED_APPS:
    add_urls(app, urlpatterns)
