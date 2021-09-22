from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.home, name='home'),
  path('portfolio/', views.portfolio, name='portfolio'),
  path('about/', views.about, name='about'),
  path('contact/', views.contact, name='contact'),
  path('search/',views.search_portfolio,name='search_portfolio'),
  path('portfolio/details/<int:portfolio_id>',views.detail,  name='portfolio_details'),
  path('api/projects/',views.MerchList.as_view()),
  path('api/users/',views.MerchUser.as_view())

]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)