from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()
urlpatterns = patterns('',
                       # Admin
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       # Calculate
                       # url(r'^herokuapp.com/$',
                       #     RedirectView.as_view(url='http://www.stringulator.com', permanent=True)),
                       (r'^calculate/$', 'calculator.views.load_calculate_page'),
                       (r'^pretty-calculate/$', 'calculator.views.load_pretty_calculate_page'),
                       (r'^calculate-tension/$', 'calculator.views.convert_input_to_tension'),
                       (r'^save-set/$', 'calculator.views.save_set'),
                       (r'^test/$', 'contact.views.test'),

                       # Download
                       (r'^download-set', 'users.views.downloadStringSet'),

                       # Search
                       (r'^search/$', 'users.views.search'),

                       # USERS

                       # Login
                       (r'^accounts/login/$', 'users.views.login'),
                       (r'^$', 'users.views.login'),
                       (r'^accounts/invalid/$', 'users.views.invalid_login'),
                       # Authorize user
                       (r'^authorize-account/$', 'users.views.auth_view'),
                       (r'^login/$', 'users.views.auth_view'),
                       # Logout
                       (r'^accounts/logout/$', 'users.views.logout'),
                       # Register
                       (r'^accounts/register_success/$', 'users.views.register_success'),
                       (r'^accounts/register/$', 'users.views.register_user'),

                       # Profile
                       (r'^profile/$', 'users.views.profile'),
                       (r'^ajax-delete/$', 'calculator.views.ajax_delete_set'),

                       # Contact
                       (r'^contact/$', 'contact.views.load_contact_page'),

                       # Test
                       # (r'^test/$', 'contact.views.load_test_page'),
                       (r'^base-bak/$', 'contact.views.load_base_bak_page'),
)
