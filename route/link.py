from bast import Route
from controller.test_controller import TestController

route = Route()
route.get('/', TestController, 'index')