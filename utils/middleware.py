class UrlPathRecordMiddleware(object):
    """记录用户访问地址中间间类"""
    exclude_path = ['/user/login/', '/user/register/', '/user/logout/']

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """记录用户访问地址"""
        if request.path not in UrlPathRecordMiddleware.exclude_path and not request.is_ajax():
            # 记录这个地址
            request.session['pre_url_path'] = request.path

#
# class UrlPathRecordMiddleware(object):
#     """记录用户访问地址中间间类"""
#     exclude_path = ['/user/login/', '/user/register/', '/user/logout/']
#
#     def process_view(self, request, view_func, *view_args, **view_kwargs):
#         """记录用户访问地址"""
#         if request.META.get('HTTP_X_FORWARDED_FOR'):
#             ip = request.META['HTTP_X_FORWARDED_FOR']
#         else:
#             ip = request.META['REMOTE_ADDR']


