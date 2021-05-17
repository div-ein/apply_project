from django.shortcuts import render, get_object_or_404, redirect
from .models import Apply
from django.utils import timezone
from .forms import CreatePostForm
# Create your views here.

def home(request):
  applies = Apply.objects
  return render(request, 'home.html',{'applies':applies})

def detail(request,apply_id)  :
  apply_detail = get_object_or_404(Apply, pk=apply_id)
  return render(request,'detail.html',{'apply_detail':apply_detail})

def create(request):
  if request.method == 'POST' :
    form = CreatePostForm(request.POST)
    if form.is_valid():
      apply = form.save(commit=False)
      apply.pub_date = timezone.datetime.now()
      apply.save()
      return redirect('/detail/'+str(apply.id))
  else:
    form = CreatePostForm()
  return render(request, 'create.html', {'form':form})

def update(request,apply_id):
  apply = Apply.objects.get(id=apply_id)
  if request.method == "POST":
    form = CreatePostForm(request.POST, instance=apply)
    if form.is_valid():
      apply = apply.save()
      return redirect('/detail/'+str(apply.id))
    
  else:
    form = CreatePostForm(instance=apply)
    return render(request, 'create.html', {'form':form})

def delete(request, apply_id):
  apply = Apply.objects.get(id=apply_id)
  apply.delete()
  return redirect('home')

def member(request):
  applies = Apply.objects
  return render(request,'member.html',{'applies':applies})

def info(request):
  return render(request, 'info.html')