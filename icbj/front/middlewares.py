from front.models import User


def front_user_middleware(get_response):

    def middleware(request):
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user_id = User.objects.filter(pk=user_id).exists()
                request.front_user = user_id
            except User.DoesNotExist:
                pass
        return get_response(request)

    return middleware
