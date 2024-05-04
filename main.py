import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import time as t

ONLY333 = False

start_time = t.time()
# Import all results
results_df = pd.read_csv("WCA_export_Results.tsv", sep="\t")
print(f"Results import took {t.time() - start_time} seconds.")

start_time = t.time()
# Import all competition data [end of the competition]
competition_df = pd.read_csv("WCA_export_Competitions.tsv", sep="\t")
print(f"Competitions import took {t.time() - start_time} seconds.")

start_time = t.time()
# Create a dictionary to store the date information
date_dict = {
    competition_id: dt.datetime.strptime(f"{endDay} {endMonth} {year}", "%d %m %Y")
    for competition_id, endDay, endMonth, year in zip(
        competition_df['id'],
        competition_df['endDay'],
        competition_df['endMonth'],
        competition_df['year']
    )
}

# Append the date to each result, using the dictionary
results_df['date'] = results_df['competitionId'].map(date_dict)
print(f"Date assignment took {t.time() - start_time} seconds.")

start_time = t.time()
# Now split the dataframe by event
events = results_df["eventId"].unique()
event_dfs = [results_df[results_df["eventId"] == event] for event in events]
print(f"Event splitting took {t.time() - start_time} seconds.")

# all best singles
start_time = t.time()
if (not ONLY333):
    # plot each event
    for i, event_df in enumerate(event_dfs):
        event_id = events[i]
        filename = f"raw_best_single_scatterplot_{event_id}.png"
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(data=event_df, x='date', y='best', ax=ax)
        ax.set_title(f"Scatter Plot for {event_id}")
        plt.savefig("Raw_Best_Single_Scatterplots/" + filename)
        plt.close()
        print(f"Plotted {len(event_df)} {event_id} best solves.")
else:
    event_id = "333"
    event_df = event_dfs[0]
    filename = f"raw_best_single_scatterplot_{event_id}.png"
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=event_df, x='date', y='best', ax=ax)
    ax.set_title(f"Scatter Plot for {event_id}")
    plt.savefig("Raw_Best_Single_Scatterplots/" + filename)
    plt.close()
    print(f"Plotted {len(event_df)} {event_id} best solves.")
print(f"Raw plotting took {t.time() - start_time} seconds.")

# nonzero best singles
start_time = t.time()
# plot each event
if(not ONLY333):
    for i, event_df in enumerate(event_dfs):
        event_id = events[i]
        filename = f"nonzero_raw_best_single_scatterplot_{event_id}.png"
        fig, ax = plt.subplots(figsize=(8, 6))
        event_df_filtered = event_df[event_df['best'] > 0]
        sns.scatterplot(data=event_df_filtered, x='date', y='best', ax=ax)
        ax.set_title(f"Scatter Plot for {event_id}")
        plt.savefig("Nonzero_Raw_Best_Single_Scatterplots/" + filename)
        plt.close()
        print(f"Plotted {len(event_df_filtered)} {event_id} best nonzero completed solves.")
else:
    event_id = "333"
    event_df = event_dfs[0]
    filename = f"nonzero_raw_best_single_scatterplot_{event_id}.png"
    fig, ax = plt.subplots(figsize=(8, 6))
    event_df_filtered = event_df[event_df['best'] > 0]
    sns.scatterplot(data=event_df_filtered, x='date', y='best', ax=ax)
    ax.set_title(f"Scatter Plot for {event_id}")
    plt.savefig("Nonzero_Raw_Best_Single_Scatterplots/" + filename)
    plt.close()
    print(f"Plotted {len(event_df_filtered)} {event_id} best nonzero completed solves.")
print(f"Nonzero raw plotting took {t.time() - start_time} seconds.")