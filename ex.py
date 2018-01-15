import threading

def sum(low, high):
    total = 0
    for i in range(low,high):
        total += i
    print("subthread",total)

t=threading.Thread(target=sum(1,10))
t.start()

print("Main Thread")