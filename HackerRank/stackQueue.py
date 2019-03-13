import sys

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
    def pushCharacter(self,letter):
        self.stack.append(letter)
    def popCharacter(self):
        return self.stack.pop()
    def enqueueCharacter(self,letter):
        self.queue.insert(0,letter)
    def dequeueCharacter(self):
        return self.queue.pop()

s = 'kayak'
obj = Solution()

for i in range(len(s)):
	obj.pushCharacter(s[i])
	obj.enqueueCharacter(s[i])

isPalindrome = True


for i in range(len(s)//2):
	if obj.popCharacter() != obj.dequeueCharacter():
		isPalindrome = False
		break
print(isPalindrome)

