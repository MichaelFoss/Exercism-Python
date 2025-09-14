def pad_left(val: int, space_to_take_up: int) -> str:
    padding: str = ''
    remaining_val: int = val if val != 0 else 1
    for i in range(0, space_to_take_up):
        if remaining_val == 0:
            padding += ' '
        remaining_val = remaining_val // 10
    return padding + str(val)

def tally(rows):
    ranking: dict[str, dict] = {}
    for row in rows:
        (team_one, team_two, game_result) = tuple(row.split(";"))
        if team_one not in ranking:
            ranking[team_one] = {
                "name": team_one,
                "wins": 0,
                "losses": 0,
                "draws": 0,
                "points": 0,
            }
        if team_two not in ranking:
            ranking[team_two] = {
                "name": team_two,
                "wins": 0,
                "losses": 0,
                "draws": 0,
                "points": 0,
            }
        if game_result == 'draw':
            ranking[team_one]["draws"] += 1
            ranking[team_two]["draws"] += 1
            ranking[team_one]["points"] += 1
            ranking[team_two]["points"] += 1
        elif game_result == 'win':
            ranking[team_one]["wins"] += 1
            ranking[team_two]["losses"] += 1
            ranking[team_one]["points"] += 3
        elif game_result == 'loss':
            ranking[team_one]["losses"] += 1
            ranking[team_two]["wins"] += 1
            ranking[team_two]["points"] += 3

    table: list[str] = ['Team                           | MP |  W |  D |  L |  P']
    team_names: list[str] = list(ranking.keys())
    team_names.sort(key=lambda x: (-ranking[x]['points'], ranking[x]['name']))
    for team_name in team_names:
        team: dict = ranking[team_name]
        table.append(f"{team['name']}{' ' * (31 - len(team['name']))}| {pad_left(team['wins'] + team['draws'] + team['losses'], 2)} | {pad_left(team['wins'], 2)} | {pad_left(team['draws'], 2)} | {pad_left(team['losses'], 2)} | {pad_left(team['points'], 2)}")

    return table