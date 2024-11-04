import random 
def fortune(f):
    p=open(f,"r")
    print(random.choice(p.read().split('%')))
fortune("fortune.txt")
