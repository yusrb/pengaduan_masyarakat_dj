from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from masyarakat_view.models import Masyarakat, Pengaduan
from .models import Petugas, Tanggapan, Log_Aktivitas
from .forms import TanggapanForm

class PengaduanBelumTerjawabListView(ListView):
    model = Pengaduan
    template_name = "petugas/pengaduan_belum_terjawab.html"
    context_object_name = "pengaduans"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('auth:petugas_login')

        user = self.request.user
        if isinstance(user, Masyarakat):
            return redirect('masyarakat:user_dashboard')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['judul'] = "Pengaduan Belum Terjawab"
        context['pengaduans'] = Pengaduan.objects.filter(status=Pengaduan.Status.BELUM_TERJAWAB)
        return context

class TanggapanBelumTerjawabCreateView(CreateView):
    model = Tanggapan
    fields = ['tanggapan']
    template_name = 'petugas/tanggapan_form.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.level == 'petugas':
            pengaduan_id = self.kwargs.get('pengaduan_id')
            pengaduan = get_object_or_404(Pengaduan, pk=pengaduan_id)

            if pengaduan.status != Pengaduan.Status.BELUM_TERJAWAB:
                return redirect('petugas:petugas_dashboard')

            return super().get(request, *args, **kwargs)
        else:
            return redirect('auth:petugas_login')

    def form_valid(self, form):
        tanggapan = form.save(commit=False)

        pengaduan_id = self.kwargs.get('pengaduan_id')
        pengaduan = get_object_or_404(Pengaduan, pk=pengaduan_id)

        tanggapan.pengaduan = pengaduan
        tanggapan.petugas = self.request.user

        pengaduan.status = Pengaduan.Status.DESPOSISI
        tanggapan.status = Tanggapan.Status.DESPOSISI

        tanggapan.save()
        pengaduan.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('petugas:petugas_dashboard')

class PengaduanDesposisiListView(ListView):
    model = Pengaduan
    template_name = "petugas/pengaduan_desposisi.html"
    context_object_name = "pengaduans"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('auth:petugas_login')

        user = self.request.user
        if isinstance(user, Masyarakat):
            return redirect('masyarakat:user_dashboard')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['judul'] = "Pengaduan Desposisi"
        context['pengaduans'] = Pengaduan.objects.filter(status=Pengaduan.Status.DESPOSISI)
        return context

class TanggapanDesposisiCreateView(CreateView):
    model = Tanggapan
    fields = ['tanggapan']
    template_name = 'petugas/tanggapan_form.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.level == 'petugas':
            pengaduan_id = self.kwargs.get('pengaduan_id')
            pengaduan = get_object_or_404(Pengaduan, pk=pengaduan_id)

            if pengaduan.status != Pengaduan.Status.DESPOSISI:
                return redirect('petugas:petugas_dashboard')

            return super().get(request, *args, **kwargs)
        else:
            return redirect('auth:petugas_login')

    def form_valid(self, form):
        tanggapan = form.save(commit=False)

        pengaduan_id = self.kwargs.get('pengaduan_id')
        pengaduan = get_object_or_404(Pengaduan, pk=pengaduan_id)

        tanggapan.pengaduan = pengaduan
        tanggapan.petugas = self.request.user

        pengaduan.status = Pengaduan.Status.PROSES
        tanggapan.status = Tanggapan.Status.PROSES

        tanggapan.save()
        pengaduan.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('petugas:petugas_dashboard')

class PengaduanProsesListView(ListView):
    model = Pengaduan
    template_name = "petugas/pengaduan_proses.html"
    context_object_name = "pengaduans"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('auth:petugas_login')

        user = self.request.user
        if isinstance(user, Masyarakat):
            return redirect('masyarakat:user_dashboard')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['judul'] = "Pengaduan Proses"
        context['pengaduans'] = Pengaduan.objects.filter(status=Pengaduan.Status.PROSES)
        return context

class TanggapanProsesCreateView(CreateView):
    model = Tanggapan
    fields = ['tanggapan']
    template_name = 'petugas/tanggapan_form.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.level == 'petugas':
            pengaduan_id = self.kwargs.get('pengaduan_id')
            pengaduan = get_object_or_404(Pengaduan, pk=pengaduan_id)

            if pengaduan.status != Pengaduan.Status.PROSES:
                return redirect('petugas:petugas_dashboard')

            return super().get(request, *args, **kwargs)
        else:
            return redirect('auth:petugas_login')

    def form_valid(self, form):
        tanggapan = form.save(commit=False)

        pengaduan_id = self.kwargs.get('pengaduan_id')
        pengaduan = get_object_or_404(Pengaduan, pk=pengaduan_id)

        tanggapan.pengaduan = pengaduan
        tanggapan.petugas = self.request.user

        pengaduan.status = Pengaduan.Status.SELESAI
        tanggapan.status = Tanggapan.Status.SELESAI

        tanggapan.save()
        pengaduan.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('petugas:petugas_dashboard')

class PengaduanSelesaiListView(ListView):
    model = Pengaduan
    template_name = "petugas/pengaduan_selesai.html"
    context_object_name = "pengaduans"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('auth:petugas_login')

        user = self.request.user
        if isinstance(user, Masyarakat):
            return redirect('masyarakat:user_dashboard')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['judul'] = "Pengaduan Selesai"
        context['pengaduans'] = Pengaduan.objects.filter(status=Pengaduan.Status.SELESAI)
        return context

class PengaduanTolakListView(ListView):
    model = Pengaduan
    template_name = "petugas/pengaduan_tolak.html"
    context_object_name = "pengaduans"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('auth:petugas_login')

        user = self.request.user
        if isinstance(user, Masyarakat):
            return redirect('masyarakat:user_dashboard')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['judul'] = "Pengaduan Tolak"
        context['pengaduans'] = Pengaduan.objects.filter(status=Pengaduan.Status.TOLAK)
        return context

class TanggapanTolakView(UpdateView):
    model = Pengaduan
    template_name = 'petugas/tanggapan_tolak.html'
    context_object_name = 'pengaduan'
    form_class = TanggapanForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["judul"] = "Validasi Kembali Page"
        return context

    def get_object(self):
        pengaduan = get_object_or_404(Pengaduan, id=self.kwargs['pengaduan_id'], status=Pengaduan.Status.TOLAK)
        return pengaduan

    def form_valid(self, form):
        pengaduan = form.save(commit=False)
        pengaduan.status = Pengaduan.Status.SELESAI
        pengaduan.petugas = self.request.user
        pengaduan.save()
        return redirect('petugas:pengaduan_tolak_view')

class TanggapanSelesaiCreateView(CreateView):
    model = Tanggapan
    fields = ['tanggapan']
    template_name = 'petugas/tanggapan_form.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.level == 'petugas' or self.request.user.level == 'admin':
            pengaduan_id = self.kwargs.get('pengaduan_id')
            pengaduan = get_object_or_404(Pengaduan, pk=pengaduan_id)

            return super().get(request, *args, **kwargs)
        else:
            return redirect('auth:petugas_login')

    def form_valid(self, form):
        tanggapan = form.save(commit=False)

        pengaduan_id = self.kwargs.get('pengaduan_id')
        pengaduan = get_object_or_404(Pengaduan, pk=pengaduan_id)

        tanggapan.pengaduan = pengaduan
        pengaduan.petugas = self.request.user
        tanggapan.petugas = self.request.user

        pengaduan.status = Pengaduan.Status.TOLAK
        tanggapan.status = Tanggapan.Status.TOLAK

        tanggapan.save()
        pengaduan.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('petugas:petugas_dashboard')

def buat_pengaduan_dokumen(request):
    pengaduans = Pengaduan.objects.filter(status='SELESAI')
    html_content = render_to_string('petugas/pengaduan_docs.html', {
        'pengaduans': pengaduans,
    })
    pdf = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="laporan_pengaduan_selesai.pdf"'
    return response
