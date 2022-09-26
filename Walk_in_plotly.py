import pandas as pd
import plotly.graph_objects as go

print('Enter file name:')
x = input()

df = pd.read_csv(x+'.csv', skiprows=12)
df.rename(columns={":DEV_SIZE": "date", "2": "Temp","2.1":"rH"}, inplace = True)
df['date'] = pd.to_datetime(df['date'])

fig=go.Figure()
fig.add_trace(go.Scatter(
        x = df['date'],
        y = df['Temp'],
        name = 'Temp'))
fig.add_trace(go.Scatter(
        x = df['date'],
        y = df['rH'],
        name = 'rH'))

fig.update_layout(xaxis_rangeslider_visible=True, template='plotly_dark')
fig.update_layout(yaxis_title='Temp/%rH', xaxis_title='Date')

fig.show()