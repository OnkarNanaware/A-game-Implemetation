# Shadow Escape: Real-Time A* Search Pathfinding Demonstration

**Course / Assignment:** AI/ML Assignment 1  
**Topic:** Informed Search Strategies — A* Algorithm Implementation  
**Language:** Python 3.x  

---

## 📌 Overview

**Shadow Escape** is a terminal-based, turn-based CUI (Console User Interface) game designed to demonstrate the real-time execution of the **A* (A-Star) Pathfinding Algorithm**. 

In this game, the player (`P`) must navigate through a non-trivial maze to reach the escape exit (`E`). Simultaneously, an autonomous adversary—the Ghost (`G`)—uses the A* search algorithm to evaluate the grid, recalculate the shortest optimal path, and actively track the player's moving coordinates after every turn.

This project serves as a practical implementation of informed search heuristics, grid graph traversal, and priority queue management in artificial intelligence.

---

## 🧠 Core AI Concepts & Implementation Details

### 1. The A* Evaluation Function
The adversary's pathfinding decisions are governed by the classic evaluation function:

$$F(n) = G(n) + H(n)$$

* **$G(n)$ (Path Cost):** The exact movement cost from the Ghost's starting node to current node $n$. Each orthogonal movement (Up, Down, Left, Right) incurs a uniform cost of `1`.
* **$H(n)$ (Heuristic Cost):** The estimated distance from node $n$ to the player's current position (target node). The system utilizes **Manhattan Distance** due to the 4-directional grid constraints:
  
  $$\text{Distance} = |x_{\text{ghost}} - x_{\text{player}}| + |y_{\text{ghost}} - y_{\text{player}}|$$

* **$F(n)$ (Total Estimated Cost):** The primary value evaluated by the AI to select the most efficient node for expansion.

### 2. Data Structures & Algorithmic Efficiency
* **Min-Heap Priority Queue (`heapq`):** The algorithm maintains an `Open Set` using Python's `heapq` module. Nodes with the lowest $F(n)$ values are popped first in $O(\log N)$ time, ensuring optimal decision-making without redundant iterations.
* **Closed Set / Visited Dictionary:** Tracks the lowest $G(n)$ cost recorded for visited grid positions to avoid infinite loops and prevent redundant updates to worse paths.
* **Parent Link Traversal:** Once the destination is matched, the path is reconstructed backwards through node parent references to retrieve the immediate next step for the adversary.

---

## 🎮 Game Rules & Map Legend

| Symbol | Entity | Description |
| :---: | :--- | :--- |
| **`P`** | **Player** | User-controlled agent moving using WASD keys. |
| **`G`** | **Ghost** | AI Chaser executing A* to recalculate pathing dynamically. |
| **`E`** | **Exit** | Target destination for player victory. |
| **`#`** | **Wall** | Non-walkable obstacles/obstacles in the grid matrix. |

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/shadow-escape-a-star.git](https://github.com/your-username/shadow-escape-a-star.git)
   cd shadow-escape-a-star