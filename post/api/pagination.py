from rest_framework.pagination import(PageNumberPagination ,LimitOffsetPagination)


class LimitPagination(LimitOffsetPagination):
	default_limit=2
	max_limit=10


class PagePagination(PageNumberPagination):
	page_size =2 