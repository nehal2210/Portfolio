
from django.urls import path,include
import blog.views

urlpatterns = [
 
    path("", blog.views.allblog,name='allblog'),
    path("<int:blog_id>/", blog.views.detail,name='detail'),

]
