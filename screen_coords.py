"""
Contains static screen coordinates the bot uses
Screen coords for 1920x1080 screens
(x, y, x+w, y+h) for Vec4 locations, (x, y) for Vec2 locations
Đã đổi tọa độ thành 1920x1040
"""

from vec4 import Vec4, GameWindow
from vec2 import Vec2

SHOP_POS = Vec4(GameWindow(485, 1030, 1470, 1065))

CHAMP_NAME_POS = [Vec4(GameWindow(13, 5, 120, 26), use_screen_offset=False),
                  Vec4(GameWindow(204, 5, 320, 26), use_screen_offset=False),
                  Vec4(GameWindow(403, 5, 520, 26), use_screen_offset=False),
                  Vec4(GameWindow(593, 5, 700, 26), use_screen_offset=False),
                  Vec4(GameWindow(778, 5, 882, 26), use_screen_offset=False)]

GOLD_POS = Vec4(GameWindow(877, 879, 925, 908))

BUY_LOC = [Vec2(575, 992), Vec2(775, 992), Vec2(
    975, 992), Vec2(1175, 992), Vec2(1375, 992)]
    