from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('login', views.login_page, name='login_page'),
    path('courses', views.courses_page, name='courses_page'),
    path('results_page', views.results_page, name='results_page'),
    path('course/<int:pk>', views.course_detail_page, name='course_detail_page'),
    path('profile', views.profile_page, name='profile_page'),
    path('profile/delete', views.profile_delete_view, name='delete_profile'),
    path('logout', views.logout_view, name='logout_view'),
    path('register', views.register_page, name='register_page'),

]