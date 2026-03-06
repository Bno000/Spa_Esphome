import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import number
from . import spa_lcd_ns, SpaLcd

CONFIG_SCHEMA = number.NUMBER_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(number.Number),
    cv.Required("spa_id"): cv.use_id(SpaLcd),
    cv.Required("type"): cv.one_of("setpoint", "main_temp"),
})

async def to_code(config):
    num = await number.new_number(config)
    spa = await cg.get_variable(config["spa_id"])

    if config["type"] == "setpoint":
        cg.add(num.set = spa.set_small_temp(num))
    if config["type"] == "main_temp":
        cg.add(num.set = spa.set_main_temp(num))
