class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

#modify print_from_stream to print out the first n numbers odd or even

def print_from_stream(n, stream=EvenStream()):
    if stream_name == "even":
    	stream = EvenStream()
    	for i in range(n):
    		print(stream.get_next())
    else:
    	for i in range(n):
        	print(stream.get_next())




queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())