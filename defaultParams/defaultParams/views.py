from django.http import HttpResponse


books = [
    "桑国演义",
    "大萨达撒",
    "卫栖梧群二群",
    "啦啦啦啦啦"
]


def book_list(request, page_id=0):
    return HttpResponse(books[page_id])
