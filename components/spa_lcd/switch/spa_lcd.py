import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch
from .. import SpaLcd

CONF_SPA_ID = "spa_id"
CONF_TYPE = "type"

TYPES = ["heat_icon", "pump_icon", "blower_icon", "ozone_icon", "backlight"]

CONFIG_SCHEMA = switch.switch_schema(
    {
        cv.GenerateID(): cv.declare_id(switch.Switch),
        cv.Required(CONF_SPA_ID): cv.use_id(SpaLcd),
        cv.Required(CONF_TYPE): cv.one_of(*TYPES),
    }
)

async def to_code(config):
    sw = await switch.new_switch(config)
    spa = await cg.get_variable(config[CONF_SPA_ID])

    if config[CONF_TYPE] == "heat_icon":
        cg.add(sw.set_turn_on_action(spa.set_icon_heat(True)))
        cg.add(sw.set_turn_off_action(spa.set_icon_heat(False)))

    if config[CONF_TYPE] == "pump_icon":
        cg.add(sw.set_turn_on_action(spa.set_icon_pump(True)))
        cg.add(sw.set_turn_off_action(spa.set_icon_pump(False)))

    if config[CONF_TYPE] == "blower_icon":
        cg.add(sw.set_turn_on_action(spa.set_icon_blower(True)))
        cg.add(sw.set_turn_off_action(spa.set_icon_blower(False)))

    if config[CONF_TYPE] == "ozone_icon":
        cg.add(sw.set_turn_on_action(spa.set_icon_ozone(True)))
        cg.add(sw.set_turn_off_action(spa.set_icon_ozone(False)))

    if config[CONF_TYPE] == "backlight":
        cg.add(sw.set_turn_on_action(spa.set_backlight(True)))
        cg.add(sw.set_turn_off_action(spa.set_backlight(False)))
