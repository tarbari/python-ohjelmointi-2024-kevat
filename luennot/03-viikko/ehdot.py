nums = [1, 2, 2]
nums2 = nums

if nums == nums2:
    print("nums == nums2")

if nums is nums2:
    print("nums is nums2")

nums.append(123)
print(nums2)

# if 3 not in nums:
#     print("3 ei löytyy")
#
#
# alive = False
#
# print("it's alive!") if alive is True else print("they dead")
# a = True
# b = True
#

# if a or b:
#     print("Totta")
# else:
#     print("muu asia")
#
# c = 11
# # xor
# if a ^ b:
#     print("asd")
#
# if c == 3:
#     print("joo")
# elif c == 10:
#     print("10 on paras")
# else:
#     print("ei")
