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

bar_category_options = list(filtered_df.columns)
default_bar_x = bar_category_options.index("Rental Market Survey zone") if "Rental Market Survey zone" in bar_category_options else 0

x_bar = st.selectbox(
    "Bar chart category",
    options=bar_category_options,
    index=default_bar_x,
    key="bar_x"
)

bar_y_options = [col for col in numeric_cols if col != x_bar]
if not bar_y_options:
    st.warning("No valid numeric columns available for the bar chart.")
    st.stop()

default_bar_y = bar_y_options.index("Percentage of renter households") if "Percentage of renter households" in bar_y_options else 0

y_bar = st.selectbox(
    "Bar chart numeric value",
    options=bar_y_options,
    index=default_bar_y,
    key="bar_y"
)

bar_data = filtered_df.groupby(x_bar, dropna=False)[y_bar].mean().reset_index()

fig1 = px.bar(bar_data, x=x_bar, y=y_bar, title=f"Average {y_bar} by {x_bar}")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("This chart compares the average value of the selected measure across categories.")

st.write("## Visualization 2: Line Chart")

line_x_options = list(filtered_df.columns)
default_line_x = line_x_options.index("Year") if "Year" in line_x_options else 0

x_line = st.selectbox(
    "Line chart x-axis",
    options=line_x_options,
    index=default_line_x,
    key="line_x"
)

line_y_options = [col for col in numeric_cols if col != x_line]
if not line_y_options:
    st.warning("No valid numeric columns available for the line chart.")
    st.stop()

default_line_y = line_y_options.index("Percentage of renter households") if "Percentage of renter households" in line_y_options else 0

y_line = st.selectbox(
    "Line chart y-axis",
    options=line_y_options,
    index=default_line_y,
    key="line_y"
) 

line_data = filtered_df.groupby(x_line, dropna=False)[y_line].mean().reset_index()

fig2 = px.line(line_data, x=x_line, y=y_line, markers=True, title=f"{y_line} across {x_line}")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("This chart shows how the selected numeric measure changes across the chosen dimension.")

if len(numeric_cols) >= 2:
    st.write("## Visualization 3: Scatter Plot")

    scatter_x_options = numeric_cols
    default_scatter_x = scatter_x_options.index("Population") if "Population" in scatter_x_options else 0

    x_scatter = st.selectbox(
        "Scatter plot x-axis",
        options=scatter_x_options,
        index=default_scatter_x,
        key="scatter_x"
    )

    scatter_y_options = [col for col in numeric_cols if col != x_scatter]
    default_scatter_y = scatter_y_options.index("Primary market vacancy rate") if "Primary market vacancy rate" in scatter_y_options else 0

    y_scatter = st.selectbox(
        "Scatter plot y-axis",
        options=scatter_y_options,
        index=default_scatter_y,
        key="scatter_y"
    )

    color_options = ["None"] + categorical_cols
    default_color = color_options.index("Rental Market Survey zone") if "Rental Market Survey zone" in color_options else 0

    color_col = st.selectbox(
        "Optional color grouping",
        options=color_options,
        index=default_color,
        key="scatter_color"
    )

    if color_col == "None":
        fig3 = px.scatter(
            filtered_df,
            x=x_scatter,
            y=y_scatter,
            title=f"{y_scatter} vs {x_scatter}"
        )
    else:
        fig3 = px.scatter(
            filtered_df,
            x=x_scatter,
            y=y_scatter,
            color=color_col,
            title=f"{y_scatter} vs {x_scatter}"
        )

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
