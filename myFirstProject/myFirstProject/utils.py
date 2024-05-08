menu = {'key_1': 'Главная',
        'key_2': 'Сравнить!',
        'key_3': 'Картинки',
        'key_4': 'Про нас',
        'key_5': 'Добавить картинку'}


class DataMixin:
    paginate_by = 5
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
        if 'dict' not in self.extra_context:
            self.extra_context['dict'] = menu
        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        context['dict'] = menu
        context['cat_selected'] = None
        context.update(kwargs)
        return context
