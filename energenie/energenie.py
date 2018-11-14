from time import sleep
import json
import os


_cache_file = "/tmp/energenie.json"

# The GPIO pins for the Energenie module
BIT1 = 17
BIT2 = 22
BIT3 = 23
BIT4 = 27

ON_OFF_KEY = 24
ENABLE = 25

# Codes for switching on and off the sockets
#       all     1       2       3       4
ON = ['1011', '1111', '1110', '1101', '1100']
OFF = ['0011', '0111', '0110', '0101', '0100']


def _change_gpio(pin, value):
    gpio_path = "/sys/class/gpio/gpio%u/value" % pin
    with open(gpio_path, "w") as f:
        f.write("1" if value else "0")

global _state_cache
_state_cache = [0,0,0,0]

if os.path.exists(_cache_file):
    try:
        with open(_cache_file) as f:
            _state_cache = json.load(f)
    except:
        pass


def change_plug_state(socket, on_or_off):
    global _state_cache
    state = on_or_off[socket][3] == '1'
    _change_gpio(BIT1, state)
    state = on_or_off[socket][2] == '1'
    _change_gpio(BIT2, state)
    state = on_or_off[socket][1] == '1'
    _change_gpio(BIT3, state)
    state = on_or_off[socket][0] == '1'
    _change_gpio(BIT4, state)
    sleep(0.1)
    _change_gpio(ENABLE, True)
    sleep(0.25)
    _change_gpio(ENABLE, False)
    if socket:
        _state_cache[socket-1] = 1 if on_or_off == ON else 0
    else:
        _state_cache = [1,1,1,1] if on_or_off == ON else [0,0,0,0]
    with open(_cache_file, "w") as f:
        json.dump(_state_cache, f)


def get_plug_state():
    return _state_cache


def switch_on(socket=0):
    change_plug_state(socket, ON)


def switch_off(socket=0):
    change_plug_state(socket, OFF)


def switches_init():
    global _state_cache
    _change_gpio(ON_OFF_KEY, False)
    _change_gpio(ENABLE, False)

    _change_gpio(BIT1, False)
    _change_gpio(BIT2, False)
    _change_gpio(BIT3, False)
    _change_gpio(BIT4, False)
    switch_off()
