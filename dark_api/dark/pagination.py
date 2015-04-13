from rest_framework.pagination import (
    PageNumberPagination as BasePageNumberPagination,
    replace_query_param,
)


class PageNumberPagination(BasePageNumberPagination):
    """
    Warning: this is brittle. This is shadowing an undocumented internal API of
    Django REST Framework, to get it to be consistent about including the `page`
    parameter for the first page as for all others.
    """
    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.previous_page_number()
        return replace_query_param(url, self.page_query_param, page_number)
