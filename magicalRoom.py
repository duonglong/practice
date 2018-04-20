# --*-- coding: utf-8 --*--
"""
You're an adventurer, and today you're exploring a big castle.
When you came in, you found a note on the wall of the room.
The note said that the castle contains n rooms, all of which are magical.
The ith room contains exactly one door which leads to another room roomsi.
Because the rooms are magical, it is possible that roomsi = i.

The note indicated that to leave the castle, you need to visit all the rooms,
starting from the current one, and return to the start room without visiting any room twice (except start one).
The current room has the number 0. And to make things more interesting,
you have to change the exit of exactly one door, i.e. to change one value roomsi.

Now you need to figure out how to leave the castle.
You need to return an array of two numbers numbers result[0] and result[1],
where result[0] is the number of the room with the exit you're going to change
and result[1] is the new room number to which the door from result[0] leads.
The new exit shouldn't be equal to the old one,
and after this operation is done it should be possible to visit all the rooms,
starting from 0, without visiting any room twice, and return to room 0 afterall.
If there is no answer, return [-1, -1] (and you're stuck in the castle forever).

Example

For rooms = [0, 1, 2], the output should be
magicalRooms(rooms) = [-1, -1];

For rooms = [0, 2, 0], the output should be
magicalRooms(rooms) = [0, 1].

After changing the exit of room 0 to 1, we have the following scheme of exits:

Room 0 leads to room 1;
Room 1 leads to room 2;
Room 2 leads to room 0.
As we can see, path 0 -> 1 -> 2 is valid and visits all the rooms exactly once.

Input/Output

[execution time limit] 4 seconds (py)

[input] array.integer rooms

An array of integers, where roomsi represents the 0-based exit from the room number i.

Guaranteed constraints:
3 ≤ rooms.length ≤ 10^5,
0 ≤ rooms[i] < rooms.length.

[output] array.integer

An array containing exactly 2 numbers, result[0] and result[1],
where result[0] is the room with the exit that's changing and result[1] is the number of the new exit of this room. result[1] shouldn't be equal to the old exit, and it should be possible to visit all rooms starting from 0 without visiting any room twice, and return to room 0 afterall. If this is impossible, return [-1, -1]
"""


def magicalRooms(rooms):
    n = len(rooms) - 1
    x = n * (n + 1) / 2 - sum(rooms)
    s = set(range(n + 1)) - set(rooms)
    r = list(s)[0] - x
    print r, list(s)[0]
    if x == 0 or len(s) > 1:
        return [-1, -1]
    if rooms[0] == 0 and len(s):
        return [-1, -1]
    for i in rooms:
        pass


# import random
# test = range(0, 100001)
# random.shuffle(test)
tests = [
    [3, 0, 4, 6, 5, 2, 5],  # [4, 1]
    [0, 2, 0],  # [0, 1]
    [4, 5, 0, 1, 4, 2]  # [4, 3]
]
for t in tests:
    magicalRooms(t)
