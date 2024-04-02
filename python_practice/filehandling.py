import os
class test():
    def writefile(self, file, write):
        self.file = file
        self.text = write
        self.file = open(self.file, "w")
        self.file.write(self.text)
        self.file.close()
    def readfile(self, change):
        self.c = change
        self.f = open(self.c, 'r')
        print(self.f.read())
        self.f.close()
    def removefile(self, remove):
        self.r = remove
        if os.path.exists(self.r):
            os.remove(self.r)
            print("File Removed successfully")
        else:
            print("The file does not exist")

obj = test()
obj.writefile("newfile2.txt", "lorem ipsum testing by deepak")
obj.readfile("newfile2.txt")
os.rename("makedir.py", "filehandling.py") #please check the file path then excute the code
obj.removefile("newfile2.txt") #first comment rename file then remove our file

