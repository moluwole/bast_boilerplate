from bast import Controller


class TestController(Controller):
    def index(self):
        self.view('index.html')
