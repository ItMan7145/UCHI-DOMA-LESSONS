class Queue:
    def __init__(self):
        self.queue = list()

    def push(self, val):
        if val not in self.queue:
            self.queue.insert(0, val)

    def pop(self):
        if len(self.queue) > 0:
            print(self.queue.pop())

    def size(self):
        print(len(self.queue))


que = Queue()

num = int(input())
for i in range(num):
    cmd = input()
    if 'push' in cmd:
        cmd = cmd.split()
        value = int(cmd[1])
        que.push(value)
    elif cmd == 'pop':
        que.pop()
    elif cmd == 'size':
        que.size()
