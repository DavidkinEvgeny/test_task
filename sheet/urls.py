from django.urls import path
from .views import SheetListView, SheetDetailView, SheetCreateView, SheetUpdateView, \
    SheetDeleteViews, SerchResultsView


urlpatterns = [
    path('', SheetListView.as_view(), name='list_sheet'),
    path('detail/<int:pk>/', SheetDetailView.as_view(), name='detail_sheet'),
    path('add-sheet/', SheetCreateView.as_view(), name='add_sheet'),
    path('update-sheet/<int:pk>/', SheetUpdateView.as_view(), name='update_sheet'),
    path('delete-sheet/<int:pk>/', SheetDeleteViews.as_view(), name='delete_sheet'),
    path('search/', SerchResultsView.as_view(), name='search_results'),
]
