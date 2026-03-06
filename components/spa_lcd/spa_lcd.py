import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

AUTO_LOAD = ["binary_sensor", "switch", "number", "sensor"]
DEPENDENCIES = ["uart"]

spa_lcd_ns = cg.esphome_ns.namespace("spa_lcd")
SpaLcd = spa_lcd_ns.class_("SpaLcd", cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(SpaLcd),
        cv.Required("uart_id"): cv.use_id(uart.UARTComponent),
    }
)

async def to_code(config):
    uart_component = await cg.get_variable(config["uart_id"])
    var = cg.new_Pvariable(config[CONF_ID], uart_component)
    await cg.register_component(var, config)
