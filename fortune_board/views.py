from django.views.generic import ListView,DetailView
from django.shortcuts import render
from .models import Post


# Create your views here.
class PostList(ListView):
    model = Post    

    def get_queryset(self):
        return Post.objects.filter(publish_confirm=True).order_by('-pk')    

    # context_object_name = ''
    # template_name='fortune_board/index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = "fortune_board/post_detail.html"

    

# def index(request):

#     post_list= Post.objects.filter(publish_confirm=True).order_by('-pk')

#     return render(
#         request, 
#         'fortune_board/index.html',
#         { 'posts': post_list, }
#         )


# def single_post_page(request, pk):
#     post = Post.objects.filter(publish_confirm=True).get(pk=pk)

#     return render(
#         request,
#         'fortune_board/single_post_page.html',
#         { 'post': post }
#         )