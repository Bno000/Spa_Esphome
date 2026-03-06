import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import number
from .. import SpaLcd

CONF_SPA_ID = "spa_id"
CONF_TYPE = "type"

TYPES = ["main_temp", "small_temp"]

CONFIG_SCHEMA = number.number_schema(
    {
        cv.GenerateID(): cv.declare_id(number.Number),
        cv.Required(CONF_SPA_ID): cv.use_id(SpaLcd),
        cv.Required(CONF_TYPE): cv.one_of(*TYPES),
    }
)

async def to_code(config):
    num = await number.new_number(config)
    spa = await cg.get_variable(config[CONF_SPA_ID])

    if config[CONF_TYPE] == "main_temp":
        cg.add(num.set_set_action(spa.set_main_temp(num)))

    if config[CONF_TYPE] == "small_temp":
        cg.add(num.set_set_action(spa.set_small_temp(num)))
