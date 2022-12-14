#
# URL:
# https://www.codingame.com/ide/puzzle/mars-lander-episode-3
#
# My Solution:
#
# import sys
# import math
#
# size = int(input())
#
# coordinates = []
# highest_point = 0
# floor = -1
#
# for i in range(size):
#
#     vecX, vecY = map(int, input().split())
#     coordinates.append((vecX, vecY))
#
#     highest_point = max(highest_point, vecY)
#     if i > 0 and coordinates[i][1] == coordinates[i - 1][1]:
#         floor = i - 1
#
#
# test = -1
# flag = False
#
# while True:
#
#     X, Y, h_speed, v_speed, fuel, rotate, power = map(int, input().split())
#
#     if test == -1:
#
#         test = 1 if h_speed is 0 else 0
#
#     if test == 0:
#
#         if Y - coordinates[floor][1] < 800:
#
#             if v_speed <= -39:
#                 print("0 4")
#
#             else:
#                 print("0 3")
#
#         elif X <= coordinates[floor + 1][0]:
#             print("-45 4")
#
#         elif v_speed <= -20:
#             print("0 4")
#
#         elif v_speed <= -12:
#             print("0 2")
#
#         else:
#             print("45 4")
#
#     if test == 1:
#         if v_speed < -45 or Y <= 1135:
#             print("0 4")
#
#         elif X <= coordinates[floor][0]:
#             print("-32 3")
#
#         elif v_speed == 0 and Y > highest_point:
#             print("0 3")
#
#         elif v_speed < 0 or Y < highest_point:
#             print("0 4")
#
#         elif v_speed >= 12 or flag:
#             flag = True
#             print("45 4")
#
#         else:
#             print("0 4")
#
#     # I helped with the code: https://github.com/denvash/codingame-puzzles-solutions/blob/master/3-Very_Hard/Mars-Lander-Episode-3.java#L45
