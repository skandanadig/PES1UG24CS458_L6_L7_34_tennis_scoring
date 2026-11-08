def parse_score(text):
    if not isinstance(text, str):
        return None
    parts = text.split('-')
    if len(parts) != 2:
        return None
    a, b = parts[0].strip(), parts[1].strip()
    try:
        return int(a), int(b)
    except (ValueError, TypeError):
        return None


def game_lead(text):
    if not isinstance(text, str):
        return None
    points = {'0': 0, '15': 1, '30': 2, '40': 3}
    parts = text.split('-')
    if len(parts) != 2:
        return None
    first, second = parts[0].strip(), parts[1].strip()
    if first not in points or second not in points:
        return None
    return points[first] - points[second]


def set_spread(games_csv):
    if not isinstance(games_csv, str):
        return None
    if not games_csv.strip():
        return None
    games = []
    for g in games_csv.split(','):
        g = g.strip()
        if not g:
            continue
        try:
            games.append(int(g))
        except (ValueError, TypeError):
            return None
    if not games:
        return None
    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    print("Spread:", result)


if __name__ == "__main__":
    main()
