
import kavya as kv

from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.datastructures import State
class InitRequestStateMiddleware:
  def __init__(self, app):
      self.app = app

  async def __call__(self, scope, receive, send):
      if scope['type'] == 'http':
          request = Request(scope)
          # Initialize request.state
          request.state.form_data = State()

      await self.app(scope, receive, send)

      pass
  pass

app  = kv.build_app(middlewares=[Middleware(InitRequestStateMiddleware)
                                   ]
                    )

      

