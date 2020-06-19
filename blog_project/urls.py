
from django.contrib import admin
from django.urls import path , include
from post import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView , LogoutView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    #basic path 
    path('admin/', admin.site.urls),
    path('',views.Home.as_view() ,name='home'),
    
    #project path
    path('post/',include('post.urls', namespace='Post')),
    path('comment/',include('comment.urls', namespace='Comment')),
    path('api/',include('post.api.urls', namespace='Post_api')),
    path('comment/api/',include('comment.api.urls' ,namespace='Comment_api')),
    path('user/',include('api.urls' ,namespace='User_api')),

    path('api/token/auth/', obtain_jwt_token),

    #registrations path
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name='registrations/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),    
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
Authernticatino check 
curl -X POST -d "username=vish&password=123" http://127.0.0.1:8000/api/token/auth/

Generate token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InZpc2giLCJleHAiOjE1OTI1NTY4MjgsImVtYWlsIjoiMUBnbWFpbC5jb20ifQ.A5XRg1VDOOZQK9ZFq63jhfox9ah2t0ZGP4AD1nv5jdw


Get Request : 
curl -H "Authorization: JWT "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InZpc2giLCJleHAiOjE1OTI1NTcxMzEsImVtYWlsIjoiMUBnbWFpbC5jb20ifQ.GPQxZsyH3mYIF7T00bIOP2ipP6c_ob1UL5IxRHgjpbI
" " http://127.0.0.1:8000/api/post/"




 curl -X POST -H "Authorization: JWT "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InZpc2giLCJleHAiOjE1OTI1NTkxMTAsImVtYWlsIjoiMUBnbWFpbC5jb20ifQ.tXqgwSsBStujmgQUXemaBYtKCTvyKKu_uBCE6uz_i_A" 
 -H "Content-Type: application/json" -d '{"title":"api-title", "content":"api-content" ,"public":"2020/3/20" }' "http://127.0.0.1:8000/api/post/create/"

"""