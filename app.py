import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Drought Detection in Kenya Based on the different Return Periods")
#st.write("Visualize Drought detection capabilities of the model based on return periods and rainfall types")
# NDMA Drought Table
ndma_data = {
    "Period": ["2005-2006", "2008-2011", "2016-2017", "2017-2018", "2020-2022"],
    "Disaster Declarations": ["", "Yes", "Yes", "", "Yes"],
    "ReliefWeb": ["", "Yes", "Yes", "", "Yes"]
}
ndma_table = pd.DataFrame(ndma_data)
ndma_table.set_index("Period", inplace=True)
# Display NDMA Table
st.subheader("Drought Table")
st.write(ndma_table)


# File paths for return periods (relative paths)
file_paths = {
    "1 in 4": "1-in-4.xlsx",
    "1 in 8": "1-in-8.xlsx",
    "1 in 10": "1-in-10.xlsx"
}

# Sheet mapping for rainfall types
sheet_mapping = {
    "Both": "AnnualPayouts(all sites)",
    "Long": "LRPayouts(all sites)",
    "Short": "SRPayouts(all sites)"
}

# List of counties
counties = ["GARISSA", "TANA RIVER"]

# Streamlit Title and Description
st.title("Drought Detection Visualization in Kenya Based on the Different Return Periods")
st.write("Visualize Drought detection capabilities of the model based on return periods and rainfall types.")

# User Input
return_period = st.selectbox("Select Return Period", options=["1 in 4", "1 in 8", "1 in 10"])
rainfall_type = st.selectbox("Select Rainfall Type", options=["Both", "Long", "Short"])

def load_and_preprocess_data(file_path, sheet_name):
    """
    Load data from an Excel file and preprocess it by grouping columns into counties.
    """
    # Load data
    data = pd.read_excel(file_path, sheet_name=sheet_name, index_col=0)

    # Group data by counties
    grouped_data = pd.DataFrame(index=data.index)
    for county in counties:
        county_columns = [col for col in data.columns if county in col.upper()]
        if county_columns:
            grouped_data[county] = data[county_columns].mean(axis=1)

    # Add an "Average" column for all sites
    grouped_data["Average"] = grouped_data.mean(axis=1)
    grouped_data *= 100  # Scale to percentage
    return grouped_data

def create_plot(data, column, title):
    """
    Create a bar plot for the selected data column.
    """
    fig = px.bar(
        data,
        x=data.index,
        y=column,
        title=title
    )
    # Customize the plot layout
    fig.update_layout(
        xaxis=dict(
            tickmode="linear",
            tick0=0,
            dtick=1
        ),
        title=dict(
            text=title,
            x=0.5,
            xanchor="center"
        ),
        xaxis_title="Years",
        yaxis_title="Burn Rate (%)",
        autosize=False,
        width=900,
        height=600,
        font=dict(
            family="Times New Roman",
            size=18,
            color="RebeccaPurple"
        )
    )
    return fig

# Load data based on user selection
file_path = file_paths[return_period]
sheet_name = sheet_mapping[rainfall_type]
data = load_and_preprocess_data(file_path, sheet_name)

# User selects visualization type
visualization_type = st.selectbox("Select Visualization", options=["Overall Average", *counties])

# Plot based on selection
if visualization_type == "Overall Average":
    st.plotly_chart(create_plot(data, "Average", f"Average Payout for {rainfall_type} Rains ({return_period})"))
else:
    st.plotly_chart(create_plot(data, visualization_type, f"{visualization_type} Payout for {rainfall_type} Rains ({return_period}) - {visualization_type}"))
