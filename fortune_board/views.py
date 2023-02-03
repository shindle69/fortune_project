from django.views.generic import ListView,DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify

# Create your views here.
def tag_page(request, slug):
    
    tag = Tag.objects.get(slug=slug)
    post_list = Tag.objects.all()

    return render(
        request,
        'fortune_board/post_list.html',
        {
            'post_list':post_list,
            'categories':Category.objects.all(),
            'no_category_post_count':Post.objects.filter(category=None).count(),
            'tag':tag,
        }
    )

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


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = [
        'title', 'content', 'post_image', 'category','publish_confirm', 
    ]

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)

            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                tags_str = tags_str.strip()

                tags_str = tags_str.replace(',',';')
                tags_list = tags_str.split(';')

                for t in tags_list:
                    t = t.strip()
                    tagging, is_tag_created = Tag.objects.get_or_create(name=t)
                    if is_tag_created:
                        tagging.slug = slugify(t, allow_unicode=True)
                        tagging.save()
                    self.object.tag.add(tagging)

            return response
        else:
            return redirect('fortune_board/')

class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    fields = [
        'title', 'content', 'post_image', 'category','publish_confirm', 
    ]

    template_name = "fortune_board/post_update_form.html"

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        if self.object.tag.exists():
            tags_str_list = list()
            for t in self.object.tag.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = ';'.join(tags_str_list)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request,  *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)
        self.object.tag.clear()

        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip()

            tags_str = tags_str.replace(',',';')
            tags_list = tags_str.split(';')

            for t in tags_list:
                t = t.strip()
                tagging, is_tag_created = Tag.objects.get_or_create(name=t)
                if is_tag_created:
                    tagging.slug = slugify(t, allow_unicode=True)
                    tagging.save()
                self.object.tag.add(tagging)

        return response










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