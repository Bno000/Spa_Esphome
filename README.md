example YAML

Use HA on_value automations to link this to your main spa controller

external_components:
  - source: github://your/repo

uart:
  id: tub_uart
  baud_rate: 1200
  tx_pin: GPIO1
  rx_pin: GPIO3

spa_lcd:
  id: spa
  uart_id: tub_uart

binary_sensor:
  - platform: spa_lcd
    spa_id: spa
    type: power_button

switch:
  - platform: spa_lcd
    spa_id: spa
    type: heat_icon

number:
  - platform: spa_lcd
    spa_id: spa
    type: main_temp
