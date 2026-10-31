class ModelBasedAgent:
    def __init__(self):
        self.model = {}

    def act(self, location, percept):
        self.model[location] = percept

        if percept == "Dirty":
            return "Suck"
        else:
            return "Move"

agent = ModelBasedAgent()

print(agent.act("A", "Dirty"))
print(agent.act("B", "Clean"))

print("Model:", agent.model)
