"""
Py Matter GUI
=============
"""

import os
import sys
from pathlib import Path

from kivy.lang import Builder

from kivymd.app import MDApp

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["PYMATTER_ROOT"] = sys._MEIPASS
else:
    os.environ["PYMATTER_ROOT"] = str(Path(__file__).parent)


KV_DIR = f"{os.environ['PYMATTER_ROOT']}/libs/kv/"

for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())

KV = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import PyMatterRootScreen libs.baseclass.root_screen.PyMatterRootScreen

ScreenManager:
    transition: FadeTransition()

    PyMatterRootScreen:
        name: "py matter root screen"
"""


class PyMatter(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Py Matter"
#        self.icon = f"{os.environ['PYMATTER_ROOT']}/assets/images/logo_light.png"
        self.icon = f"{os.environ['PYMATTER_ROOT']}/assets/images/matter_lkup_rgb_day.png"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "100"

    def build(self):
        FONT_PATH = f"{os.environ['PYMATTER_ROOT']}/assets/fonts/"

        self.theme_cls.font_styles.update(
            {
                "H1": [FONT_PATH + "Raleway-Light", 96, False, -1.5],
                "H2": [FONT_PATH + "Raleway-Regular", 60, False, -0.5],
                "H3": [FONT_PATH + "Raleway-SemiBold", 48, False, 0],
                "H4": [FONT_PATH + "Raleway-SemiBold", 34, False, 0.25],
                "H5": [FONT_PATH + "Raleway-SemiBold", 24, False, 0],
                "H6": [FONT_PATH + "Raleway-SemiBold", 20, False, 0.15],
                "Subtitle1": [FONT_PATH + "Raleway-Medium", 16, False, 0.15],
                "Subtitle2": [FONT_PATH + "Raleway-SemiBold", 14, False, 0.1],
                "Body1": [FONT_PATH + "Raleway-SemiBold", 16, False, 0.5],
                "Body2": [FONT_PATH + "Raleway-Regular", 14, False, 0.25],
                "Button": [FONT_PATH + "Raleway-SemiBold", 14, True, 1.25],
                "Caption": [FONT_PATH + "Raleway-Medium", 12, False, 0.4],
                "Overline": [FONT_PATH + "Raleway-SemiBold", 12, True, 1.5],
            }
        )
        return Builder.load_string(KV)


PyMatter().run()
