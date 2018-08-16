from bast import Controller

class TodoController(Controller):
    def index(self):
    	self.view('hello-world.html')