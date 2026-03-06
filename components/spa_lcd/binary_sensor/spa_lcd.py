print("BINARY SENSOR MODULE LOADED")
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from .. import SpaLcd

CONF_SPA_ID = "spa_id"
CONF_TYPE = "type"

TYPES = ["power_button", "jets_button", "o3_button"]

CONFIG_SCHEMA = binary_sensor.binary_sensor_schema(
    {
        cv.GenerateID(): cv.declare_id(binary_sensor.BinarySensor),
        cv.Required(CONF_SPA_ID): cv.use_id(SpaLcd),
        cv.Required(CONF_TYPE): cv.one_of(*TYPES),
    }
)

async def to_code(config):
    sens = await binary_sensor.new_binary_sensor(config)
    spa = await cg.get_variable(config[CONF_SPA_ID])

    if config[CONF_TYPE] == "power_button":
        cg.add(spa.set_on_power_press_callback(sens))

    if config[CONF_TYPE] == "jets_button":
        cg.add(spa.set_on_jets_press_callback(sens))

    if config[CONF_TYPE] == "o3_button":
        cg.add(spa.set_on_o3_press_callback(sens))
