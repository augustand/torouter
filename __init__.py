# -*- coding:utf-8 -*-


from inspect import getmembers, ismethod

from tornado import web
from tornado.web import HTTPError


def event(name_or_func):
    if callable(name_or_func):
        name_or_func._event_name = name_or_func.__name__
        return name_or_func

    def handler(f):
        f._event_name = name_or_func
        return f

    return handler


class BaseHandler(web.RequestHandler):
    def initialize(self):
        setattr(
            self,
            '_events',
            {e._event_name: e for _, e in getmembers(self, lambda x: ismethod(x) and hasattr(x, '_event_name'))}
        )

    def head(self, *args, **kwargs):
        _event_name = kwargs.get("event_name")
        if _event_name and _event_name in self._events:
            self._events[_event_name]()
        else:
            self.on_head(args, kwargs)

    def get(self, *args, **kwargs):
        _event_name = kwargs.get("event_name")
        if _event_name and _event_name in self._events:
            self._events[_event_name]()
        else:
            self.on_get(args, kwargs)

    def post(self, *args, **kwargs):
        _event_name = kwargs.get("event_name")
        if _event_name and _event_name in self._events:
            self._events[_event_name]()
        else:
            self.on_post(args, kwargs)

    def delete(self, *args, **kwargs):
        _event_name = kwargs.get("event_name")
        if _event_name and _event_name in self._events:
            self._events[_event_name]()
        else:
            self.on_delete(args, kwargs)

    def patch(self, *args, **kwargs):
        _event_name = kwargs.get("event_name")
        if _event_name and _event_name in self._events:
            self._events[_event_name]()
        else:
            self.on_patch(args, kwargs)

    def put(self, *args, **kwargs):
        _event_name = kwargs.get("event_name")
        if _event_name and _event_name in self._events:
            self._events[_event_name]()
        else:
            self.on_put(args, kwargs)

    def options(self, *args, **kwargs):
        _event_name = kwargs.get("event_name")
        if _event_name and _event_name in self._events:
            self._events[_event_name]()
        else:
            self.on_options(args, kwargs)

    def on_head(self, *args, **kwargs):
        raise HTTPError(405)

    def on_get(self, *args, **kwargs):
        raise HTTPError(405)

    def on_post(self, *args, **kwargs):
        raise HTTPError(405)

    def on_delete(self, *args, **kwargs):
        raise HTTPError(405)

    def on_patch(self, *args, **kwargs):
        raise HTTPError(405)

    def on_put(self, *args, **kwargs):
        raise HTTPError(405)

    def on_options(self, *args, **kwargs):
        raise HTTPError(405)
