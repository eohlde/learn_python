class ExampleClass(object):
    list_of_instances = []

    def __init__(self):
        self.instance_number = len(self.list_of_instances) + 1
        self.list_of_instances.append(self)

x = ExampleClass()
y = ExampleClass()

print("Hello World")