from django.urls import path
from .views import (
    PengaduanBelumTerjawabListView,
    TanggapanBelumTerjawabCreateView,
    PengaduanDesposisiListView,
    TanggapanDesposisiCreateView,
    PengaduanProsesListView,
    TanggapanProsesCreateView,
    PengaduanSelesaiListView,
    PengaduanTolakListView,
    TanggapanTolakView,
    TanggapanSelesaiCreateView,

    buat_pengaduan_dokumen
)

urlpatterns = [
    path('', PengaduanBelumTerjawabListView.as_view(), name='petugas_dashboard'),
    path('tanggapan/belum-terjawab/<int:pengaduan_id>/', TanggapanBelumTerjawabCreateView.as_view(), name='tanggapan_belum_terjawab'),
    path('pengaduan/desposisi/', PengaduanDesposisiListView.as_view(), name='pengaduan_desposisi'),
    path('tanggapan/desposisi/<int:pengaduan_id>/', TanggapanDesposisiCreateView.as_view(), name='tanggapan_desposisi'),
    path('pengaduan/proses/', PengaduanProsesListView.as_view(), name='pengaduan_proses'),
    path('tanggapan/proses/<int:pengaduan_id>/', TanggapanProsesCreateView.as_view(), name='tanggapan_proses'),
    path('pengaduan/selesai/', PengaduanSelesaiListView.as_view(), name='pengaduan_selesai'),
    path('pengaduan/tolak/', PengaduanTolakListView.as_view(), name='pengaduan_tolak'),
    path('pengaduan/tanggapan/tolak/<int:pengaduan_id>/', TanggapanTolakView.as_view(), name='tanggapan_tolak'),
    path('tanggapan/selesai/<int:pengaduan_id>/', TanggapanSelesaiCreateView.as_view(), name='tanggapan_selesai'),

    path('pengaduan/<int:pengaduan_id>/generate_pdf/', buat_pengaduan_dokumen, name='buat_pengaduan_dokumen'),
]
