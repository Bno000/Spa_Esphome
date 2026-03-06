import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from . import spa_lcd_ns, SpaLcd

CONFIG_SCHEMA = binary_sensor.BINARY_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(binary_sensor.BinarySensor),
    cv.Required("spa_id"): cv.use_id(SpaLcd),
    cv.Required("type"): cv.one_of("power_button", "jets_button", "o3_button"),
})

async def to_code(config):
    sens = await binary_sensor.new_binary_sensor(config)
    spa = await cg.get_variable(config["spa_id"])

    if config["type"] == "power_button":
        cg.add(spa.on_power_press = sens.publish_state(True))
    if config["type"] == "jets_button":
        cg.add(spa.on_jets_press = sens.publish_state(True))
    if config["type"] == "o3_button":
        cg.add(spa.on_o3_press = sens.publish_state(True))
