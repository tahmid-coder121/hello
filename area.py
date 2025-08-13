a,b,c = map(float,input().split())
pi = 3.14159
TRIANGULO = 0.5*a*c 
print(f"TRIANGULO: {TRIANGULO:.3f}")

CIRCULO = pi * c**2
print(f"CIRCULO: {CIRCULO:.3f}")

TRAPEZIO = 0.5 * (a + b)*c
print(f"TRAPEZIO: {TRAPEZIO:.3f}")

QUADRADO = b*b
print(f"QUADRADO: {QUADRADO:.3f}")

RETANGULO = a*b
print(f"RETANGULO: {RETANGULO:.3f}")
