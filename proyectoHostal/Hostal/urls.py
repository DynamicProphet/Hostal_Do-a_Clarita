"""Hostal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls'), name='producto'),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^password_reset/$',
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            email_template_name="registration/password_reset_email.html",
            success_url=('/password_reset_done/'),
        ),
        name='password_reset'
    ),
    re_path(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^password_reset_complete/$',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
