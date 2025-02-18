N=int(input())
if N%8== 1 or N%8==4:
    print("Lower")
elif N%8== 2 or N%8==5:
    print("Middle")
elif N%8== 3 or N%8==6:
    print("Upper")
elif N%8== 7:
    print("Side Lower")
else:
    print("Side Upper")
