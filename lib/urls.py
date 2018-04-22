from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)/$', views.book_detail, name='book_detail')
]
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]