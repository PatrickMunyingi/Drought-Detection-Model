import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Drought Detection Visualization in Kenya Based on the different Return Periods")
st.write("Visualize Drought detection capabilities of the model based on return periods and rainfall types.")

# User Input
return_period = st.selectbox("Select Return Period", options=["1 in 4", "1 in 8", "1 in 10"])
rainfall_type = st.selectbox("Select Rainfall Type", options=["Both", "Long", "Short"])

if return_period == "1 in 4" and rainfall_type == "Both":
    data = pd.read_excel("C:/Users/PatrickMunyingi/Downloads/CREST Pricing Simulations/1-in-4.xlsx", sheet_name="AnnualPayouts(all sites)", index_col=0)
    data['Average'] = data.mean(axis=1)
    data = data * 100
    fig = px.bar(data['Average'], x=data.index, y=data['Average'], title='Average Payout for Both Rains (1 in 4)')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        title={'text': "Average Payout for Both Rains (1 in 4)", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(family="Times New Roman", size=18, color="RebeccaPurple")
    )
    st.plotly_chart(fig)

elif return_period == "1 in 4" and rainfall_type == "Long":
    data = pd.read_excel("C:/Users/PatrickMunyingi/Downloads/CREST Pricing Simulations/1-in-4.xlsx", sheet_name="LRPayouts(all sites)", index_col=0)
    data['Average'] = data.mean(axis=1)
    data = data * 100
    fig = px.bar(data['Average'], x=data.index, y=data['Average'], title='Average Payout for Long Rains (1 in 4)')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        title={'text': "Average Payout for Long Rains (1 in 4)", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(family="Times New Roman", size=18, color="RebeccaPurple")
    )
    st.plotly_chart(fig)

elif return_period == "1 in 4" and rainfall_type == "Short":
    data = pd.read_excel("C:/Users/PatrickMunyingi/Downloads/CREST Pricing Simulations/1-in-4.xlsx", sheet_name="SRPayouts(all sites)", index_col=0)
    data['Average'] = data.mean(axis=1)
    data = data * 100
    fig = px.bar(data['Average'], x=data.index, y=data['Average'], title='Average Payout for Short Rains (1 in 4)')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        title={'text': "Average Payout for Short Rains (1 in 4)", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(family="Times New Roman", size=18, color="RebeccaPurple")
    )
    st.plotly_chart(fig)

elif return_period == "1 in 8" and rainfall_type == "Both":
    data = pd.read_excel("C:/Users/PatrickMunyingi/Downloads/CREST Pricing Simulations/1-in-8.xlsx", sheet_name="AnnualPayouts(all sites)", index_col=0)
    data['Average'] = data.mean(axis=1)
    data = data * 100
    fig = px.bar(data['Average'], x=data.index, y=data['Average'], title='Average Payout for Both Rains (1 in 8)')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        title={'text': "Average Payout for Both Rains (1 in 8)", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(family="Times New Roman", size=18, color="RebeccaPurple")
    )
    st.plotly_chart(fig)

elif return_period == "1 in 8" and rainfall_type == "Long":
    data = pd.read_excel("C:/Users/PatrickMunyingi/Downloads/CREST Pricing Simulations/1-in-8.xlsx", sheet_name="LRPayouts(all sites)", index_col=0)
    data['Average'] = data.mean(axis=1)
    data = data * 100
    fig = px.bar(data['Average'], x=data.index, y=data['Average'], title='Average Payout for Long Rains (1 in 8)')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        title={'text': "Average Payout for Long Rains (1 in 8)", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(family="Times New Roman", size=18, color="RebeccaPurple")
    )
    st.plotly_chart(fig)

elif return_period == "1 in 8" and rainfall_type == "Short":
    data = pd.read_excel("C:/Users/PatrickMunyingi/Downloads/CREST Pricing Simulations/1-in-8.xlsx", sheet_name="SRPayouts(all sites)", index_col=0)
    data['Average'] = data.mean(axis=1)
    data = data * 100
    fig = px.bar(data['Average'], x=data.index, y=data['Average'], title='Average Payout for Short Rains (1 in 8)')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        title={'text': "Average Payout for Short Rains (1 in 8)", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(family="Times New Roman", size=18, color="RebeccaPurple")
    )
    st.plotly_chart(fig)

elif return_period == "1 in 10" and rainfall_type == "Both":
    data = pd.read_excel("C:/Users/PatrickMunyingi/Downloads/CREST Pricing Simulations/1-in-10.xlsx", sheet_name="AnnualPayouts(all sites)", index_col=0)
    data['Average'] = data.mean(axis=1)
    data = data * 100
    fig = px.bar(data['Average'], x=data.index, y=data['Average'], title='Average Payout for Both Rains (1 in 10)')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        title={'text': "Average Payout for Both Rains (1 in 10)", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(family="Times New Roman", size=18, color="RebeccaPurple")
    )
    st.plotly_chart(fig)

elif return_period == "1 in 10" and rainfall_type == "Long":
    data = pd.read_excel("C:/Users/PatrickMunyingi/Downloads/CREST Pricing Simulations/1-in-10.xlsx", sheet_name="LRPayouts(all sites)", index_col=0)
    data['Average'] = data.mean(axis=1)
    data = data * 100
    fig = px.bar(data['Average'], x=data.index, y=data['Average'], title='Average Payout for Long Rains (1 in 10)')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        title={'text': "Average Payout for Long Rains (1 in 10)", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(family="Times New Roman", size=18, color="RebeccaPurple")
    )
    st.plotly_chart(fig)

elif return_period == "1 in 10" and rainfall_type == "Short":
    data = pd.read_excel("C:/Users/PatrickMunyingi/Downloads/CREST Pricing Simulations/1-in-10.xlsx", sheet_name="SRPayouts(all sites)", index_col=0)
    data['Average'] = data.mean(axis=1)
    data = data * 100
    fig = px.bar(data['Average'], x=data.index, y=data['Average'], title='Average Payout for Short Rains (1 in 10)')
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        title={'text': "Average Payout for Short Rains (1 in 10)", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(family="Times New Roman", size=18, color="RebeccaPurple")
    )
    st.plotly_chart(fig)
