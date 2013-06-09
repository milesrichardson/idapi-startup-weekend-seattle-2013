from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^person/new$', 'api.views.create_person'),
    # url(r'^person/update/(\d{0,9})$', 'api.views.update_person'),
    # url(r'^person/(\d{0,9})$', 'api.views.get_person', 'person_id'),
    url(r'^persons$', 'api.views.list_persons'),
    url(r'^query-types$', 'api.views.list_query_types'),
    url(r'^fields$', 'api.views.list_fields'),
    # url(r'^fields/required/?P<path>.*)$', 'api.views.list_required_fields'),
    # url(r'^fields/{field-id}', 'api.views.get_field'),
    url(r'^query/new', 'api.views.new_query'),
    url(r'^query/results', 'api.views.list_query_results'),
    # url(r'^query/results/(\d{0,9})$', 'api.views.list_query_results_by_person'),
    # url(r'^query/result/(\d{0,9})$', 'api.views.get_result')
)
