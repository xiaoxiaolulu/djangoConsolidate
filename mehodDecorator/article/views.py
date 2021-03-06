import json

from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render, redirect, reverse
from django.utils.decorators import method_decorator

from article.models import Article
from django.views.decorators.http import require_http_methods, require_GET
from django.core.handlers.wsgi import WSGIRequest
from django.template import loader
from django.views.generic import View, TemplateView, ListView


# @require_http_methods(['GET'])
@require_GET
def index(request):

    article = Article.objects.all()
    return render(request, 'index.html', context={'articles': article})


@require_http_methods(['POST'])
def add(request):
    t = request.POST.get('title')
    c = request.POST.get('content')
    Article.objects.create(title=t, content=c)
    return HttpResponse("success")


def home(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("home")
    else:
        return redirect(reverse('signup'))


def signup(request):
    print(request)
    return HttpResponse("sign")


def index02(request):
    person = {
        "name": "hahah"
    }
    # p_str = json.dumps(person)
    # return HttpResponse(p_str, content_type='application/json')
    return JsonResponse(person)


def csv(request):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename='abc.csv"
    writer = csv.writer(response)
    writer.writerow(['user', 'age'])
    writer.writerow(['hahah', 18])
    return response


def csv_template(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename='abc.csv"
    content = {
        "rows": [
            ['username', 'age'],
            ['sahssda', 18]
        ]
    }
    template = loader.get_template('abc.txt')
    csv_template = template.render(content)
    response.content = csv_template
    return response


def large_csv(request):
    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename='large.csv"
    rows = ("Row {} {}\n".format(row, row) for row in range(0, 10000))
    # response.streaming_content = ("username, age\n", "sasda, 18\n")
    response.streaming_content = rows
    return response


class BookListView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("哈哈哈")


class AddBookViews(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'add_book.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        author = request.POST.get('author')
        print(name, author)
        return HttpResponse('成功')


class AboutView(TemplateView):

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = {'phone': '12313131'}
        return context


def add_article(request):
    articles = []
    for x in range(0, 102):
        article = Article(title=f"标题{x}", content=f"内容{x}", price=x)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse("添加成功")


class ArticleListView(ListView):

    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(*kwargs)
        context['username'] = 'was'
        paginator = context.get('paginator')
        # print(paginator.count)
        # print(paginator.num_pages)
        # print(paginator.page_range)
        page = context.get('page_obj')
        # print(page.has_next())
        # print(page.next_page_number())
        pagination_data = self.get_pagination_data(paginator, page)
        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page-around_count, current_page)

        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page+1, num_pages+1)
        else:
            right_has_more = True
            right_pages = range(current_page+1, current_page+around_count+1)
        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages
        }

    # def get_queryset(self):
    #     return Article.objects.filter(id__lte=2)


def login_required(func):

    def wrapper(request, *args, **kwargs):
        username = request.GET.get('username')
        if username:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('index'))

    return wrapper


@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    def get(self, request):
        return HttpResponse("个人中心")

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ProfileView, self).dispatch(request, *args, **kwargs)


def index010(request):
    a = 0
    b = 1
    c = b/a
    return HttpResponse('首页')