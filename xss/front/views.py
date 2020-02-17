from django.shortcuts import render, redirect, reverse


# Create your views here.
from django.views.decorators.http import require_http_methods

from front.models import Comment


def index(request):
    context = {
        'comments': Comment.objects.all()
    }
    return render(request, 'index.html', context=context)


@require_http_methods(['POST'])
def add_comment(request):
    # from django.template.defaultfilters import escape
    #
    # content = request.POST.get('content')
    # content = escape(content)
    # Comment.objects.create(content=content)

    import bleach
    from bleach.sanitizer import ALLOWED_ATTRIBUTES, ALLOWED_TAGS
    content = request.POST.get('content')
    cleaned_data = bleach.clean(content, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
    Comment.objects.create(content=cleaned_data)
    return redirect(reverse('index'))