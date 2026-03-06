import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch
from . import spa_lcd_ns, SpaLcd

CONFIG_SCHEMA = switch.SWITCH_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(switch.Switch),
    cv.Required("spa_id"): cv.use_id(SpaLcd),
    cv.Required("type"): cv.one_of("heat_icon", "pump_icon", "blower_icon", "ozone_icon", "backlight"),
})

async def to_code(config):
    sw = await switch.new_switch(config)
    spa = await cg.get_variable(config["spa_id"])

    if config["type"] == "heat_icon":
        cg.add(sw.turn_on = spa.set_icon_heat(True))
        cg.add(sw.turn_off = spa.set_icon_heat(False))
    # repeat for others...
