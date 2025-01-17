# Q116) Implement a context manager using the with statement that opens a file, writes text, and closes the file automatically.
class FileWriter:
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file 
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False
with FileWriter('example.txt') as f:
    f.write("Hello, this is a test line written to the file.")
print("Text has been written to the file and the file is automatically closed.")
