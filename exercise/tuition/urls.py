from django.urls import path

from . import views


urlpatterns = [
    path('index/', views.index,name='index'),
    path('',views.home,name='base'),
    path('contract/',views.contract,name='contract'),
    path('cmf/',views.contactmodelForm,name='cmf'),
    path('postview/',views.postview,name='postview'),
    path('create/',views.postcreate,name='postcreate')


    

]
