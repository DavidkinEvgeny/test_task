from django.urls import path
from .views import SheetListView, SheetDetailView, SheetCreateView, SheetUpdateView, \
    SheetDeleteViews, SerchResultsView, SheetListViewAPI, SheetDetailViewAPI, SheetCreateViewAPI, \
    SheetUpdateViewAPI, SheetDeleteViewAPI, SerchResultsViewAPI


urlpatterns = [
    path('', SheetListView.as_view(), name='list_sheet'),
    path('v1/', SheetListViewAPI.as_view()),
    path('detail/<int:pk>/', SheetDetailView.as_view(), name='detail_sheet'),
    path('v1/detail/<int:pk>/', SheetDetailViewAPI.as_view()),
    path('add-sheet/', SheetCreateView.as_view(), name='add_sheet'),
    path('v1/add-sheet/', SheetCreateViewAPI.as_view()),
    path('update-sheet/<int:pk>/', SheetUpdateView.as_view(), name='update_sheet'),
    path('v1/update-sheet/<int:pk>/', SheetUpdateViewAPI.as_view()),
    path('delete-sheet/<int:pk>/', SheetDeleteViews.as_view(), name='delete_sheet'),
    path('v1/delete-sheet/<int:pk>/', SheetDeleteViewAPI.as_view()),
    path('search/', SerchResultsView.as_view(), name='search_results'),
    path('v1/search/', SerchResultsViewAPI.as_view()),
]