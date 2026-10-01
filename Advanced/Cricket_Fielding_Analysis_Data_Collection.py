import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
file_path = "cricket.xlsx"

# Read the Performance Matrix
df = pd.read_excel(
    file_path,
    header=22,
    usecols="B:L",
    nrows=7
)

print("Cricket Fielding Performance Data:")
print(df)

# Select 3 players
players = df.iloc[0:3]

print("\nData of 3 Players:")
print(players)


# Display fielding efforts
print("\nFielding Efforts of 3 Players:")

for index, row in players.iterrows():
    print("\nPlayer:", row["Player Name"])
    print("Clean Picks:", row["Clean Picks (CP)"])
    print("Good Throws:", row["Good Throws (GT)"])
    print("Catches:", row["Catches (C)"])
    print("Dropped Catches:", row["Dropped Catches (DC)"])
    print("Stumpings:", row["Stumpings (S)"])
    print("Run Outs:", row["Run Outs (RO)"])
    print("Missed Run Outs:", row["Missed Run Outs (MR)"])
    print("Direct Hits:", row["Direct Hits (DH)"])
    print("Runs Saved:", row["Runs Saved (RS)"])
    print("Performance Score:", row["Performance Score (PS)"])


# Bar Chart.
plt.figure(figsize=(8, 5))

plt.bar(
    players["Player Name"],
    players["Performance Score (PS)"]
)

plt.title("Performance Score of 3 Players")
plt.xlabel("Players")
plt.ylabel("Performance Score")

plt.tight_layout()
plt.show()
