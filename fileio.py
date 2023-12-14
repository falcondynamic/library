import csv
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:0.3f} seconds to execute")
        return result
    return wrapper

class FileIO:
    def __init__(self,filename):
        self.filename = filename

    @timing_decorator
    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()
 
    @timing_decorator
    def write(self, data):
        with open(self.filename, 'w') as file:
            return file.write(data)
        
    def append(self,data):
        with open(self.filename, 'a') as file:
            return file.write(data)
    

class FileCSV:
    def __init__(self,filename):
        self.filename = filename

    @timing_decorator
    def read(self):
        with open(self.filename, 'r') as file:
            csv_data = csv.reader(file)
            return list(csv_data)
    
    @timing_decorator
    def read_dict(self):
        with open(self.filename, 'r') as file:
            books = csv.DictReader(file)
            return list(books)