import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import UNIT_CELSIUS, ICON_THERMOMETER

from .. import SpaLcd

CONF_SPA_ID = "spa_id"
CONF_TYPE = "type"

TYPES = ["main_temp", "small_temp"]

CONFIG_SCHEMA = sensor.sensor_schema(
    {
        cv.GenerateID(): cv.declare_id(sensor.Sensor),
        cv.Required(CONF_SPA_ID): cv.use_id(SpaLcd),
        cv.Required(CONF_TYPE): cv.one_of(*TYPES),
    }
)

async def to_code(config):
    sens = await sensor.new_sensor(config)
    spa = await cg.get_variable(config[CONF_SPA_ID])

    cg.add(sens.set_unit_of_measurement(UNIT_CELSIUS))
    cg.add(sens.set_icon(ICON_THERMOMETER))
