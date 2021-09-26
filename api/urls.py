from django.urls import path

from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "own_api"


schema_view = get_schema_view(
   openapi.Info(
      title="OMDB API Client",
      default_version='v1',
      description="The clone of omdb api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('all_movies/', views.MovieListView.as_view()),
    path("add_movie/", views.MovieCreateView.as_view()),
    path('movie/<int:id>/', views.MovieDetailView.as_view()),
    path('genre/', views.GenreCreateListView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]