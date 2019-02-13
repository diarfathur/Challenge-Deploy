from django.shortcuts import render, redirect
from .models import Post
from .forms import NewPost
from django.utils import timezone

# Create your views here.
def blog(request):
   post = Post.objects.all()
   return render(request, 'blog.html', {'post': post})

def new_post(request):
   if request.method == "POST":
      form = NewPost(request.POST, request.FILES)
      if form.is_valid():
         post = form.save(commit=False)
         post.created_at = timezone.now()
         post.save()
         return redirect('blog')

   else:
      form = NewPost()
   return render(request, 'new-post.html', {'new_posts': form})

def post_page(request, id_post):
   post_ke = Post.objects.get(pk=id_post)
   return render(request, 'post-page.html', {'post_ke': post_ke})