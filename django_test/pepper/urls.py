from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^registration/$',views.registration),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
