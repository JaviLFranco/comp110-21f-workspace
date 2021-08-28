"""Relational Operators."""

__author__ = "730521799"

left_hand_side: str = input("Left-Hand Side: ")
right_hand_side: str = input("Right-Hand Side: ")
left_hand_side_int = int(left_hand_side)
right_hand_side_int = int(right_hand_side)
operation_a = str(left_hand_side_int < right_hand_side_int)
operation_b = str(left_hand_side_int >= right_hand_side_int)
operation_c = str(left_hand_side_int == right_hand_side_int)
operation_d = str(left_hand_side_int != right_hand_side_int)
print(left_hand_side + " < " + right_hand_side + " is " + operation_a)
print(left_hand_side + " >= " + right_hand_side + " is " + operation_b)
print(left_hand_side + " == " + right_hand_side + " is " + operation_c)
print(left_hand_side + " != " + right_hand_side + " is " + operation_d)