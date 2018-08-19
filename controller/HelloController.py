from bast import Controller


class HelloController(Controller):
    def index(self):
        self.view('index.html')
