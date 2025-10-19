import hvplot.pandas
import pandas as pd
import panel as pn
from dataset import dataset
from sklearn.preprocessing import StandardScaler

pn.extension("tabulator", raw_css=["""
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

body, .bk, .bk-root, .markdown, h1, h2, h3, h4, h5, h6, p, span, div, label, input, select, button {
    font-family: 'Poppins', sans-serif !important;
}
"""])

ACCENT = "teal"

styles = {
    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px",
    "border-radius": "8px",
    "padding": "16px",
    "flex": "1",
}

# Extract Data
source_data = dataset.copy()

# Transform Data
min_year = int(source_data["model_year"].min())
max_year = int(source_data["model_year"].max())
origins = {0: "All", 1: "USA", 2: "Europe", 3: "Japan"}
source_data["origin_name"] = source_data["origin"].map({1: "USA", 2: "Europe", 3: "Japan"})

def filter_data(origin, min_year_filter, max_year_filter, min_cylinders, max_cylinders):
    if origin == 0:  # All origins
        data = source_data[
            (source_data.model_year >= min_year_filter) &
            (source_data.model_year <= max_year_filter) &
            (source_data.cylinders >= min_cylinders) &
            (source_data.cylinders <= max_cylinders)
        ]
    else:
        data = source_data[
            (source_data.origin == origin) & 
            (source_data.model_year >= min_year_filter) &
            (source_data.model_year <= max_year_filter) &
            (source_data.cylinders >= min_cylinders) &
            (source_data.cylinders <= max_cylinders)
        ]
    return data

# Filters
origin_select = pn.widgets.Select(
    name="Origin",
    value=0,
    options={v: k for k, v in origins.items()},
    description="Country of origin",
    styles={"margin-block" : "16px"}
)

year_range = pn.widgets.RangeSlider(
    name="Model Year Range",
    start=min_year,
    end=max_year,
    value=(min_year, max_year),
    styles={"margin-block" : "16px"}
)

cylinders_range = pn.widgets.RangeSlider(
    name="Cylinders Range",
    start=int(source_data["cylinders"].min()),
    end=int(source_data["cylinders"].max()),
    value=(int(source_data["cylinders"].min()), int(source_data["cylinders"].max())),
    styles={"margin-block" : "16px"}
)

# Transform Data 2
df = pn.rx(filter_data)(
    origin=origin_select, 
    min_year_filter=year_range.param.value_start,
    max_year_filter=year_range.param.value_end,
    min_cylinders=cylinders_range.param.value_start,
    max_cylinders=cylinders_range.param.value_end
)

count = df.rx.len()
avg_mpg = df.mpg.mean()
avg_horsepower = df.horsepower.mean()
avg_weight = df.weight.mean()

# Plot Data
# 1. Distribusi nilai MPG pada seluruh mobil
mpg_hist = df.hvplot.hist(
    y='mpg', 
    bins=20,
    title='MPG Distribution',
    xlabel='MPG',
    ylabel='Frequency',
    color=ACCENT,
)

# 2. Perbedaan rata-rata MPG berdasarkan cylinders
mpg_by_cyl = (
    df.groupby('cylinders')['mpg'].mean().reset_index()
).hvplot.bar(
    x='cylinders',
    y='mpg',
    title='Average MPG by Cylinders',
    xlabel='Number of Cylinders',
    ylabel='Average MPG',
    color=ACCENT,
    rot=0
)

# 3. Hubungan antara weight dan MPG
mpg_by_weight = df.hvplot.scatter(
    x='weight',
    y='mpg',
    title='Weight vs MPG',
    xlabel='Weight (lbs)',
    ylabel='MPG',
    color=ACCENT,
    cmap='viridis',
    size=50,
    alpha=0.6
)

# 4. Tren rata-rata MPG dari tahun ke tahun
mpg_by_year = (
    df.groupby('model_year')['mpg'].mean().reset_index()
).hvplot.line(
    x='model_year',
    y='mpg',
    title='Average MPG per Year',
    xlabel='Year',
    ylabel='Average MPG',
    color=ACCENT,
    line_width=3,
    marker='o',
    markersize=8
)

# Display Data
indicators = pn.FlexBox(
    pn.indicators.Number(
        value=count, 
        name="Total Cars", 
        format="{value:,.0f}", 
        styles=styles,
        title_size="14pt",
        font_size="42pt"
    ),
    pn.indicators.Number(
        value=avg_mpg,
        name="Avg. MPG",
        format="{value:,.1f}",
        styles=styles,
        title_size="14pt",
        font_size="42pt"
    ),
    pn.indicators.Number(
        value=avg_horsepower,
        name="Avg. Horsepower",
        format="{value:,.1f}",
        styles=styles,
        title_size="14pt",
        font_size="42pt"
    ),
    pn.indicators.Number(
        value=avg_weight,
        name="Avg. Weight (lbs)",
        format="{value:,.0f}",
        styles=styles,
        title_size="14pt",
        font_size="42pt"
    ),
)

plot1 = pn.pane.HoloViews(mpg_hist, sizing_mode="stretch_both", name="MPG Distribution")
plot2 = pn.pane.HoloViews(mpg_by_cyl, sizing_mode="stretch_both", name="Avg MPG by Cylinders")
plot3 = pn.pane.HoloViews(mpg_by_weight, sizing_mode="stretch_both", name="MPG vs Weight")
plot4 = pn.pane.HoloViews(mpg_by_year, sizing_mode="stretch_both", name="Avg MPG per Year")
table = pn.widgets.Tabulator(
    df, 
    sizing_mode="stretch_both", 
    name="Data Table",
    page_size=15
)

# Layout Data
tabs = pn.Tabs(
    plot1, plot2, plot3, plot4, table, 
    styles=styles, 
    sizing_mode="stretch_width", 
    height=500, 
    margin=10
)

# Info section
info_text = f"""
## Auto MPG Dataset

This dashboard visualizes the Auto MPG dataset from UCI Machine Learning Repository.

**Dataset Info:**
- Total records: {len(source_data)}
- Years: {min_year} - {max_year}
- Features: displacement, cylinders, horsepower, weight, acceleration, model_year, origin
- Target: mpg (miles per gallon)

**Filters:**
- Select origin (All, USA, Europe, or Japan)
- Adjust year range
- Adjust cylinders range
"""

info_pane = pn.pane.Markdown(info_text, styles=styles)

pn.template.FastListTemplate(
    title="Auto MPG Dashboard",
    sidebar=[info_pane, origin_select, year_range, cylinders_range],
    main=[pn.Column(indicators, tabs, sizing_mode="stretch_both")],
    main_layout=None,
    accent=ACCENT,
).servable()