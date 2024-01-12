class january():
        def division(self, a, b):
            self.a = a
            self.b  = b
            try:
                self.c = self.a / self.b
                print(self.c)
            except ZeroDivisionError:
                # result = self.c
                print("You can't divide by zero!")

obj = january()
obj.division(10, 0)
