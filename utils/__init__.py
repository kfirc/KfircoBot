class Owner:
    def __init__(self, **information):
        self.information = information

    def __getattr__(self, item):
        return self.information[item]

    def __str__(self):
        return '\n'.join([f'{key.title()}: {value}' for key, value in self.information.items()])
