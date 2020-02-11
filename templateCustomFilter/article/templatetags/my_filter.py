from django import template


register = template.Library()


def greet(value, world=None):
    """
    过滤器最多有两个参数
    :param value: 
    :return: 
    """
    return value+world

register.filter("greet", greet)
