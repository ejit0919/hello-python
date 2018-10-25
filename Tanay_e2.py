import sys

if float(sys.argv[1]) >= 220: 
    print("Super Typhoon")
elif float(sys.argv[1]) >= 118 and float(sys.argv[1]) <220:
    print("Typhoon")
elif float(sys.argv[1]) >= 89 and float(sys.argv[1]) <118:
    print("Severe Tropical Storm")
elif float(sys.argv[1]) >= 62 and float(sys.argv[1]) <89:
    print("Tropical Storm")
elif float(sys.argv[1]) <=61 :
    print("Tropical Depression")