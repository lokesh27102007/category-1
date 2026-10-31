def goal_based_agent(location, rooms):

    dirty = []

    for room, status in rooms.items():
        if status == "Dirty":
            dirty.append(room)

    if not dirty:
        return "Goal Achieved"

    if location in dirty:
        rooms[location] = "Clean"
        return "Clean the room"

    return "Move to " + dirty[0]


rooms = {
    "A": "Dirty",
    "B": "Dirty",
    "C": "Clean"
}

print(goal_based_agent("A", rooms))
