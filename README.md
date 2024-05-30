# Pacman Search Project

![Search Snippet](maze.png)

## Introduction

In this project, my Pacman agent finds paths through his maze world, both to reach a particular location and to collect food efficiently. I built general search algorithms and applied them to Pacman scenarios.

This project includes an autograder to grade the answers on my machine. It can be run with the command:

```
cd search
python autograder.py
```
### Big Note!
This program need python version 3.6 to run. This is available on Windows (and possibly Linux), but not Mac. See `requirements.txt`.

## Skills Developed

## Skills Developed
- **Search Algorithms**: Implemented and applied DFS, BFS, UCS, and A* Search in Python.
- **Algorithm Optimization**: Created efficient, admissible, and consistent heuristics for A* Search.
- **State Management**: Encoded and managed relevant state information for effective problem-solving.
- **Performance Analysis**: Analyzed and optimized search algorithm performance.
- **Handling Edge Cases**: Ensured robustness in search algorithms under various conditions.
- **Data Structures**: Utilized stacks, queues, and priority queues effectively.

## Files

The code for this project consists of several Python files, some of which I read and understood to complete the assignment and some of which I edited/implemented.

### Files Edited:
- `search.py`: Contains all of the search algorithms.
- `searchAgents.py`: Contains all of the search-based agents.

### Files Reviewed:
- `pacman.py`: The main file that runs Pacman games. This file describes a Pacman `GameState` type, which I used in this project.
- `game.py`: The logic behind how the Pacman world works. This file describes several supporting types like `AgentState`, `Agent`, `Direction`, and `Grid`.
- `util.py`: Useful data structures for implementing search algorithms.

### Supporting Files:
- `graphicsDisplay.py`: Graphics for Pacman
- `graphicsUtils.py`: Support for Pacman graphics
- `textDisplay.py`: ASCII graphics for Pacman
- `ghostAgents.py`: Agents to control ghosts
- `keyboardAgents.py`: Keyboard interfaces to control Pacman
- `layout.py`: Code for reading layout files and storing their contents
- `autograder.py`: Project autograder
- `testParser.py`: Parses autograder test and solution files
- `testClasses.py`: General autograding test classes
- `test_cases/`: A directory containing the test cases for each question
- `searchTestClasses.py`: Project-specific autograding test classes

## Getting Started

```
python pacman.py
```

### Basic Commands

- Play a game with a simple agent:
  ```
  python pacman.py --layout testMaze --pacman GoWestAgent
  ```

- Play a game and test the search algorithms:
  ```
  python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
  ```

### Autograder

To run the autograder for a specific question (for example question 1):

```
python autograder.py -q q1 
```

## Implementations

### Question 1: Depth First Search

I implemented the depth-first search (DFS) algorithm in the `depthFirstSearch` function in `search.py`.

Tested the implementation with:

```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```

### Question 2: Breadth-First Search

I implemented the breadth-first search (BFS) algorithm in the `breadthFirstSearch` function in `search.py`.

Tested the implementation with:

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

### Question 3: Uniform Cost Search

I implemented the uniform-cost search (UCS) algorithm in the `uniformCostSearch` function in `search.py`.

Tested the implementation with:

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

### Question 4: A* Search

I implemented the A* search algorithm in the `aStarSearch` function in `search.py`.

Tested the implementation with:

```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

### Question 5: Corners Problem

I implemented the `CornersProblem` search problem in `searchAgents.py`.

Tested the implementation with:

```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

### Question 6: Corners Problem Heuristic

I implemented a non-trivial, consistent heuristic for the `CornersProblem` in `cornersHeuristic`.

Tested the implementation with:

```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

### Question 7: Eating All The Dots (4 points)

I filled in `foodHeuristic` in `searchAgents.py` with a consistent heuristic for the `FoodSearchProblem`.

Tested the implementation with:

```
python pacman.py -l testSearch -p AStarFoodSearchAgent
```

### Question 8: Suboptimal Search (3 points)

I implemented the function `findPathToClosestDot` in `searchAgents.py`.

Tested the implementation with:

```
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```
