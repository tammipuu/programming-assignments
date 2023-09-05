from random import uniform

points = int(input('Syötä arvottavat pisteet: '))
points_inside = 0   # circle

for f in range(points):
    x = uniform(0, 1)
    y = uniform(0, 1)
    if pow(x, 2) + pow(y, 2) < 1:
        points_inside += 1

approx_pi = 4 * points_inside / points
print(f'Piin likiarvo: {approx_pi}')