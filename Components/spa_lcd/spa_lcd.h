class SpaLcd : public Component, public UARTDevice {
 public:
  SpaLcd(UARTComponent *parent) : UARTDevice(parent) {}

  // Called every loop
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

 private:
  void send_cmd(const std::string &s);
};
