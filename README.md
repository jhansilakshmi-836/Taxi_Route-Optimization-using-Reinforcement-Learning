# Taxi_Route-Optimization-using-Reinforcement-Learning
This project simulates a taxi moving in a city grid, picking up a passenger and dropping them at their destination while accounting for traffic delays. It allows users to customize the taxi start, passenger pickup, drop-off, and traffic positions, providing a visual route map and total travel time.

Project :- Taxi Route Optimization with Traffic Flow
Aim :-
The aim of this project is to simulate and optimize a taxi route in a grid-based city environment, considering passenger pickup, drop-off, and traffic delays.

Operators :-
Move Up (up) – Move one cell up in the grid.
Move Down (down) – Move one cell down in the grid.
Move Left (left) – Move one cell to the left.
Move Right (right) – Move one cell to the right.
Pickup Passenger (pickup) – Pick up the passenger when taxi reaches the passenger location.
Dropoff Passenger (dropoff) – Drop off the passenger at the destination.

Additional Consideration :-
Traffic cells (X) increase travel time by slowing the taxi but do not block movement

Project Workflow :-
User provides input :- Taxi start, Passenger pickup, Destination, and optional Traffic positions.
The taxi calculates the Manhattan-style shortest path to the passenger and then to the destination.
T = Taxi start
P = Passenger pickup
D = Destination
* = Taxi route
X = Traffic cells
Total travel time is calculated considering traffic delays.

Conclusion :-
*Taxi completes route efficiently.
*Traffic affects travel time.
*Grid map shows path clearly
