def help(name, work):
    print("help " + name + " in " + work)


help(work="anuj", name="analytics")

print("Hello", end="  ")
print("Bello")


l = [4356, 67, 567, 567]

# for item in l:
#     print(str(item), end=", ")
#
# print()

# def sqr(x):
#     return x*x


updated = list(map(lambda x: print(x), l))

print(updated)

