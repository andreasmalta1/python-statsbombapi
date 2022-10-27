from statsbombpy import sb

print(sb.competitions())
print(sb.matches(competition_id=43, season_id=3))
events = sb.events(match_id=8657)
print(events.head())
print(events.columns)
events=events[['team', 'type', 'minute', 'location', 'pass_end_location', 'player']]
events=events[events['team']=='England'].reset_index()
print(events.head(20))