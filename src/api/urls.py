from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

'''
API endpoints:

GET /api/youth
    Param: activeOnly=True (if activeOnly param not specified, default value is False)
    Param: search=john (optional search param filters search results)
    Returns: Array of youth objects

GET /api/youth/ (pk is an int which represents a youth's primary key)
    Returns: Youth object for the youth with that PK

PUT /api/youth/PK/progress-chart (create or update operation for the progress chart.
    Once a user presses "save changes", the front end will persist changes with this PUT request)
    Returns: response code 201
'''

urlpatterns = [
    url(r'^youth/$', views.YouthList.as_view(), name='youth-list'),
    url(r'^youth/(?P<youth_id>[0-9]+)/$', views.YouthDetail.as_view(), name='youth-detail'),
    url(r'^placement-type/$', views.PlacementTypeList.as_view(), \
        name='youth-change-placement'),
    url(r'^visit/(?P<youth_visit_id>[0-9]+)/change-placement/$', views.YouthChangePlacement.as_view(), \
        name='youth-change-placement'),
    url(r'docs/$', views.api_docs, name='docs')
]
urlpatterns = format_suffix_patterns(urlpatterns)
