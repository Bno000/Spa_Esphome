import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import UNIT_CELSIUS, ICON_THERMOMETER

from . import spa_lcd_ns, SpaLcd

CONF_SPA_ID = "spa_id"
CONF_TYPE = "type"

TYPES = ["main_temp", "small_temp"]

CONFIG_SCHEMA = sensor.SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(sensor.Sensor),
    cv.Required(CONF_SPA_ID): cv.use_id(SpaLcd),
    cv.Required(CONF_TYPE): cv.one_of(*TYPES),
})

async def to_code(config):
    sens = await sensor.new_sensor(config)
    spa = await cg.get_variable(config[CONF_SPA_ID])

    # These sensors are *output only* from ESPHome → STC,
    # so we don't bind callbacks here.
    #
    # But we DO expose them so users can read the values
    # they last wrote to the LCD (optional).
    #
    # If you later want the STC to report temperatures back,
    # this is where you'd bind spa.on_temp_update = sens.publish_state

    if config[CONF_TYPE] == "main_temp":
        cg.add(sens.set_unit_of_measurement(UNIT_CELSIUS))
        cg.add(sens.set_icon(ICON_THERMOMETER))

    if config[CONF_TYPE] == "small_temp":
        cg.add(sens.set_unit_of_measurement(UNIT_CELSIUS))
        cg.add(sens.set_icon(ICON_THERMOMETER))
