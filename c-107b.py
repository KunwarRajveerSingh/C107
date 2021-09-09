import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

student_df = df.loc[df['student_id'] == "TRL_imb"]
mean = student_df.groupby("level")["attempt"].mean()
print(mean)

fig = go.Figure(go.Bar(
    x=mean,
    y=['Level1', 'Level2', 'Level3', 'Level4'],
    orientation='h'
))
fig.show()