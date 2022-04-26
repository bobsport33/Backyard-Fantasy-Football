import nflfastpy as nfl
import numpy as np
import pandas as pd

def season_target_share(): 
    df = nfl.load_pbp_data(2021)

    teams = df['posteam'].dropna().unique().tolist()

    pass_df = df.loc[df['pass_attempt'] == 1]

    target_df = df.groupby(['receiver_player_name', 'posteam'], as_index=False)['pass_attempt'].sum().merge(df.loc[df['receiver_player_id'].notnull()].groupby(['posteam'], as_index=False)['pass_attempt'].sum(), on=['posteam'], suffixes=('_player', '_team'))
    target_df['target_share'] = round(target_df['pass_attempt_player'] / target_df['pass_attempt_team'] * 100)

    # for team in teams:
    #   team_df = target_df.loc[target_df['posteam'] == team]
    #   print(team)
    #   print(team_df.sort_values(by='target_share', ascending=False).head(5))

    top_40 = target_df.sort_values(by='target_share', ascending=False).head(40)
    top_40.reset_index(drop=True, inplace=True)
    top_40.index += 1
    top_40.rename(columns={'receiver_player_name': "Player Name", "posteam": "Team", "pass_attempt_player": "Player Pass Attempt- Season", 'pass_attempt_team': 'Team Pass Attmept- Season', 'target_share': 'Target Share'}, inplace=True)

    return top_40

def weekly_target_share(week): 
    df = nfl.load_pbp_data(2021)

    week = week
    if type(week) == int:
        df = df.loc[df['week'] == week]

    teams = df['posteam'].dropna().unique().tolist()

    pass_df = df.loc[df['pass_attempt'] == 1]

    target_df = df.groupby(['receiver_player_name', 'posteam'], as_index=False)['pass_attempt'].sum().merge(df.loc[df['receiver_player_id'].notnull()].groupby(['posteam'], as_index=False)['pass_attempt'].sum(), on=['posteam'], suffixes=('_player', '_team'))
    target_df['target_share'] = round(target_df['pass_attempt_player'] / target_df['pass_attempt_team'] * 100)

    # for team in teams:
    #   team_df = target_df.loc[target_df['posteam'] == team]
    #   print(team)
    #   print(team_df.sort_values(by='target_share', ascending=False).head(5))

    top_40 = target_df.sort_values(by='target_share', ascending=False).head(40)
    top_40.reset_index(drop=True, inplace=True)
    top_40.index += 1
    top_40.rename(columns={'receiver_player_name': "Player Name", "posteam": "Team", "pass_attempt_player": "Player-Pass Attempt", 'pass_attempt_team': 'Team-Pass Attmept', 'target_share': 'Target Share'}, inplace=True)

    return top_40

