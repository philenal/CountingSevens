

### counts the number of numbers containing a 7 from 0 to 10^d-1 inclusive ###
def sevensInTenthPowers(d):
    return (10**d - 9**d)

### counts the number of numbers containing a 7 from 0 to s inclusive ###
def countSeven(s):
    s = str(s)
    d = len(s) - 1 # largest power of 10 that we can rewrite s in (i.e. d=3 if s = (a_3)*10^3 + (a_2)*10^2 + (a_1)*10^1 + (a_0)*10^0)
    count = 0
    while len(s) != 0:
        firstDigit = int(s[0]) # leftmost digit of s
        if (firstDigit == 7):
            # we count the number of 7's in [0,699] for example, but then we count all the numbers from [700, s]
            # there's an if else statement for the case where s=7 and we can't obtain an integer value at index 1 since it doesn't exist
            count += 7*sevensInTenthPowers(d) + int(s[1:]) + 1 if len(s) > 1 else 1
            s = "" # we don't need to look at s anymore since we already counted all of the numbers
        else:
            if (firstDigit > 7):
                # account for the special interval [700, 799] for example
                count += (firstDigit -1)*(sevensInTenthPowers(d)) + 10**d
            else:
                count += firstDigit*sevensInTenthPowers(d)

            s = s[1:]
        d -=1
    return count

### test cases ###
print("------------ TESTING countSeven ---------------")
print("There are ",countSeven(700), " numbers containing a 7 from 0 to 700") # s[0] = 7
print("There are ",countSeven(847), " numbers containing a 7 from 0 to 847") # s[0] > 7
print("There are ",countSeven(54), " numbers containing a 7 from 0 to 54") # s[0] < 7

print()

print("------------ TESTING sevensInTenthPowers ---------------")
print("There are ",sevensInTenthPowers(0), " numbers containing a 7 from 0 to 0") 
print("There are ",sevensInTenthPowers(2), " numbers containing a 7 from 0 to 99") 
print("There are ",sevensInTenthPowers(3), " numbers containing a 7 from 0 to 999") 