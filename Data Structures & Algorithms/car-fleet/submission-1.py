class Solution:

  def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
    # Pair position and speed, then sort by position descending (closest to target first)
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []

    for p, s in sorted(pair, reverse=True):
      # Calculate time required to reach the target
      time = (target - p) / s
      stack.append(time)

      # If current car takes less or equal time than the car ahead,
      # it catches up and becomes part of that fleet.
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()

    return len(stack)