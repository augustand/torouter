# torouter
关于对tornado路由的一些设计

```
from handle import BaseHandler, event
class MainHandler(BaseHandler):
    def initialize(self, **kwargs):
        print kwargs

        BaseHandler.initialize(self)

    def on_get(self, *args, **kwargs):
        self.write("ok1111")
        self.finish()

    @event
    def click(self):
        print self.request.arguments
        self.write(self.request.arguments)

curl http://localhost:6751/todos.click?hello=22222&hello=3333
```