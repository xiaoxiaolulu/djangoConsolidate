from front.models import User


def front_user(request):
    
    user_id = request.session.get('user_id')
    context = {}
    try:
        user = User.objects.get(pk=user_id)
        context['front_user'] = user
    except User.DoesNotExist:
        pass
    return context
