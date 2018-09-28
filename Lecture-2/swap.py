# a = input()
# # b = input()
# #
# # a, b = b, a
# #
# # print(a, b, sep=", ")

print(type((2,5,)))

a = 6, 7

print(a + a)


def add(*nums):
    # print(type(nums))

    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return nums[0] + nums[1]

    if len(nums) > 2:
        return add(nums[0] + nums[1], *nums[2:])


print(add(3, 6, 7))

sum((456, 47, 5))


# a = ("anuj", "moh", "34", "moh")
#
# l = list(set(a))
#
# l.sort()
#
# print(l)









