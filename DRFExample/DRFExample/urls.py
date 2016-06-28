""" Add DRFExample urls here """

from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'DRFExample.views.home', name='home'),
    url(r'^page2/$', 'DRFExample.views.page2', name='page2'),
]

# mio_portal will automatically find and include these urls
AUTO_INCLUDE = True

# You can specify a different url namespace here (defaults to 'DRFExample' if not provided).
# namespace = 'DRFExample'

# You can specify a different root url here (defaults to 'DRFExample' if not provided).
# root_url = 'MOR/DRFExample'
