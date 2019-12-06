class ExampleClass(object):
    list_of_instances = []

    def __init__(self):
        self.instance_number = len(self.list_of_instances) + 1
        self.list_of_instances.append(self)

x = ExampleClass()
y = ExampleClass()

print(f"x has instance number {x.instance_number}")
print(f"y has instance number {y.instance_number}")
print(f"There are {ExampleClass.list_of_instances.__len__()} instances of the class")
print(f"x knows that there are {x.list_of_instances.__len__()} number of instances")
print(f"y knows that there are {y.list_of_instances.__len__()} number of instances")