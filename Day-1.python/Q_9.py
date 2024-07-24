#
cost_apple=15
cost_banana=4
cost_oranges=5
print("enter no of apples")
cost_apple=int(input())
print("enter no of bananas")
cost_bananas=int(input())
print("enter no of oranges")
cost_oranges=int(input())
print("enetr the amount given by mother")
print_given=int(input())
sum=(cost_apple*cost_apple)+(cost_bananas*cost_bananas)+(cost_oranges*cost_oranges)
if(sum<=amount_given):
    print("not cheated")
else:
    print("cheated")
 