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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    ### COMMENT ALL THE PRINT MESSAGES TO IMPROVE RUNTIME
    """ Initialize """
    starting_point = problem.getStartState()
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    """ DepthFirstSearch : Implementation requires a stack """
    fringe = util.Stack()
    visited = []

    """ Fringe will contain all the possible options to visit """
    fringe.push([(starting_point, 'STOP', 0)])

    """ Loop condition fulfillment condition :
            1. Either the fringe is empty
            2. We encounter the goal condition """
    while not fringe.isEmpty():
        """ Get the top of the stack """
        current_path = fringe.pop()
        # print "Current Path: ", current_path

        """ Get the current state """
        current_coordinates, _direction, _cost = current_path[len(current_path)-1]
        # print "Current Coordinates: ", current_coordinates

        """ Expand current_coordinates only if not in visited """
        if not current_coordinates in visited:
            visited.append(current_coordinates)
            # print "Visited updated to: ", visited

            """ If the current_coordinates matches the goal state, then return directions """
            if problem.isGoalState(current_coordinates):
                # print "Path coordinates followed: ", visited
                return map(lambda directions: directions[1], current_path[1:])

            non_visited_nodes = filter(lambda successors: not successors[0] in visited , problem.getSuccessors(current_coordinates))
            # print "Non Visited nodes: ", non_visited_nodes
           
            """ Create path """
            for successor in non_visited_nodes:
                next_node = list(current_path)
                next_node.append(successor)
                fringe.push(next_node)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    ### COMMENT ALL THE PRINT MESSAGES TO IMPROVE RUNTIME
    """ Initialize """
    starting_point = problem.getStartState()
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())

    """ BreadthFirstSearch : Implementation requires a queue """
    fringe = util.Queue()
    visited = []

    """ Fringe will contain all the possible options to visit """
    fringe.push([(starting_point, 'STOP', 0)])

    """ Loop condition fulfillment condition :
       1. Either the fringe is empty
       2. We encounter the goal condition """
    while not fringe.isEmpty():
        """ Get the head of the queue """
        current_path = fringe.pop()
        # print "Current Path: ", current_path

        """ Get the current state """
        current_coordinates, _direction, _cost = current_path[len(current_path)-1]
        # print "Current Coordinates: ", current_coordinates

        """ Expand current_state only if not in visited """
        if not current_coordinates in visited:
            visited.append(current_coordinates)
            # print "Visited updated to: ", visited

            """ If the current state matches the goal state, then return state """
            if problem.isGoalState(current_coordinates):
                # print "Path coordinates followed: ", visited
                return map(lambda directions: directions[1], current_path[1:])

            non_visited_nodes = filter(lambda successors: not successors[0] in visited, problem.getSuccessors(current_coordinates))
            # print "Non Visited nodes: ", non_visited_nodes

            """ Create Path """
            for successor in non_visited_nodes:
                next_node = list(current_path)
                next_node.append(successor)
                fringe.push(next_node)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    ### COMMENT ALL THE PRINT MESSAGES TO IMPROVE RUNTIME
    """ Initialize """
    starting_point = problem.getStartState()
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())

    """ UniformCostSearch : Implementation requires a Priority Queue """
    fringe = util.PriorityQueue()
    visited = []

    """ Fringe will contain all the possible options to visit """
    start_state = ([(starting_point, 'STOP', 0)], 0)
    fringe.push(start_state, 0)

    """ Loop condition fulfillment condition :
            1. Either the fringe is empty
            2. We encounter the goal condition """
    while not fringe.isEmpty():
        """ Get the head of the queue """
        current_path = fringe.pop()
        # print "Current Path: ", current_path
    
        """ Get the current coordinates """
        current_coordinates, _direction, _cost = current_path[0][len(current_path[0]) - 1]
        # print "Current Coordinates: ", current_coordinates

        """ Expand current_coordinates only if not in visited """
        if not current_coordinates in visited:
            visited.append(current_coordinates)
            # print "Visited updated to: ", visited

            """ If the current_coordinates matches the goal state, then return directions """
            if problem.isGoalState(current_coordinates):
                # print "Path coordinates followed: ", visited
                return map(lambda directions: directions[1], current_path[0][1:])

            non_visited_nodes = filter(lambda successors: not successors[0] in visited, problem.getSuccessors(current_coordinates))
            # print "Non Visited nodes: ", non_visited_nodes

            for successor in non_visited_nodes:
                """ Calculate cost """
                cost = current_path[1] + successor[2]
                next_node = (list(current_path[0]), cost)
                next_node[0].append(successor)
                fringe.push(next_node, cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """Search the node that has the lowest combined cost and heuristic first."""
    ### COMMENT ALL THE PRINT MESSAGES TO IMPROVE RUNTIME
    """ Initialize """
    starting_point = problem.getStartState()
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())

    """ A-star Search : Implementation requires a Prioirity Queue """
    fringe = util.PriorityQueue()
    visited = []

    """ Fringe will contain all the possible options to visit """
    start_state = ([(starting_point, 'STOP', 0)], 0)
    fringe.push(start_state, 0)

    """ Loop condition fulfillment condition :
            1. Either the fringe is empty
            2. We encounter the goal condition """
    while not fringe.isEmpty():
        """ Get the head of the queue """
        current_path = fringe.pop()
        # print "Current Path: ", current_path

        """ Get the current state """
        current_coordinates, _direction, _cost  = current_path[0][len(current_path[0]) - 1]
        # print "Current Coordinates: ", current_coordinates

        """ Expand current_coordinates only if not in visited """
        if not current_coordinates in visited:
            visited.append(current_coordinates)
            # print "Visited updated to: ", visited

            """ If the current_coordinates matches the goal state, then return directions """
            if problem.isGoalState(current_coordinates):
                # print "Path coordinates followed: ", visited
                return map(lambda directions: directions[1], current_path[0][1:])

            non_visited_nodes = filter(lambda successors: not successors[0] in visited, problem.getSuccessors(current_coordinates))
            # print "Non Visited nodes: ", non_visited_nodes

            for successor in non_visited_nodes:
                """ Calculate cost """
                cost = current_path[1] + successor[2]
                next_item = (list(current_path[0]), cost)
                next_item[0].append(successor)
                fringe.push(next_item, cost + heuristic(successor[0], problem))

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
