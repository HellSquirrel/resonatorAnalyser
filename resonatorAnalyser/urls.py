from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from analyser.views import results
# from django.contrib import admin
# admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='main.html')),
    url(r'matrix/$', results.MatrixView.as_view()),
    url(r'misalignments/$', results.MisView.as_view())

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
