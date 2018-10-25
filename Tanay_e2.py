import sys

if int(sys.argv[1]) >= 220: 
    print("Super Typhoon")
elif int(sys.argv[1]) >= 118 and int(sys.argv[1]) <220:
    print("Typhoon")
elif int(sys.argv[1]) >= 89 and int(sys.argv[1]) <118 :
    print("Severe Tropical Storm")
elif int(sys.argv[1]) >= 62 and int(sys.argv[1]) <89:
    print("Tropical Storm")
elif int(sys.argv[1]) <=61 :
    print("Tropical Depression")