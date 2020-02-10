from django.urls import converters, register_converter


class CategoryConverter(object):

    regex = r'\w+|(\w+\+\w+)+'

    def to_python(self, value):
        # python + django + flask
        # [python, django, flask]
        result = value.split("+")
        return result

    def to_value(self, value):
        # [python, django, flask]
        # python + django + flask
        if isinstance(value, list):
            result = "+".join(value)
            return result
        else:
            raise RuntimeError("参数必须为列表")


register_converter(CategoryConverter, 'cate')
