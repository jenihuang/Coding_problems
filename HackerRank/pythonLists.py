if __name__ == '__main__':
    final = []
    N = int(input())
    for i in range(N):
        commandList = input().split()
        if commandList[0] == "print":
            print(final)
        elif commandList[0] == "insert":
            final.insert(int(commandList[1]),int(commandList[2]))
        elif commandList[0] == "remove":
            final.remove(int(commandList[1]))
        elif commandList[0] == "append":
            final.append(int(commandList[1]))
        elif commandList[0] == "sort":
            final.sort()
        elif commandList[0] == "pop":
            final.pop()
        elif commandList[0] == "reverse":
            final.reverse()

