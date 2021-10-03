class Solution:
    def reverse(self, num):
        if num >= -2**31 and num <= 2**31 - 1:
            reversed_num = 0
            if (num < 10 and num > 0) or (num > -10 and num < 0):
                print("Number has only one digit, can't reverse!")
                return num
            else:
                while num != 0:
                    reversed_num *= 10
                    reversed_num += num - int((num / 10)) * 10
                    num /= 10
                    num = int(num)
            return reversed_num
        else:
            print("Out of bounds, exiting...")
            return 0

x = Solution()
print(x.reverse(1534236469))