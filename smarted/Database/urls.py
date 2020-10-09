from rest_framework import routers
from django.urls import path
from . import views
from .api import *

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('resources', ResourceViewSet, 'resources')
router.register('files', FileViewSet, 'files')
router.register('institutions', InstitutionViewSet, 'institutions')
router.register('courses', CourseViewSet, 'courses')
router.register('assessment', AssessmentViewSet, 'assessment')
router.register('staffCourse', StaffCourseViewSet, 'staffCourse')
router.register('studentCourse', StudentCourseViewSet, 'studentCourse')
router.register('student', StudentViewSet, 'student')
router.register('staff', StaffViewSet, 'staff')
router.register('studentAssessment', StudentAssessmentViewSet, 'studentAssessment')
router.register('courseGradeGoal', CourseGradeGoalViewSet, 'courseGradeGoal')
urlpatterns = router.urls

urlpatterns += [
    path('course-assessment/', views.course_assessment, name='course-assessment'),
    path('login-post/', views.log_in, name='login'),
    path('student-courses/', views.get_student_courses, name='student-courses'),
    path('post-vark/', views.post_vark, name='post-vark'),
    path('get-vark/', views.get_vark, name='get-vark'),
    path('get-grades/', views.get_student_grades, name='get-grades'),

    path('teacher-login/', views.teacher_login, name='teacher-login'),
    path('students-in-course/', views.students_in_course, name='students-in-course'),
    path('student-assessment-grade/', views.student_assessment_grade, name='student-assessment-grade'),
    path('teacher-courses/', views.teacher_course, name='teacher-courses')
]