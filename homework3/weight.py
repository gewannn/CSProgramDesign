EarthWeight = float(input("输入你现在的体重,单位为kg： "))


for i in range (1,11):
    EarthWeight += 0.5 
    MoonWeight = EarthWeight * 0.165
    print(f"{i}年后，你在地球上的体重为{EarthWeight}kg,你在月球上的体重为{MoonWeight:.2f}kg")
