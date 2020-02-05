from rest_framework.routers import DefaultRouter
from maid import views
router=DefaultRouter()
router.register('dashborad',views.DashBoardViewSet,basename='dashboard')
router.register('society',views.SocietyViewSet,basename='society')
router.register('resident',views.ResidentsViewSet,basename='resident')
router.register('employee',views.EmployeeViewSet,basename='employee')
router.register('attendance',views.AttendanceViewSet,basename='attendance')
router.register('reguestbackup',views.Request_backupViewSet,basename='reguestbackup')
router.register('shortlished',views.Sortlist_Request_backup,basename='shortlished')
router.register('replacement',views.ReplacementBackupViewSet,basename='replacement')
# router.register('report',views.Generate_ReportViewSet,basename='report')
router.register('report',views.ReportViewSet,basename='report')
urlpatterns=router.urls