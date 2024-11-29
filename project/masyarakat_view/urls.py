from django.urls import path
from .views import (
  UserDashboardView,

  PengaduanHistoryListView,
  PengaduanCreateView,
  PengaduanDeleteView,
)

urlpatterns = [
  path('' , UserDashboardView.as_view(), name="user_dashboard"),

  path('pengaduan/history/', PengaduanHistoryListView.as_view(), name="pengaduan_history"),
  path('pengaduan/create/<int:jenis_laporan_id>', PengaduanCreateView.as_view(), name="pengaduan_create"),
  path('pengaduan/delete/<int:pk>', PengaduanDeleteView.as_view(), name="pengaduan_delete"),
]