import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from datetime import datetime
import time as t

ONLY333 = True

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

# these will be used in common throughout the rest of the 3x3 analysis
event_id = "3x3x3"
event_df = event_dfs[0]

# start_time = t.time()
# # all solves
# filename = f"all_singles_scatterplot_{event_id}.png"
# fig, ax = plt.subplots(figsize=(8, 6))
# num_solves = 0
# event_df['wr'] = event_df['best'].cummin()
# for i in range(5):
#     sns.scatterplot(data=event_df, x='date', y=f'value{i+1}', ax=ax, color="#0352fc")
#     num_solves += len(event_df)
# ax.set_title(f"{event_id} Results")
# ax.plot(event_df['date'], event_df['wr'], color='red', label='World Record')
# ax.legend()
# plt.xlabel("Date")
# plt.ylabel("Time")
# plt.savefig(filename)
# plt.close()
# print(f"Plotted {num_solves} {event_id} solves.")
# print(f"Total single plotting took {t.time() - start_time} seconds.")

# start_time = t.time()
# # all completed solves
# filename = f"completed_singles_scatterplot_{event_id}.png"
# fig, ax = plt.subplots(figsize=(8, 6))
# num_solves = 0
# event_best_df = event_df[event_df['best'] > 0]
# event_best_df['wr'] = event_best_df['best'].cummin()
# event_best_avg_df = event_df[event_df['average'] > 0]
# event_best_avg_df['wr'] = event_best_avg_df['average'].cummin()
# for i in range(5):
#     event_df_filtered = event_df[event_df[f'value{i+1}'] > 0]
#     sns.scatterplot(data=event_df_filtered, x='date', y=f'value{i+1}', ax=ax, color="#0352fc")
#     num_solves += len(event_df_filtered)
# ax.set_title(f"{event_id} Results")
# ax.plot(event_best_avg_df['date'], event_best_avg_df['wr'], color='green', label='World Record Average')
# ax.plot(event_best_df['date'], event_best_df['wr'], color='red', label='World Record Single')
# ax.legend()
# plt.xlabel("Date")
# plt.ylabel("Time")
# plt.savefig(filename)
# plt.close()
# print(f"Plotted {num_solves} {event_id} completed solves.")
# print(f"Total completed single plotting took {t.time() - start_time} seconds.")




# start_time = t.time()
# # Filter to include only positive averages
# filtered_df = event_df[(event_df['average'] > 0) & (event_df['date'] >= datetime(2003, 1, 1))]

# # Sort the DataFrame by 'date' and 'average' in ascending order
# filtered_df.sort_values(by=['date', 'average'], ascending=[True, True], inplace=True)

# # Initialize an empty DataFrame to store rows that have been in the fastest 100 times
# historical_top_100_df = pd.DataFrame()

# # Iterate through each unique date in ascending order
# for date in sorted(filtered_df['date'].unique()):
#     # Select rows up to the current date
#     up_to_date_df = filtered_df[filtered_df['date'] <= date]
    
#     # Sort by 'average' to get the fastest times first
#     up_to_date_df_sorted = up_to_date_df.sort_values(by='average', ascending=True)
    
#     # Select the top 100 fastest times up to the current date
#     top_100_up_to_date = up_to_date_df_sorted.head(100)
    
#     # Append these rows to the historical_top_100_df DataFrame
#     historical_top_100_df = pd.concat([historical_top_100_df, top_100_up_to_date])
#     print(date)

# # Remove duplicates in case a row is in the top 100 for multiple dates
# historical_top_100_df.drop_duplicates(inplace=True)

# # Reset index after all operations
# historical_top_100_df.reset_index(drop=True, inplace=True)

# # Optionally, sort the final DataFrame by 'date' and 'average' if needed
# historical_top_100_df.sort_values(by=['date', 'average'], ascending=[True, True], inplace=True)

# # Display the DataFrame
# print(historical_top_100_df)
# historical_top_100_df.to_pickle("t100.pkl")
# print(f"Total top 100 averages determination took {t.time() - start_time} seconds.")

historical_top_100_df = pd.read_pickle("t100.pkl")

start_time = t.time()
# all solves
filename = f"top_100_avgs_{event_id}.png"
fig, ax = plt.subplots(figsize=(8, 6))
# num_solves = 0
# Ensure the DataFrame is sorted by date
event_df.sort_values('date', inplace=True)
event_df['wr'] = event_df[(event_df['average'] > 0) & (event_df['date'] >= datetime(2003, 1, 1))]['average'].cummin()
# for i in range(5):
#     sns.scatterplot(data=event_df, x='date', y=f'value{i+1}', ax=ax, color="#0352fc")
#     num_solves += len(event_df)
sns.scatterplot(data=historical_top_100_df, x='date', y='average', ax=ax, color="#0352fc")
ax.set_title(f"{event_id} Results")
ax.plot(event_df['date'], event_df['wr'], color='red', label='World Record')
ax.legend()
plt.xlabel("Date")
plt.ylabel("Time")
plt.savefig(filename)
plt.close()
print(f"Total top 100 avgs plotting took {t.time() - start_time} seconds.")

start_time = t.time()
log_historical_top_100_df = historical_top_100_df.assign(average=np.log(historical_top_100_df["average"]))
# all solves
filename = f"log_top_100_avgs_{event_id}.png"
fig, ax = plt.subplots(figsize=(8, 6))
# num_solves = 0
# Ensure the DataFrame is sorted by date
event_df.sort_values('date', inplace=True)
event_df['wr'] = event_df[(event_df['average'] > 0) & (event_df['date'] >= datetime(2003, 1, 1))]['average'].cummin()
wrs = event_df.assign(wr=np.log(event_df['wr']))
# for i in range(5):
#     sns.scatterplot(data=event_df, x='date', y=f'value{i+1}', ax=ax, color="#0352fc")
#     num_solves += len(event_df)
sns.scatterplot(data=log_historical_top_100_df, x='date', y='average', ax=ax, color="#0352fc")
ax.set_title(f"{event_id} Results")
ax.plot(event_df['date'], wrs['wr'], color='red', label='World Record')
ax.legend()
plt.xlabel("Date")
plt.ylabel("ln(Time)")

# Plot the regression line
ax.plot([datetime(2004, 1, 1), datetime(2024, 1, 1)], [7.6, 6.2], color='green')

plt.savefig(filename)
plt.close()
print(f"Total top 100 avgs plotting took {t.time() - start_time} seconds.")

# start_time = t.time()
# # Filter to include only positive singles
# s_filtered_df = event_df[(event_df['best'] > 0) & (event_df['date'] >= datetime(2004, 1, 1))]

# # Sort the DataFrame by 'date' and 'best' in ascending order
# s_filtered_df.sort_values(by=['date', 'best'], ascending=[True, True], inplace=True)

# # Initialize an empty DataFrame to store rows that have been in the fastest 100 times
# s_historical_top_100_df = pd.DataFrame()

# # Iterate through each unique date in ascending order
# for date in sorted(s_filtered_df['date'].unique()):
#     # Select rows up to the current date
#     s_up_to_date_df = s_filtered_df[s_filtered_df['date'] <= date]
    
#     # Sort by 'average' to get the fastest times first
#     s_up_to_date_df_sorted = s_up_to_date_df.sort_values(by='best', ascending=True)
    
#     # Select the top 100 fastest times up to the current date
#     s_top_100_up_to_date = s_up_to_date_df_sorted.head(100)
    
#     # Append these rows to the historical_top_100_df DataFrame
#     s_historical_top_100_df = pd.concat([s_historical_top_100_df, s_top_100_up_to_date])
#     print(date)

# # Remove duplicates in case a row is in the top 100 for multiple dates
# s_historical_top_100_df.drop_duplicates(inplace=True)

# # Reset index after all operations
# s_historical_top_100_df.reset_index(drop=True, inplace=True)

# # Optionally, sort the final DataFrame by 'date' and 'average' if needed
# s_historical_top_100_df.sort_values(by=['date', 'best'], ascending=[True, True], inplace=True)

# # Display the DataFrame
# print(historical_top_100_df)
# s_historical_top_100_df.to_pickle("s_t100.pkl")
# print(f"Total top 100 averages determination took {t.time() - start_time} seconds.")

s_historical_top_100_df = pd.read_pickle("s_t100.pkl")
start_time = t.time()
# all solves
filename = f"s_top_100_avgs_{event_id}.png"
fig, ax = plt.subplots(figsize=(8, 6))
# num_solves = 0
# Ensure the DataFrame is sorted by date
event_df.sort_values('date', inplace=True)
event_df['wra'] = event_df[(event_df['average'] > 0) & (event_df['date'] >= datetime(2004, 1, 1))]['average'].cummin()
event_df['wrs'] = event_df[(event_df['best'] > 0) & (event_df['date'] >= datetime(2004, 1, 1))]['best'].cummin()
# for i in range(5):
#     sns.scatterplot(data=event_df, x='date', y=f'value{i+1}', ax=ax, color="#0352fc")
#     num_solves += len(event_df)
sns.scatterplot(data=historical_top_100_df, x='date', y='average', ax=ax, color="#0352fc", label="Average")
sns.scatterplot(data=s_historical_top_100_df, x='date', y='best', ax=ax, color="#FC0000", alpha=0.3, label="Single")
ax.set_title(f"{event_id} Results")
ax.plot(event_df['date'], event_df['wra'], color='green', label='World Record Average')
ax.plot(event_df['date'], event_df['wrs'], color='yellow', label='World Record Single')
ax.legend()
plt.xlabel("Date")
plt.ylabel("Time")
plt.savefig(filename)
plt.close()
print(f"Total top 100 avgs plotting took {t.time() - start_time} seconds.")

start_time = t.time()
log_historical_top_100_df = historical_top_100_df.assign(average=np.log(historical_top_100_df["average"]))
s_log_historical_top_100_df = s_historical_top_100_df.assign(best=np.log(s_historical_top_100_df["best"]))
# all solves
filename = f"s_log_top_100_avgs_{event_id}.png"
fig, ax = plt.subplots(figsize=(8, 6))
# num_solves = 0
# Ensure the DataFrame is sorted by date
event_df.sort_values('date', inplace=True)
event_df['wra'] = event_df[(event_df['average'] > 0) & (event_df['date'] >= datetime(2004, 1, 1))]['average'].cummin()
event_df['wrs'] = event_df[(event_df['best'] > 0) & (event_df['date'] >= datetime(2004, 1, 1))]['best'].cummin()
wrs = event_df.assign(wr=np.log(event_df['wra']))
wrss = event_df.assign(wr=np.log(event_df['wrs']))
# for i in range(5):
#     sns.scatterplot(data=event_df, x='date', y=f'value{i+1}', ax=ax, color="#0352fc")
#     num_solves += len(event_df)
sns.scatterplot(data=log_historical_top_100_df, x='date', y='average', ax=ax, color="#0352fc", label="Average")
sns.scatterplot(data=s_log_historical_top_100_df, x='date', y='best', ax=ax, color="#FC0000", alpha=0.3, label="Single")
ax.set_title(f"{event_id} Results")
ax.plot(event_df['date'], wrs['wr'], color='green', label='World Record Average')
ax.plot(event_df['date'], wrss['wr'], color='yellow', label='World Record Single')
ax.legend()
plt.xlabel("Date")
plt.ylabel("ln(Time)")

# Plot the regression line
# ax.plot([datetime(2004, 1, 1), datetime(2024, 1, 1)], [7.6, 6.2], color='green')

plt.savefig(filename)
plt.close()
print(f"Total top 100 avgs plotting took {t.time() - start_time} seconds.")