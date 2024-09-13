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

void Algoritmos::anchoPrimero() {
    auto t1 = std::chrono::high_resolution_clock::now();

    queue<vector<int>> q;
    set<vector<int>> visitados;
    q.push(tablero);
    while (!q.empty()) {
        vector<int> siguiente = q.front(); q.pop();
        
        if (siguiente == objetivo) return;

        vector<vector<int>> movimientos = posiblesMovimientos(siguiente);
        for (auto movimiento : movimientos) {
            if (visitados.find(movimiento) != visitados.end()) continue;
            visitados.insert(movimiento);
            q.push(movimiento); 
        }
    }

    auto t2 = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> ms_double = t2 - t1;
    std::cout << ms_double.count() << "ms\n";
}

void Algoritmos::shuffle() {
}

void Algoritmos::greedy() {
}

void Algoritmos::solucionadorIDS() {
}

void Algoritmos::IDSHeuristica() {
}
