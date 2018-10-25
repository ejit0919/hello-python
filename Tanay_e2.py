import sys

wind = float(sys.argv[1])

if wind >= 220: 
    print("Super Typhoon")
elif wind >= 118 and wind <220:
    print("Typhoon")
elif wind >= 89 and wind <118:
    print("Severe Tropical Storm")
elif wind >= 62 and wind <89:
    print("Tropical Storm")
elif wind <=61 :
    print("Tropical Depression")