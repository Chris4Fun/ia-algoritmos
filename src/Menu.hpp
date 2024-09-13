#ifndef MENU_HPP
#define MENU_HPP

#include <cstdint>
#include <iostream>
#include <map>
#include <string>

#define OPCIONES_PRINCIPAL                                                        \
  "╔═══════════════════════╗\n" \
  "║    Menú Principal     ║\n"                                              \
  "║ 1. Ancho Primero      ║\n"                                               \
  "║ 2. Greedy             ║\n"                                              \
  "║ 3. Solucionador IDS   ║\n"                                              \
  "║ 4. IDS Heuristica     ║\n"                                              \
  "║ 5. Créditos           ║\n"                                              \
  "║ 6. Salir              ║\n"                                               \
  "╚═══════════════════════╝\n" \
  "Seleccione una opción: "


#define CREDITOS                                                                                    \
  "╔═════════════════════════════╗\n" \
  "║          Créditos           ║\n"                                                          \
  "║ Christopher Acosta Madrigal ║\n"                                                           \
  "║ Alberto González Avendaño   ║\n"                                                           \
  "║ Christopher Acosta Madrigal ║\n"                                                           \
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
