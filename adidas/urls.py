"""adidas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from adidas import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name="homepage"),
    url(r'^register$', views.RegistrationView.as_view(), name="register"),
    url(r'^sign-in$', views.SignInView.as_view(), name="sign-in"),
    url(r'^sign-out$', views.SignOutView.as_view(), name="sign-out"),
    url(r'^profile/view$', views.ProfileDetailView.as_view(),
        name="profile_view"),
    url(r'^profile/update$', views.ProfileUpdateView.as_view(),
        name="profile_update"),
]