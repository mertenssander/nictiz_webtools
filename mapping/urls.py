from django.conf.urls import url

from . import views

app_name = 'mapping'
urlpatterns = [
    url(r'project/(?P<project>\w+)/task/(?P<task>\w+)', views.TaskEditorPageView.as_view(), name='task_editor'),
    url(r'project/?project_id=(?P<project>\w+)', views.ProjectIndexPageView.as_view(), name='project_index'),
    url(r'taskmanager/(?P<project>\w+)', views.TaskManagerPageView.as_view(), name='taskmanager_project'),
    url(r'taskmanager', views.TaskManagerPageView.as_view(), name='taskmanager'),
    url(r'project/(?P<project>\w+)', views.ProjectIndexPageView.as_view(), name='project_index'),
    url(r'ajaxprogressreport/(?P<secret>\w+)', views.AjaxProgressRecordPageView.as_view(), name='ajaxprogressreport'),
    url(r'ajaxtargetsearch', views.AjaxTargetSearch.as_view(), name='ajaxtargetsearch'),
    url(r'audit/(?P<project>\w+)/(?P<audit_type>\w+)', views.AuditPageView.as_view(), name='audit'),
    url(r'tasksearch/(?P<project>\w+)/', views.AjaxSearchTaskPageView.as_view(), name='tasksearch'),
    url(r'deletecomment/(?P<comment_id>\w+)', views.DeleteCommentPageView.as_view(), name='deletecomment'),
    url(r'postcomment', views.PostCommentPageView.as_view(), name='post_comment'),
    url(r'update_nhg', views.UpdateNHGPageView.as_view(), name='update_nhg'),
    url(r'update_snomed', views.UpdateSnomedPageView.as_view(), name='update_snomed'),
    url(r'task_create', views.TaskCreatePageView.as_view(), name='task_create'),
    url(r'status_filter/(?P<project>\w+)/(?P<task>\w+)/(?P<status>\w+)/(?P<own_tasks>\w+)', views.StatusFilterPageView.as_view(), name='own_task_filter'),
    url(r'status_filter/(?P<project>\w+)/(?P<task>\w+)/(?P<status>\w+)', views.StatusFilterPageView.as_view(), name='status_filter'),
    url(r'status_update/(?P<task>\w+)/(?P<status>\w+)', views.StatusUpdatePageView.as_view(), name='status_update'),
    url(r'change_user/(?P<task>\w+)/(?P<user>\w+)', views.ChangeUserPageView.as_view(), name='change_user'),

    # url(r'ajax_test', views.AjaxTestView.as_view(), name='ajax_test'),
    url(r'ecl_query/(?P<task_id>\w+)', views.AjaxSimpleEclQuery.as_view(), name='ecl_query'),
    url(r'ecl_query_builder_results/(?P<task_id>\w+)', views.AjaxEclQueryMapResults.as_view(), name='ecl_query_builder_results'),
    url(r'ecl_query_builder/(?P<task_id>\w+)', views.AjaxEclQueryMapBuilder.as_view(), name='ecl_query_builder'),
    url(r'whitelist_audit/(?P<audit>\w+)', views.AjaxWhitelistAudit.as_view(), name='whitelist_audit'),
    url(r'show_events/(?P<task>\w+)', views.ViewEventsPageView.as_view(), name='show_events'),
    url(r'mapping_target_list/(?P<task>\w+)', views.MappingTargetListPageView.as_view(), name='mapping_target_list'),
    url(r'get_current_status/(?P<task>\w+)', views.GetCurrentStatus.as_view(), name='get_current_status'),
    url(r'get_audits_for_task/(?P<task>\w+)', views.GetAuditsForTask.as_view(), name='get_audits_for_task'),

    url(r'', views.MappingIndexPageView.as_view(), name='index'),
]