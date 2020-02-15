from front.models import User


def front_user_middleware(get_response):

    def middleware(request):
        print("request到达view之前执行的代码")
        user_id = request.session.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
            request.front_user = user
        except User.DoesNotExist:
            request.front_user = None
        response = get_response(request)
        print("response到达浏览器之前执行的代码")
        return response

    return middleware
