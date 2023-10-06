# bounce.py
#
# Exercise 1.5

ball_height = 100
energy_remaining = 3 / 5
bounce_count = 1

while bounce_count <= 10:
    ball_height = ball_height * energy_remaining
    print(bounce_count, round(ball_height, 4))
    bounce_count += 1