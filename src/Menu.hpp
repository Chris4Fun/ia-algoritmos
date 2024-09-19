#ifndef MENU_HPP
#define MENU_HPP

#include "Algoritmos.hpp"

#include <cmath>
#include <ctime>
#include <sched.h>
#include <time.h>
#include <cstdint>
#include <ostream>
#include <unistd.h>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>

#define OPCIONES_PRINCIPAL     \
  "╔═════════════════════════════════╗\n"\
  "║          Menú Principal         ║\n"\
  "║ 1. Ancho Primero                ║\n"\
  "║ 2. Ancho Primero con Heuristica ║\n"\
  "║ 3. Solucionador IDS             ║\n"\
  "║ 4. IDS Heuristica               ║\n"\
  "║ 5. Generar tablero              ║\n"\
  "║ 6. Créditos                     ║\n"\
  "║ 7. Salir                        ║\n"\
  "╚═════════════════════════════════╝\n"\
  "Seleccione una opción: "


#define CREDITOS                     \
  "╔═════════════════════════════╗\n"\
  "║          Créditos           ║\n"\
  "║ Christopher Acosta Madrigal ║\n"\
  "║ Alberto González Avendaño   ║\n"\
  "║ Felipe Mena Rodríguez       ║\n"\
  "╚═════════════════════════════╝\n"

class Menu {
 private:
  double timeElapsed = 0;

 public:
  Menu();
  ~Menu();

  void run();

  int mostrarPrincipal();
  void mostrarCreditos();


};

#endif  // MENU_HPP
