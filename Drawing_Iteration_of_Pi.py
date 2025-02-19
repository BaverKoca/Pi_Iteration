import turtle
import numpy as np
import time
import pygame
import time


screen = turtle.Screen()
screen.title("Write Pi's iteartion")

screen.bgcolor("black") # Change background color from there

pi_turtle = turtle.Turtle()

speed_of_p = pi_turtle.speed(10) # Speed of drawing

theta_degrees = np.linspace(0, 113*360, 10000)
theta_radians = np.deg2rad(theta_degrees)
z = np.exp(theta_radians * 1j) + np.exp(np.pi * theta_radians * 1j)
x = np.real(z)
y = np.imag(z)

music_file_path = "You can write file path here"  # Don't forget to write .mp3 too
pygame.mixer.init()
pygame.mixer.music.load(music_file_path)
pygame.mixer.music.play()

pi_turtle.penup()
pi_turtle.color("White")
for i in range(len(x)):
    pi_turtle.goto(x[i] * 100, y[i] * 100)
    pi_turtle.pendown()
    
screen.exitonclick()
