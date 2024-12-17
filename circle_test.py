from PIL import Image
import pygame
import time
import os
import sys

PYGAME_DETECT_AVX2=1

def circle(r, xc, yc, img):
    x = 0
    y =  r
    d = 0
    #d = 2*((x+1)*(x+1) + (y-1)*(y-1) - r*r) + 2*y - 1 
    while x <= y:
        if d > 0:
            y -= 1
            d += 4*x - 4*y + 10
        else:
            d += 4*x + 6
            
        img.putpixel((xc + x, yc - y), (20, 90, 100))
        img.putpixel((yc + y, xc - x), (20, 90, 100))
        img.putpixel((yc + y, xc + x), (20, 90, 100))
        img.putpixel((xc + x, yc + y), (20, 90, 100))
        img.putpixel((xc - x, yc + y), (20, 90, 100))
        img.putpixel((yc - y, xc + x), (20, 90, 100))
        img.putpixel((yc - y, xc - x), (20, 90, 100))
        img.putpixel((xc - x, yc - y), (20, 90, 100))
        x+=1

def test_0():
    # Собственная функция
    start_time = time.time()
    for i in range(0, 1001):
        k = i / 10
        img = Image.new('RGB', (1000, 1000), 'black')
        circle(499, 500, 500, img)
        sys.stdout.write("\r%d%%" % k)
        sys.stdout.flush()
        
    img.save('test_0.png')
    print('\ntest_0 My function execution time = ' + str(time.time() - start_time))

        # Функция из библиотеки pygame
    start_time = time.time()

    window = pygame.display.set_mode((1000, 1000))

    active = True
    for i in range(0, 1001):
        pygame.draw.circle(window, (255, 0, 0), (500, 500), 499, 1)  # Рисуем круг
    pygame.display.update()
    print('test_0 Pygame function execution time = ' + str(time.time() - start_time) + '\n====================')
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
   

def test_1():
    # Собственная функция
    start_time = time.time()
    img = Image.new('RGB', (1000, 1000), 'black')
    for r in range(10, 499):
        circle(r, 500, 500, img)
    img.save('test_1.png')
    print('test_1 My function execution time = ' + str(time.time() - start_time))

    # Функция из библиотеки pygame
    start_time = time.time()

    window = pygame.display.set_mode((1000, 1000))
    active = True
    for r in range(10, 499):
        pygame.draw.circle(window, (255, 0, 0), (500, 500), r, 1)  # Рисуем круг
    img.save('test_1.png')
    pygame.display.update()
    print('test_1 Pygame function execution time = ' + str(time.time() - start_time) + '\n====================')
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
   


def test_2():
    start_time = time.time()
    img = Image.new('RGB', (1000, 1000), 'black')
    for x in range(50, 951, 30):
        for y in range(50, 951, 30):
            circle(40, x, y, img)
    img.save('test_2.png')
    print('test_2 execution time = ' + str(time.time() - start_time))

    # Функция из библиотеки pygame
    start_time = time.time()

    window = pygame.display.set_mode((1000, 1000))
    active = True
    for x in range(50, 951, 30):
        for y in range(50, 951, 30):
            pygame.draw.circle(window, (255, 0, 0), (x, y), 40, 1)  # Рисуем круг
    
    pygame.display.update()

    print('test_2 Pygame function execution time = ' + str(time.time() - start_time) + '\n====================')
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

def test_3():
    start_time = time.time()
    img = Image.new('RGB', (1000, 1000), 'black')
    for x in range(50, 951, 20):
        for y in range(50, 951, 20):
            circle(5, x, y, img)
    img.save('test_3.png')
    print('test_3 execution time = ' + str(time.time() - start_time))

    # Функция из библиотеки pygame
    start_time = time.time()

    window = pygame.display.set_mode((1000, 1000))
    active = True
    for x in range(50, 951, 20):
        for y in range(50, 951, 20):
            pygame.draw.circle(window, (255, 0, 0), (x, y), 5, 1)  # Рисуем круг
    
    pygame.display.update()

    print('test_3 Pygame function execution time = ' + str(time.time() - start_time) + '\n====================')
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False



pygame.init()
print('====================')
test_0()
#test_1()
#test_2()
#test_3()