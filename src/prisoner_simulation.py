import random

def random_strategy(drawers):
    """
    Each prisoner picks at-most 50 random drawers.
    If all prisoners find their number, return 1. 
    Else everyone is executed, return 0.
    
    i.e Return 1 if all prisoners succeed, return 0 otherwise.
    """
    for i in range(1, 101):
        picked = set()
        for _ in range(50):
            r = random.randint(0, 99)
            while r in picked:
                r = random.randint(0, 99)
            picked.add(r)
            if drawers[r] == i:
                break
        else:
            return 0
    return 1

def best_strategy():
    """
    Implements the optimal 'loop-following' strategy.
    Returns 1 if all prisoners succeed, 0 otherwise.
    """
    drawers = list(range(1, 101))
    random.shuffle(drawers)
    mapping = {i + 1: drawers[i] for i in range(100)}

    for i in range(1, 101):
        curr = i
        for attempts in range(50):
            if mapping[curr] == i:
                break
            curr = mapping[curr]
        else:
            return 0
    return 1

def run_case(trials=2000):
    """
    Run multiple trials and return success percentage for both strategies.
    """
    best_wins = 0
    random_wins = 0
    for _ in range(trials):
        # Prepare drawers for random strategy
        drawers = list(range(1, 101))
        random.shuffle(drawers)
        if random_strategy(drawers):
            random_wins += 1
        if best_strategy():
            best_wins += 1
    return (best_wins / trials) * 100, (random_wins / trials) * 100

def run_experiment(rounds=10):
    """
    Average the result over multiple runs.
    """
    best_total = 0
    random_total = 0
    for _ in range(rounds):
        best, random_ = run_case()
        best_total += best
        random_total += random_
    print(f"Average Probability of Success with Best Strategy: {best_total / rounds:.2f}%")
    print(f"Average Probability of Success with Random Strategy: {random_total / rounds:.2f}%")

if __name__ == "__main__":
    run_experiment()

