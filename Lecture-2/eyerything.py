print(type(3))

print(int)
print(type([]))


def run():
    print("Run Berry Run")


def run(name):
    print("Run Run" + name)




b = run

run()
b()

print(type(run))
