from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('qualifications/', views.qualifications, name='qualifications'),
    path('qualifications/<int:id>/', views.qualifications, name='edit_qualification'),
    path('qualifications/delete/<int:id>/', views.delete_qualification, name='delete_qualification'),

    path('languages/', views.languages, name='languages'),
    path('languages/<int:id>/', views.languages, name='edit_language'),
    path('languages/delete/<int:id>/', views.delete_language, name='delete_language'),

    path('frameworkapis/', views.frameworkapi, name='frameworkapi'),
    path('frameworkapis/<int:id>/', views.frameworkapi, name='edit_frameworkapi'),
    path('frameworkapis/delete/<int:id>/', views.delete_frameworkapi, name='delete_frameworkapi'),

    path('databases/', views.databases, name='databases'),
    path('databases/<int:id>/', views.databases, name='edit_database'),
    path('databases/delete/<int:id>/', views.delete_database, name='delete_database'),

    path('toolsplatforms/', views.toolsplatforms, name='toolsplatforms'),
    path('toolsplatforms/<int:id>/', views.toolsplatforms, name='edit_toolplatform'),
    path('toolsplatforms/delete/<int:id>/', views.delete_tool, name='delete_toolplatform'),

    path('webtech/', views.webtech, name='webtech'),
    path('webtech/<int:id>/', views.webtech, name='edit_webtech'),
    path('webtech/delete/<int:id>/', views.delete_webtech, name='delete_webtech'),

    path('coreconcepts/', views.coreconcept, name='coreconcepts'),
    path('coreconcepts/<int:id>/', views.coreconcept, name='edit_coreconcept'),
    path('coreconcepts/delete/<int:id>/', views.delete_coreconcept, name='delete_coreconcept'),

    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.projects, name='edit_project'),
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete_project'),

    path('experience/', views.experience, name='experience'),
    path('experience/<int:exp_id>/', views.experience, name='edit_experience'),
    path('experience/delete/<int:exp_id>/', views.delete_experience, name='delete_experience'),
    path('contact/', views.contact, name='contact'),

    path('sociallinks/', views.social_media, name='socialmedia'),
    path('sociallinks/<int:id>/', views.social_media, name='edit_socialmedia'),
    path('sociallinks/delete/<int:id>/', views.delete_social_media, name='delete_socialmedia'),

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)