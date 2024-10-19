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
  "║ 5. Generar tablero aleatorio    ║\n"\
  "║ 6. Asignar tablero              ║\n"\
  "║ 7. Créditos                     ║\n"\
  "║ 8. Salir                        ║\n"\
  "╚═════════════════════════════════╝\n"\
  "Seleccione una opción: "


#define CREDITOS                     \
  "╔═════════════════════════════╗\n"\
  "║          Créditos           ║\n"\
  "║ Christopher Acosta Madrigal ║\n"\
  "║ Alberto Gonzalez Avendaño   ║\n"\
  "║ Felipe Mena Rodríguez       ║\n"\
  "║ Sebastian Sanchez Sandi     ║\n"\
  "╚═════════════════════════════╝\n"

class Menu {
 private:
  double timeElapsed = 0;
  void asignarTablero();

 public:
  Menu();
  ~Menu();

  void run();

  int mostrarPrincipal();
  void mostrarCreditos();


};

#endif  // MENU_HPP
