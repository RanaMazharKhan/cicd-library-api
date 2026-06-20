"""urls.py - this is the receptionist for the whole factory.
When someone knocks on a door, this file decides which
assembly line (app) should answer.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("library.urls")),  # send everything else to "library"
]
