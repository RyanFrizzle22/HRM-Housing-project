import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Housing Decision Support Dashboard", layout="wide")

st.title("Housing Decision Support Dashboard")
st.markdown("""
This dashboard helps a decision-maker explore housing-related data and identify patterns
that may support planning and policy decisions.
""")

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

csv_files = list(DATA_DIR.glob("*.csv"))

if not csv_files:
    st.error("No CSV files were found in the data folder.")
    st.stop()

selected_file = st.sidebar.selectbox(
    "Choose a dataset",
    options=[f.name for f in csv_files]
)

file_path = DATA_DIR / selected_file
df = pd.read_csv(file_path)

st.sidebar.header("Filters")

st.write("### Dataset Preview")
st.dataframe(df.head())

numeric_cols = df.select_dtypes(include="number").columns.tolist()
categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

if len(numeric_cols) < 1:
    st.warning("This dataset does not have enough numeric columns for charts.")
    st.stop()

filter_col = None
if categorical_cols:
    filter_col = st.sidebar.selectbox("Choose a category column to filter", ["None"] + categorical_cols)

filtered_df = df.copy()

if filter_col and filter_col != "None":
    filter_values = st.sidebar.multiselect(
        f"Select values from {filter_col}",
        options=sorted(df[filter_col].dropna().astype(str).unique()),
        default=sorted(df[filter_col].dropna().astype(str).unique())
    )
    filtered_df = filtered_df[filtered_df[filter_col].astype(str).isin(filter_values)]

st.write("## Visualization 1: Bar Chart")

x_bar = st.selectbox("Bar chart category", options=filtered_df.columns, key="bar_x")

bar_y_options = [col for col in numeric_cols if col != x_bar]
if not bar_y_options:
    st.warning("No valid numeric columns available for the bar chart.")
    st.stop()

y_bar = st.selectbox("Bar chart numeric value", options=bar_y_options, key="bar_y")

bar_data = filtered_df.groupby(x_bar, dropna=False)[y_bar].mean().reset_index()

fig1 = px.bar(bar_data, x=x_bar, y=y_bar, title=f"Average {y_bar} by {x_bar}")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("This chart compares the average value of the selected measure across categories.")

st.write("## Visualization 2: Line Chart")

x_line = st.selectbox("Line chart x-axis", options=filtered_df.columns, key="line_x")

line_y_options = [col for col in numeric_cols if col != x_line]
if not line_y_options:
    st.warning("No valid numeric columns available for the line chart.")
    st.stop()

y_line = st.selectbox("Line chart y-axis", options=line_y_options, key="line_y")

line_data = filtered_df.groupby(x_line, dropna=False)[y_line].mean().reset_index()

fig2 = px.line(line_data, x=x_line, y=y_line, markers=True, title=f"{y_line} across {x_line}")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("This chart shows how the selected numeric measure changes across the chosen dimension.")

if len(numeric_cols) >= 2:
    st.write("## Visualization 3: Scatter Plot")

    x_scatter = st.selectbox("Scatter plot x-axis", options=numeric_cols, key="scatter_x")
    y_scatter = st.selectbox(
        "Scatter plot y-axis",
        options=[col for col in numeric_cols if col != x_scatter],
        key="scatter_y"
    )

    color_col = st.selectbox(
        "Optional color grouping",
        options=["None"] + categorical_cols,
        key="scatter_color"
    )

    if color_col == "None":
        fig3 = px.scatter(filtered_df, x=x_scatter, y=y_scatter, title=f"{y_scatter} vs {x_scatter}")
    else:
        fig3 = px.scatter(filtered_df, x=x_scatter, y=y_scatter, color=color_col, title=f"{y_scatter} vs {x_scatter}")

    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("This chart helps show whether two numeric variables appear to move together.")
else:
    st.info("A scatter plot requires at least two numeric columns.")

st.write("## Decision Support Summary")
st.markdown("""
Use the filters and visualizations to compare patterns across datasets and categories.
The dashboard is meant to help identify where housing pressures, trends, or relationships
may justify further policy attention or intervention.
""")
