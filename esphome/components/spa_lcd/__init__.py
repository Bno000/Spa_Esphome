from esphome.codegen import cg, namespace

spa_lcd_ns = namespace('spa_lcd')
SpaLcd = spa_lcd_ns.class_('SpaLcd', cg.Component, cg.UARTDevice)

# Register platforms
from . import spa_lcd
from . import binary_sensor
from . import switch
from . import number
