from django.utils.deprecation import MiddlewareMixin
import time


class ArgumentLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start = time.time()
        print('Calling {0}'.format(request))

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('Calling {0}.{1}'.format(callback.__module__, callback.__name__))
        print('Arguments: {}'.format(callback_kwargs or (callback_args,)))

    def process_response(self, request, response):
        response.write('<p>Response elapsed time: {:.2f}</p>'.format(time.time() - self.start))
        return response
