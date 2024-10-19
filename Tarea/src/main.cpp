#include "Menu.hpp"

int main() {
  Menu* menu = new Menu();
  menu->run();
  delete menu;
  return 0;
}