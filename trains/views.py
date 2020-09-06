from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Train
from .forms import TrainForm


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 10)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'train_home.html', {'objects_list': trains, })


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Train
    form_class = TrainForm
    template_name = 'train_create.html'
    success_url = reverse_lazy('train:home')
    success_message = 'The train has been successfully added!'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'object'
    template_name = 'train_detail.html'


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Train
    form_class = TrainForm
    template_name = 'train_update.html'
    success_url = reverse_lazy('train:home')
    success_message = 'The train has been successfully edited!'


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Train
    success_url = reverse_lazy('train:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'The train has been successfully deleted!')
        return self.post(request, *args, **kwargs)