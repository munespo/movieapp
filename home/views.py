from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Video
# Create your views here.
def home(request):
   videoob=Video.objects.order_by('-created_date')[:5]
   
   context = {
    'videoob': videoob,
    }
   return render(request, 'home/welcome.html',context)

def view_movie(request,id):
    videoob= Video.objects.get(id=id)
    context = {
    'videoob': videoob,
    }
    return render(request, 'home/view_movie.html',context)

class CreateVideo(CreateView):
    model = Video
    fields = ['name', 'type', 'client', 'project_manager','title','description','videoFile','thumbnail','created_date','edited_date']
    template_name = 'home/create_video.html'   
    def get_success_url(self):
        return reverse('home')

class UpdateVideo(UpdateView):
    model = Video
    fields = ['name', 'type', 'client', 'project_manager','title','description','videoFile','thumbnail','created_date','edited_date']
    template_name = 'home/create_video.html'   
    def get_success_url(self):
        return reverse('home')

class DeleteVideo(DeleteView):
    model = Video
    template_name = 'home/delete_video.html'   
    def get_success_url(self):
        return reverse('home')
def members(request):
   
   return render(request, 'home/members.html')
