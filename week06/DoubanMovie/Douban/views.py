from django.shortcuts import render

# Create your views here.
from .models import MovieInfo

def movies_short(request):
    ###  从models取数据传给template  ###
    shorts = MovieInfo.objects.all()
    return render(request, 'result.html', locals())

def favourableComment(request):
    condtions = {'n_star__gt': 3}
    results = MovieInfo.objects.filter(**condtions)
    return render(request, 'favourableComment.html', locals())

def search(request):
    s = request.GET['s']
    error_msg = ''
    post_list = MovieInfo.objects.filter(comment__icontains=s)
    return render(request, 'results.html', {'error_msg': error_msg,'post_list': post_list})