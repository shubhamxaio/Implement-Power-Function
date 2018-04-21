class Solution:
    def pow(self, x, n, d):
        if d == 1: return 0

        rem = x % d
        p = 1
        while n > 0:
            if n % 2 == 1:
                p *= rem
                p %= d
            n /= 2
            rem = rem**2 % d

        return p


if __name__ == '__main__':
    x, n, d = int(input()), int(input()), int(input())
    print(Solution().pow(x, n, d))