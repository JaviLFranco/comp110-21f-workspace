"""Drawing forests in a loop."""

__author__ = "730521799"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth = int(input("Depth: "))
depth_b = depth + 1
while depth >= 0:
    trees = depth_b - depth
    print(trees * TREE)
    depth = depth - 1