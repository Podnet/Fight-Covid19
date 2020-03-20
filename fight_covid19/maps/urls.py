# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import include, path
# from django.views.generic import TemplateView
# from rest_framework.authtoken.views import obtain_auth_token
# from fight_covid19.maps import views as map_views
#
# # from
#
# urlpatterns = [
#     path("", map_views.HomePageView(), name="home"),
#     path(
#         "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
#     ),
#     path("maps/", TemplateView.as_view(template_name="maps/maps.html"), name="maps"),
#     # Django Admin, use {% url 'admin:index' %}
#     path(settings.ADMIN_URL, admin.site.urls),
#     # User management
#     path("users/", include("fight_covid19.users.urls", namespace="users")),
#     path("accounts/", include("allauth.urls")),
#     # Your stuff: custom urls includes go here
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# # API URLS
# urlpatterns += [
#     # API base url
#     path("api/", include("config.api_router")),
#     # DRF auth token
#     path("auth-token/", obtain_auth_token),
# ]
