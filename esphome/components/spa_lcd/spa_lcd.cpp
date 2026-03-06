void SpaLcd::send_cmd(const std::string &s) {
  this->write_array((const uint8_t*)s.data(), s.size());
}

void SpaLcd::set_main_temp(int v) {
  char buf[16];
  int len = sprintf(buf, "M%d\r\n", v);
  send_cmd(std::string(buf, len));
}

void SpaLcd::set_small_temp(int v) {
  char buf[16];
  int len = sprintf(buf, "T%d\r\n", v);
  send_cmd(std::string(buf, len));
}

void SpaLcd::set_icon_heat(bool on) {
  send_cmd(on ? "H1\r\n" : "H0\r\n");
}

void SpaLcd::set_icon_pump(bool on) {
  send_cmd(on ? "P1\r\n" : "P0\r\n");
}

void SpaLcd::set_icon_blower(bool on) {
  send_cmd(on ? "F1\r\n" : "F0\r\n");
}

void SpaLcd::set_icon_ozone(bool on) {
  send_cmd(on ? "O1\r\n" : "O0\r\n");
}

void SpaLcd::set_backlight(bool on) {
  send_cmd(on ? "B1\r\n" : "B0\r\n");
}

void SpaLcd::loop() {
  while (this->available()) {
    char c = this->read();

    if (c == 'P' && on_power_press) on_power_press();
    if (c == 'J' && on_jets_press) on_jets_press();
    if (c == 'O' && on_o3_press) on_o3_press();
  }
}
