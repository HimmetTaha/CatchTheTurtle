import time
import turtle
from random import randint

score = 0
time_left = 30

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("light blue")
screen.title("Catch the Turtle")

# Sembol için turtle oluşturduk
t = turtle.Turtle()
t.speed(0)
t.shape("turtle")
t.color("green")
t.shapesize(1.5, 1.5, 1)

# Sayaç için turtle oluşturuyoruz
counter = 0
counter_turtle = turtle.Turtle()
counter_turtle.penup()
counter_turtle.hideturtle()
counter_turtle.goto(-380, 260)  # Sayaç metnini sola taşıdık
counter_turtle.write("Tıklama Sayısı: {}".format(counter), align="left", font=("Arial", 16, "normal"))

# Süre için turtle oluşturuyoruz
timer = 30
timer_turtle = turtle.Turtle()
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(300, 260)  # Timer metnini sağa taşıdık

# Tıkaldığımızı algılıyor burası
def update_counter(x, y):
    global counter
    counter += 1
    counter_turtle.clear()
    counter_turtle.write("Tıklama Sayısı: {}".format(counter), align="left", font=("Arial", 16, "normal"))

# Tıklama olayını bağlama
t.onclick(update_counter)

start_time = time.time()
while True:
    x = randint(-300, 200)
    y = randint(-200, 200)

    t.penup()
    t.goto(x, y)
    t.pendown()

    screen.update()

    elapsed_time = int(time.time() - start_time)
    time_left = max(0, timer - elapsed_time)

    # Timer'ı göstermek için güncellemeyi burada yapıyoruz
    timer_turtle.clear()
    timer_turtle.write("Süre: {}".format(time_left), align="right", font=("Arial", 16, "normal"))  # Sağa hizalama

    time.sleep(0.5)

    if time_left == 0:
        break

turtle.done()
