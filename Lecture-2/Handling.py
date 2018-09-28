try:

    b =5467
    # a = 4567 / 0
    # print(a)

    file = open("hello.exe", "r")

except ZeroDivisionError as e:
    print("Hello from except")
except FileNotFoundError as e:
    print(e.filename, "not found")

except:
    print("Something went wrong. Please try again later")

