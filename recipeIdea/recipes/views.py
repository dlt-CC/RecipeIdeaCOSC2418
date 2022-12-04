from django.views import generic
from .models import Post
from .forms import CommentForm, RecipeForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def Register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def Login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def add(request):
    recipe_form = RecipeForm(request.POST or None)
    if request.method == "POST":
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False) # saves the recipe
            recipe.save()
            return redirect("home")
    else:
        return render(request, "add.html", {"recipe_form": recipe_form})
    
def comment(request, slug):
    template_name = 'comment.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})