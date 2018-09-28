def eat():
    print("Something but no return")


def run(kms):
    print("I ran this much " + str(kms))


def sleep(comfort, balance):
    sat = comfort * 10
    return sat

sleep(6, balance= 10)

com = int(input("Enter comfort level : "))

print("my satisfaction is" + str(sleep(6)))