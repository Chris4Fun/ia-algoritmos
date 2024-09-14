#include "Algoritmos.hpp"

#include <bits/stdc++.h>

using namespace std;
const vector<int> objetivo = {1, 2, 3, 4, 5, 6, 7, 8, 0};

Algoritmos::Algoritmos() {
}

Algoritmos::~Algoritmos() {
}

// Matrices a las que se puede llegar a partir de la actual
vector<vector<int>> Algoritmos::posiblesMovimientos(const vector<int>& actual) {
    vector<vector<int>> movimientos;
    int indiceVacio = find(actual.begin(), actual.end(), 0) - actual.begin();
    int iVacio = indiceVacio/3, jVacio = indiceVacio % 3;

    // Lista de casillas que se pueden mover hacia el Vacio
    vector<pair<int, int>> moves = {
        {iVacio-1, jVacio}, 
        {iVacio+1, jVacio}, 
        {iVacio, jVacio-1}, 
        {iVacio, jVacio+1}
    };

    for (auto [i, j] : moves) {
        if ((i >= 0) && (i < 3) && (j >= 0) && (j < 3)) {
            int nuevoIndiceVacio = i*3 + j;
            vector<int> siguiente = actual;
            swap(siguiente[indiceVacio], siguiente[nuevoIndiceVacio]);
            movimientos.push_back(siguiente);
        }
    }
    return movimientos;
}

bool Algoritmos::anchoPrimero() {
    auto t1 = std::chrono::high_resolution_clock::now();
    // Revisar si estado inicial es solucion
    if (tablero == objetivo) {
        auto t2 = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> ms_double = t2 - t1;
        std::cout << "Se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
        return true; 
    }
    // Algoritmo
    queue<vector<int>> frontera;
    set<vector<int>> visitados;
    frontera.push(tablero);
    while (!frontera.empty()) {
        vector<int> siguiente = frontera.front(); frontera.pop();
        vector<vector<int>> movimientos = posiblesMovimientos(siguiente);
        for (auto movimiento : movimientos) {
            // Revisar si alguno de los movimientos lleva al objetivo
            if (movimiento == objetivo) {
                auto t2 = std::chrono::high_resolution_clock::now();
                std::chrono::duration<double, std::milli> ms_double = t2 - t1;
                std::cout << "Se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
                return true;
            }
            if (visitados.find(movimiento) != visitados.end()) continue;
            visitados.insert(movimiento);
            frontera.push(movimiento); 
        }
    }
    // Si llega aqui, no se encontro solucion
    auto t2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> ms_double = t2 - t1;
    std::cout << "No se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
    return false;
}

void Algoritmos::shuffle() {
}

void Algoritmos::greedy() {
}

int Algoritmos::iterativeDeepeningDfs(vector<int> estado, set<vector<int>> &visitados, int depth) {
	if(depth == 0) {
		return false;
	}

	// Reviso si el estado actual es una solucion
	if(estado == objetivo) {
		return true;
	}

	// Añado este estado no visitado a los nodos visitados
	visitados.insert(estado);

	// Obtener los movimientos posibles
	vector<vector<int>> movimientos = posiblesMovimientos(estado);

	int resultado = false;
	// Itero por los posibles movimientos revisando si ya ha sido visitado ese nodo.
	for(auto movimiento : movimientos) {
		if(visitados.find(movimiento) == visitados.end()) {
			resultado = iterativeDeepeningDfs(movimiento, visitados, depth - 1);
			if(resultado) {
				return resultado;
			}
		}
	}

	return resultado;
}

void Algoritmos::solucionadorIDS() {
    int encontroSolucion = 0;
	int depth = 1;
	auto t1 = std::chrono::high_resolution_clock::now();
	while(!encontroSolucion) {
		set<vector<int>> visitados;
		encontroSolucion = iterativeDeepeningDfs(tablero, visitados, depth);
		++depth;
	}
	auto t2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> ms_double = t2 - t1;

	if(encontroSolucion) {
		std::cout << "Se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
	} else {
		std::cout << "No se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
	}
}

void Algoritmos::IDSHeuristica() {
}
