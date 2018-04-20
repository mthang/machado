# Copyright 2018 by Embrapa.  All rights reserved.
#
# This code is part of the machado distribution and governed by its
# license. Please see the LICENSE.txt and README.md files that should
# have been included as part of this package for licensing information.

"""URLs."""

from machado import views
from django.conf.urls import include, url
from rest_framework_nested import routers
from rest_framework.documentation import include_docs_urls

router = routers.SimpleRouter()
router.register(r'organism', views.OrganismViewSet, base_name='organism')
router.register(r'cv', views.CvViewSet, base_name='cv')
router.register(r'cvterm', views.CvtermViewSet, base_name='cvterm')
router.register(r'db', views.DbViewSet, base_name='db')
router.register(r'dbxref', views.DbxrefViewSet, base_name='dbxref')
router.register(r'chromosome', views.ChromosomeViewSet, base_name='chromosome')
router.register(r'scaffold', views.ScaffoldViewSet, base_name='scaffold')

cv_router = routers.NestedSimpleRouter(
    router, r'cv', lookup='cv')
cv_router.register(r'cvterm', views.NestedCvtermViewSet)

organism_router = routers.NestedSimpleRouter(
    router, r'organism', lookup='organism')
organism_router.register(r'chromosome', views.NestedChromosomeViewSet,
                         base_name='chromosome')
organism_router.register(r'scaffold', views.NestedScaffoldViewSet,
                         base_name='scaffold')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stats$', views.stats, name='stats'),
    url(r'api/', include_docs_urls(title='machado API')),
    url(r'api/', include(router.urls)),
    url(r'api/', include(cv_router.urls)),
    url(r'api/', include(organism_router.urls)),
]
