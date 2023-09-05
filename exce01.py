wt = float(input("Weight :"))
unit = input("K-Kilogram or L-lbs ? ")
if unit.upper() == "K":
    final = (wt / 0.45)
    print("Final weight in lbs :"+ str(final))
else:
    final = (wt * 0.45)
    print("Final weight in kg :"+ str(final))
