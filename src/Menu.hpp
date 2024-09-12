#ifndef MENU_HPP
#define MENU_HPP

#include <cstdint>
#include <iostream>
#include <map>
#include <string>

#define OPCIONES_PRINCIPAL                                                        \
  "╔═══════════════════════╗\n" \
  "║    Menú Principal     ║\n"                                              \
  "║ 1. Modelo Cola        ║\n"                                               \
  "║ 2. Modelo Árbol       ║\n"                                              \
  "║ 3. Créditos           ║\n"                                              \
  "║ 4. Créditos           ║\n"                                              \
  "║ 5. Créditos           ║\n"                                              \
  "║ 6. Salir              ║\n"                                               \
  "╚═══════════════════════╝\n" \
  "Seleccione una opción: "


#define CREDITOS                                                                                    \
  "╔═════════════════════════════╗\n" \
  "║          Créditos           ║\n"                                                          \
  "║ Christopher Acosta Madrigal ║\n"                                                           \
  "╚═════════════════════════════╝\n"

class Menu {
 private:
  double timeElapsed = 0;

 public:
  Menu();
  ~Menu();

  void run();
  void runCola();
  void runArbol();

  int mostrarPrincipal();
  int mostrarOperadoresArbol();
  int mostrarOperadoresCola();
  void mostrarCreditos();
  void mostrarColaActual();
  void mostrarArbolActual();

  void crearArbolAuto(int64_t levelsToCreate, int64_t NumHijos);

// Algoritmos

};

#endif  // MENU_HPP
