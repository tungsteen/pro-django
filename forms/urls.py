from django.conf.urls import url
from .views import index, custom_form_view, upload_form_view

urlpatterns = [
    url(r'^$', index),
    url(r'custom$', custom_form_view),
    url(r'upload$', upload_form_view)
]
