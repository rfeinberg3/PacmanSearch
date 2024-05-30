# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack_DFS = util.Stack() # Stack object
    startState = problem.getStartState()
    nodeCollection = [] # collection to keep track of explored nodes
    nodeCollection.append(startState)



    def dig(pos=startState, collection=nodeCollection, stack=stack_DFS):
        if not problem.isGoalState(pos):
            successors = problem.getSuccessors(pos)
            for successor in successors[::-1]:
                successor_position = successor[0]
                if successor_position not in collection: # if successor position is not in our node collection
                    stack.push(successor) # take this move
                    pos = successor_position # update pos to new position
                    collection.append(successor_position) # mark new node as explored
                    goal_found = dig(pos, collection, stack)
                    if goal_found:
                        return True
            if not stack.isEmpty():
                stack.pop()
        else:
            readStack(stack)
            return True



    def readStack(stackle):
        global actions # list of actions to return
        actions = []
        while not (stackle.isEmpty()):
            node = stackle.pop()  # pop stack
            direction = node[1]  # direction action
            actions.append(direction)  # append directions
            if node[0] == problem.getStartState():  # once we hit the starting node we don't want to add any more actions, so break
                break
        actions = actions[::-1]


    # Start main
    if problem.isGoalState(problem.getStartState()):
        return []

    dig()
    return actions

    util.raiseNotDefined()
    # End main
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue_BFS = util.Queue() # a queue of paths
    startState = problem.getStartState()
    nodeCollection = [] # collection to keep track of explored nodes
    nodeCollection.append(startState)
    actions = []

    queue_BFS.push([startState])
    while queue_BFS: # while the queue is not empty
        path = queue_BFS.pop() # path = the next in the queue (FIFO order)
        if path == [startState]:
            node_position = startState
        else:
            node_position = path[-1][0] # this is our current position
        ## Check goal
        if problem.isGoalState(node_position):
            # our path contains the goal
            for node in path[::-1]:
                if node == startState:
                    break
                actions.append(node[1]) # append just the direction element from each node
            break
        ## end check goal
        successors = problem.getSuccessors(node_position) # successors of current node
        for successor in successors[::-1]:
            successor_position = successor[0]
            if successor_position not in nodeCollection:  # if successor position is not in our node collection
                new_path = list(path) # new_path = path (complete copy)
                new_path.append(successor) # append the new node to the path
                nodeCollection.append(successor_position)
                queue_BFS.push(new_path) # push the new path to the queue

    actions = actions[::-1]
    return actions
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    pQueue_UCS = util.PriorityQueue() # a queue of paths
    startState = problem.getStartState()
    nodeCollection = [] # collection to keep track of explored nodes
    nodeCollection.append(startState)
    actions = []


    pQueue_UCS.push([startState], 0)
    while pQueue_UCS:
        path = pQueue_UCS.pop()  # path = the next in the queue (FIFO order)
        if path == [startState]:
            node_position = startState
        else:
            node_position = path[-1][0]  # this is our current position
        if problem.isGoalState(node_position):
            # our path contains the goal
            for node in path[::-1]:
                if node == startState:
                    break
                actions.append(node[1])  # append just the direction element from each node
            break

        successors = problem.getSuccessors(node_position)  # successors of current node

        for successor in successors[::-1]:
            successor_position = successor[0]
            successor_cost = successor[2]
            if successor_position not in nodeCollection or problem.isGoalState(successor_position):  # if successor position is not in our node collection
                nodeCollection.append(successor_position)  # mark new node as explored
                new_path = list(path)  # new_path = path (complete copy)
                new_path.append(successor)  # append the new node to the path
                for node in path:
                    if node == startState:
                        continue
                    successor_cost += node[2]
                pQueue_UCS.push(new_path, successor_cost)  # push the new path to the queue

    return actions[::-1]
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pQueue_A = util.PriorityQueue() # a queue of paths
    startState = problem.getStartState()
    nodeCollection = [] # collection to keep track of explored nodes
    nodeCollection.append(startState)
    actions = []

    pQueue_A.push([startState], 0)
    while pQueue_A:
        path = pQueue_A.pop()  # path = the next in the queue (FIFO order)
        if path == [startState]:
            node_position = startState
        else:
            node_position = path[-1][0]  # this is our current position
        if problem.isGoalState(node_position):
            # our path contains the goal
            for node in path[::-1]:
                if node == startState:
                    break
                actions.append(node[1])  # append just the direction element from each node
            break

        successors = problem.getSuccessors(node_position)  # successors of current node

        for successor in successors[::-1]:
            successor_position = successor[0]
            successor_cost = successor[2]
            if successor_position not in nodeCollection or problem.isGoalState(successor_position):  # if successor position is not in our node collection
                nodeCollection.append(successor_position)  # mark new node as explored
                new_path = list(path)  # new_path = path (complete copy)
                new_path.append(successor)  # append the new node to the path
                for node in path:
                    if node == startState:
                        continue
                    successor_cost += node[2]
                G = successor_cost
                H = heuristic(successor_position, problem)
                F = G + H
                pQueue_A.push(new_path, F)  # push the new path to the queue

    return actions[::-1]
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
