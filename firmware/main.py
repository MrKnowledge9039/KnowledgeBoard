print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()

rgb = RGB(pixel_pin=board.GP3, num_pixels=9)
keyboard.extensions.append(rgb)

keyboard.modules = [layers, encoder_handler]
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.GP4, board.GP5, board.GP10)
keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9,)


Zoom_in = KC.LCTRL(KC.EQUAL)
Zoom_out = KC.LCTRL(KC.MINUS)

encoder_handler.pins = (
    (board.GP0, board.GP1, None), # encoder #1 
    (board.GP2, board.GP1, None), # encoder #2
    )

LayerNum = 0

LUP = KC.FD(LayerNum - 1) if LayerNum > 0 else KC.FD(0)
LDN = KC.FD(LayerNum + 1) if LayerNum < 5 else KC.FD(5)

encoder_handler.map = [ (( KC.VOLD, KC.VOLU), (KC.BRID, KC.BRIU),), # Default
                        ((Zoom_out, Zoom_in), (KC.LBRC, KC.RBRC),), # Zoom / Krita Layer will get upgrade
                        ((KC.RIGHT, KC.LEFT), (KC.DOWN, KC.UP),),   # DMXC Pos
                        ((KC.MS_RT, KC.MS_LT), (KC.MW_UP, KC.MW_DN),),   # Move Mouse
                        ((KC.FD(LUP), KC.FD(LDN)), (KC.NO, KC.NO),),   # Switch Layer
                      ]


class LayerRGB(RGB):
    def on_layer_change(self, layer):
        if layer == 0:
            rgb.set_hsv(170, self.sat_default, self.val_default, 0) # blue
        elif layer == 1:
            rgb.set_hsv(170, self.sat_default, self.val_default, 1)
        elif layer == 2:
            rgb.set_hsv(170, self.sat_default, self.val_default, 2)
        elif layer == 4:
            rgb.set_hsv(170, 0, self.val_default, 3)               
        elif layer == 4:
                    rgb.set_hsv(170, 0, self.val_default, 3)       
        # update the LEDs manually if no animation is active:
        self.show()



keyboard.keymap = [
    [
        KC.MO(5), KC.NO, KC.MUTE,
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.N9,
    ],
    [
        KC.MO(5), KC.NO, KC.MUTE,
        KC.F13, KC.F14, KC.F15,
        KC.F16, KC.F17, KC.F18,
        KC.F19, KC.F20, KC.F21,
    ],
    [
        KC.MO(5), KC.NO, KC.MUTE,
        KC.N1, KC.N2, KC.N3,
        KC.Q, KC.W, KC.E,
        KC.A, KC.S, KC.D,
    ],
    [
        KC.MO(5), KC.NO, KC.MUTE,
        KC.RGB_HUI, KC.RGB_HUD, KC.RGB_TOG,
        KC.RGB_VAI, KC.RGB_VAD, KC.NO,
        KC.NO, KC.NO, KC.NO,
    ]
]

rgb.set_hsv_fill(0, 0, rgb.val_default)

if __name__ == '__main__':
    keyboard.go()