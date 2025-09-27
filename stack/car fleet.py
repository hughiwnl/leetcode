class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse = True)
        stack = []

        for p,s in pair:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
'''
target = 12
position = [10, 8, 0, 5, 3]
speed = [ 2, 4, 1, 1, 3]
Pair + sort:
[(10,2), (8,4), (5,1), (3,3), (0,1)]
Times to target:
(10,2): (12-10)/2 = 1 hour → stack = [1]
(8,4): (12-8)/4 = 1 hour → stack = [1,1] → last car takes ≤ previous → pop → stack = [1]
(5,1): (12-5)/1 = 7 hours → stack = [1,7]
(3,3): (12-3)/3 = 3 hours → stack = [1,7,3] → 3 ≤ 7 → pop → stack = [1,7]
(0,1): (12-0)/1 = 12 hours → stack = [1,7,12]
Answer = len(stack) = 3 fleets.
'''