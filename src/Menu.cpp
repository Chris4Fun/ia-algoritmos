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
      std::cout << "Ancho primero" << std::endl;
      algoritmos.anchoPrimero();
      break;
    case 2:
      std::cout << "Ancho primero heuristica" << std::endl;
      algoritmos.anchoPrimeroHeuristica();
      break;
    case 3:
      std::cout << "Solucionador IDS" << std::endl;
      algoritmos.ids();
      break;
    case 4:
      std::cout << "IDS Heuristica" << std::endl;
      algoritmos.idsHeuristica();
      break;
    case 5:
      std::cout << "Generando tablero aleatorio..." << std::endl;
      algoritmos.shuffle();
      algoritmos.imprimirTablero();
      break;
    case 6:
      asignarTablero();
      break;
    case 7:
      mostrarCreditos();
      break;
    case 8:
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

void Menu::asignarTablero() {
  Algoritmos algoritmos = Algoritmos();
  std::cout << "Ingrese los valores: " << std::endl;
  vector<int> tablero(9);
  for (int i = 0; i < 9; i++) std::cin>>tablero[i];
  algoritmos.asignarTablero(tablero);
}

// --------------------------------------
// -------------ALGORITMOS---------------
// --------------------------------------
