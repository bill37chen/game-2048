__author__ = 'Bill'
import random


class game():
    def __init__(self):
        self.list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.length = 4
        self.result = False
        self.msg = ""

    def random(self):
        if self.list.count(2048) > 0:
            self.result = True
            self.msg = "Win!"
        else:
            x = random.choice([2, self.length])
            zero_list = [i for i, value in enumerate(self.list) if value == 0]
            if len(zero_list) == 0:
                self.result = True
                self.msg = "Lost!"
            else:
                position = random.choice(zero_list)
                self.list[position] = x

    def move(self, direction):
        if direction == "W":
            for i in range(self.length):
                column = i
                templist = []
                for j in range(self.length):
                    row = j
                    index = row * self.length + column
                    if self.list[index] != 0:
                        templist.append(self.list[index])
                if len(templist) > 1:
                    cindex = 0
                    while cindex < len(templist) - 1:
                        if templist[cindex] == templist[cindex + 1]:
                            templist[cindex] *= 2
                            templist.pop(cindex + 1)
                        else:
                            cindex += 1
                count = len(templist)
                for zeronum in range(self.length-count):
                    templist.append(0)
                for j in range(self.length):
                    row = j
                    index = column + row * self.length
                    self.list[index] = templist[row]
        elif direction == "S":
            for i in range(self.length-1, -1, -1):
                column = i
                templist = []
                for j in range(self.length-1, -1, -1):
                    row = j
                    index = row * self.length + column
                    if self.list[index] != 0:
                        templist.append(self.list[index])
                if len(templist) > 1:
                    cindex = 0
                    while cindex < len(templist) - 1:
                        if templist[cindex] == templist[cindex + 1]:
                            templist[cindex] *= 2
                            templist.pop(cindex + 1)
                        else:
                            cindex += 1
                count = len(templist)
                for zeronum in range(self.length-count):
                    templist.append(0)
                templist.reverse()
                for j in range(self.length-1, -1, -1):
                    row = j
                    index = column + row * self.length
                    self.list[index] = templist[row]
        elif direction == "A":
            for i in range(self.length):
                row = i
                templist = []
                for j in range(self.length):
                    column = j
                    index = column + row * self.length
                    if self.list[index] != 0:
                        templist.append(self.list[index])
                if len(templist) > 1:
                    cindex = 0
                    while cindex < len(templist) - 1:
                        if templist[cindex] == templist[cindex + 1]:
                            templist[cindex] *= 2
                            templist.pop(cindex + 1)
                        else:
                            cindex += 1
                count = len(templist)
                for zeronum in range(self.length-count):
                    templist.append(0)
                for j in range(self.length):
                    column = j
                    index = column + row * self.length
                    self.list[index] = templist[column]
        elif direction == "D":
            for i in range(self.length-1, -1, -1):
                row = i
                templist = []
                for j in range(self.length-1, -1, -1):
                    column = j
                    index = column + row * self.length
                    if self.list[index] != 0:
                        templist.append(self.list[index])
                if len(templist) > 1:
                    cindex = 0
                    while cindex < len(templist) - 1:
                        if templist[cindex] == templist[cindex + 1]:
                            templist[cindex] *= 2
                            templist.pop(cindex + 1)
                        else:
                            cindex += 1
                count = len(templist)
                for zeronum in range(self.length-count):
                    templist.append(0)
                templist.reverse()
                for j in range(self.length-1, -1, -1):
                    column = j
                    index = column + row * self.length
                    self.list[index] = templist[column]

    def show(self):
        if self.result:
            print self.msg
        else:
            for i in range(self.length):
                row = i
                output = ""
                for j in range(self.length):
                    column = j
                    output += str(self.list[row * self.length + column]).rjust(8)
                print output

    def run(self, direction):
        self.move(direction)
        self.random()
        self.show()

    def start(self):
        self.random()
        self.random()
        self.show()