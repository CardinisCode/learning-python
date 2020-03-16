class Counter:
    def __init__(self):
        self.count = 0

def incrementor(c, num):
    c.count = c.count + 1
    print("c.count:", c.count)
    num += 1

def main():
    counter = Counter()
    num = 0
    for x in range(0, 100):
        incrementor(counter, num)
        
    return (counter.count, num)

aTuple = main()
print("aTuple:", aTuple)
    