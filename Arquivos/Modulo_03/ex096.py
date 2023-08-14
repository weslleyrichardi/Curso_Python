def area(b, h):
    area = b * h
    print(f"A área do retângulo ({b:.1f} × {h:.1f}) é {area:.1f}m²")


area(float(input("Digite a base (m): ")), float(input("Digite a altura (m): ")))
