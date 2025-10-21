import math

def z1(a,fi):
    return (math.pow(math.sin(3*a),-2)+math.cos(7*a)-math.sin(6*a))/(math.tan(a)+fi-2*a)
def z2(a):
    return (13*math.pow(math.tan(a),2)-54*math.tan(a)+98)
print(z1(math.pi/2,math.pi))
print(z2(math.pi/3))
