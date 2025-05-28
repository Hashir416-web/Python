class bird:
    def __init__(self):
        print("Bird is ready")
    def whoisthe(self):
        print("Bird")
        def swim(self):
            print("Swim faster")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisthe(self):
        print("Penguin")
    def run(self):
        print("Run faster")
peggy = penguin()
peggy.whoisthe()
peggy.run()