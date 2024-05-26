menu = [{'key': 'Главная', 'url_name': 'home'},
        {'key': 'Оценить!', 'url_name': 'assess'},
        {'key': 'Картинки', 'url_name': 'photos'},
        {'key': 'Про нас', 'url_name': 'about'},
        {'key': 'Добавить картинку', 'url_name': 'addpage'}
        ]


class DataMixin:
    #paginate_by = 5
    title_page = None
    content_page = None
    cat_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page
            self.extra_context['content'] = self.title_page
        if self.content_page:
            self.extra_context['content'] = self.content_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context
