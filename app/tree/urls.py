from django.urls import path
from django.contrib import admin
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view

from tree.views import TreeList, TreeDetail, PreorderTree, MaxTree, MinTree, LowestCommonAncestor

schema_view = get_swagger_view(title='BINARY SEARCH TREE WEB API')


urlpatterns = [
    path('front/betsy/irish/embargo/admin/', admin.site.urls),

    # Swagger API
    path(
        'api/',
        schema_view,
        name='api'
    ),

    # tree
    path(
        'tree/',
        TreeList.as_view(),
        name=TreeList.name
    ),
    re_path(
        '^tree/(?P<pk>[0-9]+)/$',
        TreeDetail.as_view(),
        name=TreeDetail.name
    ),
    path(
        'preorder/',
        PreorderTree.as_view(),
        name=PreorderTree.name
    ),
    path(
        'max/',
        MaxTree.as_view(),
        name=MaxTree.name
    ),
    path(
        'min/',
        MinTree.as_view(),
        name=MinTree.name
    ),
    path(
        'common-ancestor/',
        LowestCommonAncestor.as_view(),
        name=LowestCommonAncestor.name
    ),
]