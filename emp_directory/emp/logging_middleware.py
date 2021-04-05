""" This middleware will log all the incoming requets """
import datetime
import json


class LoggingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        path = request.path
        try:
            payload = json.loads(request.body.decode('utf-8'))
        except:
            payload = {}
        start_time = datetime.datetime.now()
        method = request.method

        resp = self.get_response(request)

        end_time = datetime.datetime.now()
        if path in ['/admin/jsi18n/', '/favicon.ico']:
            return resp
        print({
            'requested_user': user,
            'payload': payload,
            'path': path,
            'method': method,
            'request_ttl': end_time-start_time,

        })
        return resp
