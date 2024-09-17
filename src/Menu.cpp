#include "Menu.hpp"

Menu::Menu() {
}

Menu::~Menu() {
}


// ----------------------------------
// ----------MENU PRINCIPAL----------
// ----------------------------------
void Menu::run() {
  
  Algoritmos algoritmos = Algoritmos();

  int opcion;
  do {
    opcion = mostrarPrincipal();
    switch (opcion) {
    case 1:
      std::cout << "Ancho " << std::endl;
      algoritmos.anchoPrimero();
      break;
    case 2:
      std::cout << "Greedy" << std::endl;
      algoritmos.greedy();
      break;
    case 3:
      std::cout << "Solucionador IDS" << std::endl;
      algoritmos.solucionadorIDS();
      break;
    case 4:
      std::cout << "IDS Heuristica" << std::endl;
      algoritmos.IDSHeuristica();
      break;
    case 5:
      std::cout << "Generando tablero aleatorio..." << std::endl;
      algoritmos.shuffle();
      algoritmos.printBoard();
      break;
    case 6:
      mostrarCreditos();
      break;
    case 7:
      std::cout << "Saliendo..." << std::endl;
      break;
    default:
      std::cout << "Opción inválida." << std::endl;
      break;
    }
  } while (opcion != 7);
}


// --------------------------------------
// ----------MÉTODOS AUXILIARES----------
// --------------------------------------
int Menu::mostrarPrincipal() {
  int opcion;
  std::cout << OPCIONES_PRINCIPAL;
  std::cin >> opcion;
  return opcion;
}

void Menu::mostrarCreditos() { std::cout << CREDITOS; }

// --------------------------------------
// -------------ALGORITMOS---------------
// --------------------------------------
