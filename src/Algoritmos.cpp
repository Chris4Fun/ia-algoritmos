#include "Algoritmos.hpp"

using namespace std;

Algoritmos::Algoritmos() {
}

Algoritmos::~Algoritmos() {
}

// --------------------------  Métodos de apoyo  -------------------------------

void Algoritmos::shuffle() {
    /* Genera semilla con time (el static cast se realiza para evitar problemas
    con signos del tipo de dato time_t): */
    unsigned seed = static_cast<unsigned>(std::time(NULL));
    // Con la semilla se crea un generador de números aleatorios:
    std::default_random_engine random(seed);
    // Se barajean los elementos del vector:
    std::shuffle(this->tablero.begin(), this->tablero.end(), random);
}

// Matrices a las que se puede llegar a partir de la actual
vector<vector<int>> Algoritmos::posiblesMovimientos(const vector<int>& actual) {
    vector<vector<int>> movimientos;
    // Busca donde está el espacio vacío:
    int indiceVacio = find(actual.begin(), actual.end(), 0) - actual.begin();
    // Obtiene posición como si fuera una matriz 3x3:
    int iVacio = indiceVacio / 3;
    int jVacio = indiceVacio % 3;

    // Lista de casillas que se pueden mover hacia el espacio vacio:
    vector<pair<int, int>> moves = {
        {iVacio - 1, jVacio}, 
        {iVacio + 1, jVacio}, 
        {iVacio, jVacio - 1}, 
        {iVacio, jVacio + 1}
    };
    // Genera los nuevos estados:
    for (auto [i, j] : moves) {
        // Verifica que los movimientos estén dentro de los límites del tablero:
        if ((i >= 0) && (i < 3) && (j >= 0) && (j < 3)) {
            // Convierte nuevamente a representación lineal:
            int nuevoIndiceVacio = i * 3 + j;
            // Crea el estado y lo guarda:
            vector<int> siguiente = actual;
            swap(siguiente[indiceVacio], siguiente[nuevoIndiceVacio]);
            movimientos.push_back(siguiente);
        }
    }
    return movimientos;
}

void Algoritmos::printBoard() {    
    // Imprime el tablero como una matriz de 3x3
    std::cout << "Tablero:\n";
    for (int i = 0; i < 9; ++i) {
        std::cout << tablero[i] << " ";
        if ((i + 1) % 3 == 0) {
            std::cout << std::endl;
        }
    }
    std::cout << std::endl;
}
// -----------------------------  Algoritmos  ----------------------------------

bool Algoritmos::anchoPrimero() {
    auto t1 = std::chrono::high_resolution_clock::now();
    // Revisar si estado inicial es solucion
    if (this->tablero == objetivo) {
        auto t2 = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> ms_double = t2 - t1;
        std::cout << "Se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
        return true; 
    }
    // Algoritmo
    queue<vector<int>> frontera;
    set<vector<int>> visitados;
    frontera.push(this->tablero);
    while (!frontera.empty()) {
        vector<int> siguiente = frontera.front();
        frontera.pop();
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

bool Algoritmos::greedy() {
    // Inicia el contador:
    auto t1 = std::chrono::high_resolution_clock::now();
    // Revisar si estado inicial es solucion:
    if (this->tablero == objetivo) {
        // Mide e indica la duración:
        auto t2 = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> ms_double = t2 - t1;
        std::cout << "Se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
        return true; 
    }
    // Algoritmo
    // Crea criterio de ordenamiento para la cola:
    Compare cmp(this->objetivo);
    // Crea cola de prioridad con el criterio dado:
    priority_queue<vector<int>, vector<vector<int>>, Compare> frontera(cmp);
    // Crea estados visitados:
    set<vector<int>> visitados;

    frontera.push(this->tablero);
    while (!frontera.empty()) {
        vector<int> siguiente = frontera.top();
        frontera.pop();
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
    // Si llega aqui, no se encontro solucion:
    auto t2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> ms_double = t2 - t1;
    std::cout << "No se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
    return false;
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
  // Inicia el contador:
  auto t1 = std::chrono::high_resolution_clock::now();

  // Boolean para detenerse en caso de haber encotrado la solucion
  bool encontroSolucion = false;

  // Cola de prioridad para ordenar por la heuristica
  std::priority_queue<std::pair<int, std::vector<int>>,
  std::vector<std::pair<int, std::vector<int>>>,
  greater<std::pair<int, std::vector<int>>>> colaPrioridad;

  // Crea un conjunto de los estados visitados
  std::set<std::vector<int>> visitados;

  // Pushea el primer estado
  colaPrioridad.push({heuristicaManhattan(this->tablero), this->tablero});

  while(!colaPrioridad.empty() && !encontroSolucion) {
    // Obtiene el primer elemento de la cola
    std::vector<int> estadoActual = colaPrioridad.top().second;
    colaPrioridad.pop();

    // Se revisa si se encuentra en el objectivo
    if (estadoActual == this->objetivo) {
      encontroSolucion = true;
    }

    //  Agrega el estado a visitados
    visitados.insert(estadoActual);
    // Obtener los movimientos posibles
    vector<vector<int>> movimientos = posiblesMovimientos(estadoActual);
    // Itero por los posibles movimientos revisando si ya ha sido visitado ese nodo.
    for (auto movimiento : movimientos)
    {
      if (visitados.find(movimiento) == visitados.end())
      {
        colaPrioridad.push({heuristicaManhattan(movimiento), movimiento });
      }
    }
  }

  // Termina el contador
  auto t2 = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double, std::milli> ms_double = t2 - t1;

  if(encontroSolucion) {
    std::cout << "Se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
  } else {
    std::cout << "No se encontro la solucion. Duracion: " << ms_double.count() << "ms\n";
  }

}

int Algoritmos::heuristicaManhattan(const vector<int>& movimientoActual) {
    int distance = 0;

    for (size_t i = 0; i < movimientoActual.size(); ++i) {
        int distanciaIndividual = abs(movimientoActual[i] - this->objetivo[i]);
        distance += distanciaIndividual;
    }
    return distance;
}
