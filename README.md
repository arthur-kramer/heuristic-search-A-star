# Heuristic Search with A*

## 📌 Overview

This project implements the A algorithm to help a user find the fastest path between two stations in an illustrative simulation of the London Underground, as shown in the figure below.

<img width="729" height="415" alt="image" src="https://github.com/user-attachments/assets/f4f2609b-cd0e-4041-a9c0-5f2a3a8552e1" />

## 🛠️ Methodology

The problem modeling considers the initial and goal states, the possible actions, the costs, and the evaluation function.

The **initial state** is the origin station provided by the user in the format “Station_Color”; in the simulation, it was set as E1_Red, representing station E1 on the Red line.

The **goal state** is the destination station, also in the format “Station_Color”, defined as E6_Blue, corresponding to station E6 on the Blue line.

The **actions** correspond to movements between adjacent stations and transfers between lines.

The **cost** of each action depends on its nature: movements between adjacent stations on the same line have a cost based on the required time, calculated from the actual distance and an average speed of 40 km/h, according to the equation below. Transfers between different lines have a fixed cost of 3 minutes, representing the time needed to change lines.

$$
time\ [min] = \frac{realdistance\ [km]}{40} \times 60
$$

The **evaluation function** 𝑓(𝑛) of A* combines two components: the accumulated cost 𝑔(𝑛), from the initial state to the current state, and the heuristic function ℎ(𝑛), which estimates the time to the goal state, calculated based on the Euclidean distance between the current station and the destination station.

With the initial and goal states defined in the simulation, logs of the A* algorithm execution were generated. These logs show, at each iteration, the composition of the frontier, the node under analysis, its successor nodes, and the costs associated with each. Upon reaching the goal state, the algorithm provides the fastest route found and the total time required to traverse it (total cost).

## 🗺️🔄 A* Algorithm Iterations: Illustrated Step-by-Step

The following images illustrate the representation of the initial state and the first iterations of the A* algorithm, simulating the calculation of the fastest route between stations E1_Red and E6_Blue.

### 1️⃣ **Initial State and First Iteration**

<img width="505" height="463" alt="image" src="https://github.com/user-attachments/assets/2284cc44-a6c1-4e38-83c8-26ea1121bbcb" />

### 2️⃣ **Second Iteration**

<img width="640" height="452" alt="image" src="https://github.com/user-attachments/assets/ecb5cb16-bee4-494f-9bc3-84efcbb1e0a8" />

### 3️⃣ **Third Iteration**

<img width="703" height="489" alt="image" src="https://github.com/user-attachments/assets/9826698b-76d5-46b8-8fdb-72899df9c508" />

### 4️⃣ **Fourth Iteration**

<img width="703" height="547" alt="image" src="https://github.com/user-attachments/assets/3ec8143d-83a7-4f75-965d-a625d0ee90b9" />
