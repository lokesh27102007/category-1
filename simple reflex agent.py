def simple_reflex_agent(percept):

    if percept == "dirty":
        return "Clean the room"

    elif percept == "clean":
        return "Move to next room"

    else:
        return "Do nothing"


print(simple_reflex_agent("dirty"))
print(simple_reflex_agent("clean"))
