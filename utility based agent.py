def utility_based_agent(utility):

    best_action = max(utility, key=utility.get)

    return best_action


utility = {
    "Move": 3,
    "Clean": 9,
    "Wait": 1
}

action = utility_based_agent(utility)

print("Best Action:", action)
