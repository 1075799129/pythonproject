data = [True,True,False]

if any(data):
    print("At least one True")
if all(data):
    print("Not one False")
if any(data) and not all(data):
    print("At least one True and one False")