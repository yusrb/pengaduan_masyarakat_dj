from typing import Any
from django.urls import reverse_lazy
from django.views.generic import (
  ListView,
  CreateView,
  DeleteView,
)
from django.shortcuts import get_object_or_404, redirect
from .forms import PengaduanForm
from .models import (
  Masyarakat,
  Jenis_Laporan,
  Pengaduan,
)
from petugas_view.models import (
  Petugas
)
from dinas_view.models import Dinas

class UserDashboardView(ListView):
  model = Jenis_Laporan
  template_name = "masyarakat/dashboard.html"
  context_object_name = 'jenis_laps'

  def get(self,request):
    if not self.request.user.is_authenticated:
      return redirect('auth:user_login')

    user = self.request.user
    if isinstance(user, Petugas):
      return redirect('petugas:petugas_dashboard')
    return super().get(request)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["judul"] = "Dashboard Pengaduan Masyarakat"
      context["header"] = "Dashboard Masyarakat"
      context["dinas_all"] = Dinas.objects.all()
      return context

class PengaduanHistoryListView(ListView):
  model = Pengaduan
  template_name = 'masyarakat/pengaduan_history.html'
  context_object_name = "pengaduans"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["judul"] = "Histori Pengaduan Page"
      context['header'] = "Dashboard Masyarakat"
      context["pengaduans"] = Pengaduan.objects.filter(user=self.request.user.pk).order_by('-tgl_pengaduan')
      return context

class PengaduanCreateView(CreateView):
    model = Pengaduan
    template_name = "masyarakat/pengaduan_form.html"
    form_class = PengaduanForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['judul'] = "Pengaduan Create Page"

        jenis_laporan_id = self.kwargs.get('jenis_laporan_id')
        jenis_laporan = get_object_or_404(Jenis_Laporan, id=jenis_laporan_id)
        context['jenis_laporan'] = jenis_laporan

        return context

    def form_valid(self, form):
        jenis_laporan_id = self.kwargs.get('jenis_laporan_id')
        jenis_laporan = get_object_or_404(Jenis_Laporan, id=jenis_laporan_id)

        user = self.request.user
        if isinstance(user, Masyarakat):
            form.instance.user = user
            form.instance.jenis_laporan = jenis_laporan
            return super().form_valid(form)
        else:
            return redirect('masyarakat:user_login')

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('auth:user_login')

        user = self.request.user
        if isinstance(user, Petugas):
            return redirect('petugas:petugas_dashboard')

        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('masyarakat:user_dashboard')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan

    def get_success_url(self):
      return reverse_lazy('masyarakat:pengaduan_history')
