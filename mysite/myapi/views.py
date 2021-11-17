from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post, Preference
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer


@login_required
def create_post(request):
    if request.method == 'POST':
        if request.POST.get('caption'):  # and request.POST.get('image'):
            post = Post()
            post.caption = request.POST.get('caption')
            # post.image = request.POST.get('image')
            post.author = request.user
            post.save()

            return render(request, 'posts/create.html')

    else:
        return render(request, 'posts/create.html')


def home(request):
    all_posts = Post.objects.all()

    context = {'allposts': all_posts}

    return render(request, 'posts/home.html', context)


def detail_post_view(request, identity=None):
    each_post = get_object_or_404(Post, id=identity)

    context = {'eachpost': each_post}

    return render(request, 'posts/detail.html', context)


@login_required
def post_preference(request, post_id, user_preference):
    if request.method == "POST":
        each_post = get_object_or_404(Post, id=post_id)

        obj = ''

        value_obj = ''

        try:
            obj = Preference.objects.get(user=request.user, post=each_post)

            value_obj = obj.value  # value of user_preference

            value_obj = int(value_obj)

            user_preference = int(user_preference)

            if value_obj != user_preference:
                obj.delete()

                upref = Preference()
                upref.user = request.user

                upref.post = each_post

                upref.value = user_preference

                if user_preference == 1 and value_obj != 1:
                    each_post.likes += 1
                    each_post.dislikes -= 1
                elif user_preference == 2 and value_obj != 2:
                    each_post.dislikes += 1
                    each_post.likes -= 1

                upref.save()

                each_post.save()

                context = {'eachpost': each_post,
                           'postid': post_id}

                return render(request, 'posts/detail.html', context)

            elif value_obj == user_preference:
                obj.delete()

                if user_preference == 1:
                    each_post.likes -= 1
                elif user_preference == 2:
                    each_post.dislikes -= 1

                each_post.save()

                context = {'eachpost': each_post,
                           'postid': post_id}

                return render(request, 'posts/detail.html', context)

        except Preference.DoesNotExist:
            upref = Preference()

            upref.user = request.user

            upref.post = each_post

            upref.value = user_preference

            user_preference = int(user_preference)

            if user_preference == 1:
                each_post.likes += 1
            elif user_preference == 2:
                each_post.dislikes += 1

            upref.save()

            each_post.save()

            context = {'eachpost': each_post,
                       'postid': post_id}

            return render(request, 'posts/detail.html', context)

    else:
        each_post = get_object_or_404(Post, id=post_id)
        context = {'eachpost': each_post,
                   'postid': post_id}

        return render(request, 'posts/detail.html', context)
