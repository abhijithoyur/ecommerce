from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import  Task
from . forms import TodoForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView


from django.shortcuts import HttpResponse
# Create your views here.
class List_view(ListView):
    model=Task
    template_name='home.html'
    context_object_name ='task1'

class TaskDetail_view(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'task'
class TaskUpdate_view(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')


    def get_success_url(self):
        return reverse_lazy('cdetail',kwargs={'pk':self.object.id})
class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('chome')


def task(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')

    return render(request,"delete.html")
def update(request,id):
    ta=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=ta)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'ta':ta})