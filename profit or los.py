actualcost=float(input("actual cost :"))
sellingcost= float(input("Selling cost :"))
profit=sellingcost-actualcost
if actualcost>sellingcost:
    print("loss")
else:
    print("profit={0}and selling price is {1}".format(profit,sellingcost) )