from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

# Create your views here.
def addBlog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        picture = request.FILES.get('picture')
        dsc = request.POST.get('dsc')
        link = request.POST.get('link')

        blog = models.Blog(
        title = title,
        picture = picture,
        dsc = dsc,
        link = link)

        blog.save()
        messages.success(request,'Blog is Successfully Added!')
        return redirect('view_blog')
    return render(request, 'blogs/addBlog.html')

def viewBlog(request):
    blogs = models.Blog.objects.all()

    dict = {
        'blogs':blogs,
    }
    return render(request, 'blogs/viewBlog.html', context=dict)

def blogDetial(request, id):
    detial = models.Blog.objects.filter(id=id)

    dict = {
        'detial':detial,
    }
    return render(request, 'blogs/blogDetial.html', context=dict)

def editBlog(request, id):
    detial = models.Blog.objects.filter(id=id)
    id = id
    return render(request, 'blogs/editBlog.html', context={'detial':detial, 'id':id})

def updateBlog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        blog_id = request.POST.get('blog_id')
        picture = request.FILES.get('picture')
        dsc = request.POST.get('dsc')
        link = request.POST.get('link')

        blog = models.Blog.objects.get(id = blog_id)
        blog.title = title
        blog.picture = picture
        blog.dsc = dsc
        blog.link = link
        blog.created = blog.update

        blog.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_blog')

def deleteBlog(request, id):
    blog = models.Blog.objects.get(id = id)
    blog.delete()
    messages.success(request, 'Successfully Deleted!')
    return redirect('view_blog')