from bast import Route

route = Route()
route.get('/', 'TestController.index')
route.get('/hello', 'TodoController.index')