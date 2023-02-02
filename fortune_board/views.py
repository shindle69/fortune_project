from django.views.generic import ListView,DetailView
from django.shortcuts import render
from .models import Post, Category


# Create your views here.
def category_page(request, slug):
    if slug == "no_category":
        category = "미분류"
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'fortune_board/post_list.html',
        {
            'post_list':post_list,
            'categories':Category.objects.all(),
            'no_category_post_count':Post.objects.filter(category=None).count(),
            'category':category,
        }
    )

class PostList(ListView):
    model = Post    

    def get_queryset(self):
        return Post.objects.filter(publish_confirm=True).order_by('-pk')    

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context

    # context_object_name = ''
    # template_name='fortune_board/index.html'

class PostDetail(DetailView):
    model = Post
    template_name = "fortune_board/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context

    

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