"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to
its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around
the circuit once in the clockwise direction, otherwise return -1.
If there exists a solution, it is guaranteed to be unique
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        i = 0        
        while i < len(gas):
            tank = gas[i] - cost[i]
            j = i
            while tank >= 0:
                j += 1
                if j == len(gas):
                    return i
                tank += gas[j] - cost[j]
            i = j + 1
