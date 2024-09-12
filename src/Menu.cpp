#include "Menu.hpp"

#include <cmath>
#include <ctime>
#include <sched.h>
#include <time.h>
#include <cstdint>
#include <ostream>
#include <unistd.h>

Menu::Menu() {
  this->cola = nullptr;
  this->arbol = nullptr;
}

Menu::~Menu() {
  if (this->cola != nullptr) {
    this->cola->destruir();
  }
  if (this->arbol != nullptr) {
    this->arbol->Destruir();
  }
}

double log(double base, double x) { return std::log(x) / std::log(base); }

void Menu::crearArbolAuto(int64_t levelsToCreate, int64_t numHijos) {
  this->arbol->PonerRaiz(0);
  int64_t etiquetaHijo = 1;
  int64_t numNodos = 1;

  if (levelsToCreate == 1) {
    return;
  }

  NODO *nodoActual = nullptr;

  Cola<NODO *> colaNodo;
  colaNodo.iniciar();
  colaNodo.encolar(this->arbol->Raiz());
  while (!colaNodo.vacia()) {
    nodoActual = colaNodo.desencolar();
    for (int i = 1; i <= numHijos; ++i) {
      auto aux = this->arbol->AgregarHijo(nodoActual, i, etiquetaHijo);
      colaNodo.encolar(aux);
      ++etiquetaHijo;
      ++numNodos;
    }
    int64_t leveledNodes = numNodos;
    leveledNodes -= std::pow(numHijos, levelsToCreate - 2);
    if (log(numHijos, levelsToCreate == 2 ? leveledNodes : leveledNodes - 1) ==
        levelsToCreate - 1 ) {
      colaNodo.destruir();
      break;
    }
  }
}

// ----------------------------------
// ----------MENU PRINCIPAL----------
// ----------------------------------
void Menu::run() {
  this->arbol = new ARBOL;
  this->arbol->Iniciar();

  // Arbol creado automaticamente, balanceado
  crearArbolAuto(10,3);

  int opcion;
  do {
    opcion = mostrarPrincipal();
    switch (opcion) {
    case 1:
      this->runCola();
      break;
    case 2:
      this->runArbol();
      break;
    case 3:
      mostrarCreditos();
      break;
    case 4:
      std::cout << "Saliendo..." << std::endl;
      break;
    default:
      std::cout << "Opción inválida." << std::endl;
      break;
    }
  } while (opcion != 4);
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

int Menu::mostrarOperadoresArbol() {
  int opcion;
  std::cout << OPERADORES_ARBOL;
  std::cin >> opcion;
  return opcion;
}

int Menu::mostrarOperadoresCola() {
  int opcion;
  std::cout << OPERADORES_COLA;
  std::cin >> opcion;
  return opcion;
}

void Menu::mostrarCreditos() { std::cout << CREDITOS; }

void Menu::mostrarColaActual() {
  if (this->cola == nullptr) {
    std::cout << "No hay una cola actualmente." << std::endl;
    return;
  }
  this->cola->imprimir();
}

void Menu::mostrarArbolActual() {
  if (this->arbol->Vacio()) {
    std::cout << "El árbol está vacío." << std::endl;
    return;
  }
  this->arbol->Imprimir();
}
