# Импорт необходимых библиотек
import pygame
import math
import threading
import random

# Класс для представления планеты
class Planet:
    def __init__(self, x, y, radius, angular_velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = random.uniform(0, 360)  # Начальный угол для разнообразия движения
        self.angular_velocity = angular_velocity

    # Функция для обновления координат планеты для движения по кругу
    def update_position(self):
        self.x = self.radius * math.cos(math.radians(self.angle)) + 200
        self.y = self.radius * math.sin(math.radians(self.angle)) + 200
        self.angle += self.angular_velocity

# Функция для отрисовки планет
def draw_planet(screen, x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 5)

# Функция для отрисовки экрана
def draw_screen(screen, planets):
    screen.fill((0, 0, 0))
    for planet in planets:
        draw_planet(screen, int(planet.x), int(planet.y))
    pygame.display.flip()

# Функция для обновления координат планет в отдельном потоке
def update_planets(planets):
    while True:
        for planet in planets:
            planet.update_position()
        pygame.time.delay(10) # Скорость вращения планет(чем меньше значение, тем больше скорость)

# Создание планет
planets = []

# Параметры планет
num_planets = 5

# Создание нескольких планет с уникальными значениями радиуса и угловой скорости
for i in range(num_planets):
    radius = random.randint(50, 150)  # Случайный радиус для каждой планеты
    angular_velocity = random.uniform(0.5, 2)  # Случайная угловая скорость
    planet = Planet(200, 200, radius, angular_velocity)
    planets.append(planet)

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Planet")

# Запуск потока для обновления координат планет
thread = threading.Thread(target=update_planets, args=(planets,))
thread.start()

# Цикл отрисовки экрана
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_screen(screen, planets)

pygame.quit()
