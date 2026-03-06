import esphome.codegen as cg
from esphome.components import uart

spa_lcd_ns = cg.esphome_ns.namespace("spa_lcd")
SpaLcd = spa_lcd_ns.class_("SpaLcd", cg.Component, uart.UARTDevice)

from .spa_lcd import CONFIG_SCHEMA

# Force ESPHome to load platform modules
from . import binary_sensor
from . import switch
from . import number
from . import sensor
