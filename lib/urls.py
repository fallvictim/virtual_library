from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    url(r'^$', views.main_page, name='main_page'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail')
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]

urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/(<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete')
]

urlpatterns += [
    path('book/instances/create', views.BookInstanceCreate.as_view(), name='bookinst_create'),
    path('book/(<int:book_pk>/<uuid:pk>/update', views.BookInstanceUpdate.as_view(), name='bookinst_update'),
    path('book/<int:book_pk>/<uuid:pk>/delete', views.BookInstanceDelete.as_view(), name='bookinst_delete')
]

urlpatterns += [
    path('book/users/create', views.UserCreate.as_view(), name='user_create'),
]
