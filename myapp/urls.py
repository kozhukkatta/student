from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('course',views.course,name='course'),
    path('student',views.student,name='student'),
    path('details',views.details,name='details'),
    path('cour_det',views.cour_det,name='cour_det'),
    path('reg',views.reg,name='reg'),
    path('add_course',views.add_course,name='add_course'),
    path('add_student',views.add_student,name='add_student'),
    path('edits/<int:pk>',views.edits,name='edits'),
    path('up_student/<int:pk>',views.up_student,name='up_student'),
    path('deletes/<int:pk>',views.deletes,name='deletes'),
    path('editc/<int:pk>',views.editc,name='editc'),
    path('up_course/<int:pk>',views.up_course,name='up_course'),
    path('deletec/<int:pk>',views.deletec,name='deletec'),
    path('add_stud',views.add_stud,name='add_stud'),
    
]