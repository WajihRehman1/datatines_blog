from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.core.mail import send_mail
from django.db.models import Count, Q
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import DetailView, CreateView, DeleteView
from .models import post, comment
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def catagory_count():
    queryset = post.objects.values('catagories__title').annotate(Count('catagories__title'))
    return queryset


def index(request):
    featured = post.objects.filter(featured=True)
    latest = post.objects.order_by('-timestamp')[0:3]
    context = {'object': featured, 'latest': latest}
    return render(request, 'blogApp/index.html', context)


def blog(request):
    catagory_counts = catagory_count()
    post_list = post.objects.all()
    recent = post.objects.order_by('-timestamp')[:3]
    paginator = Paginator(post_list, 6)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    return render(request, 'blogApp/blog.html', {'queryset': paginated_queryset, ' page_request_var': page_request_var,
                                                 'recent': recent, 'catagory_counts': catagory_counts})


def search_post(request):
    queryset = post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)

        ).distinct()

    context = {
        'queryset': queryset
    }
    return render(request, 'blogApp/search_results.html', context)


class Post(DetailView):
    context_object_name = 'post'
    model = post
    template_name = 'blogApp/post.html'

    def get_context_data(self, **kwargs):
        context = super(Post, self).get_context_data(**kwargs)
        context['recent'] = post.objects.order_by('-timestamp')[:3]
        context['catagory_counts'] = catagory_count()
        po = self.kwargs['pk']
        context['comments'] = post.objects.all()
        name = self.request.user
        userComment = self.request.GET.get('comment')
        modelInstance = comment()
        if name != None and userComment != None:

            modelInstance.user=name
            modelInstance.content = userComment
            modelInstance.Post = post.objects.get(id=po)
            modelInstance.save()

        return context


def checkCatagories(request):
    queryset = post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)

        ).distinct()

    context = {
        'queryset': queryset
    }
    return render(request, 'blogApp/search_results.html', context)


def contactMail(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        msg = "Email : " + email + " has subscribed to DATA-TINES BLOG"
        send_mail(
            'Subscription to DATA_TINES',
            msg,
            settings.EMAIL_HOST_USER,
            ['mwajihrehman@gmail.com', 'syedabdullah199758@gmail.com','ahmedaslam283@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'blogApp/index.html')


def adminLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('blogApp:index'))

            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse("Wroong details")
    else:
        return render(request, 'blogApp/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blogApp:index'))

