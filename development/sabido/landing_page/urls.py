from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name = 'landing_page'),
    path('main', views.main, name = 'main')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

