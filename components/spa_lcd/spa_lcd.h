#pragma once
#include "esphome.h"

class SpaLcd : public esphome::Component, public esphome::uart::UARTDevice {
 public:
  SpaLcd(esphome::uart::UARTComponent *parent) : UARTDevice(parent) {}

  void loop() override;

  // Commands
  void set_main_temp(int v);
  void set_small_temp(int v);
  void set_icon_heat(bool on);
  void set_icon_pump(bool on);
  void set_icon_blower(bool on);
  void set_icon_ozone(bool on);
  void set_backlight(bool on);

  // Button callbacks
  std::function<void()> on_power_press;
  std::function<void()> on_jets_press;
  std::function<void()> on_o3_press;

 protected:
  void send_cmd(const std::string &s);
};
