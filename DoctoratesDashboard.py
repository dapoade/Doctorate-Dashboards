import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# @st.cache

df_codes = pd.read_csv('https://raw.githubusercontent.com/dapoade/Doctorate-Dashboards/main/DoctoratesbyStateandDegree.csv')


st.markdown(""" # Doctorates Dashboard

### Data

The original data contains the total numbers doctorates granted broken down by institutions and fields of study. However, institution-level data is too granular to visualize in a choropleth map.
As a result, I decided to visualize the state-level statistics as the base of analysis. The fields of study are broken down into All Fields, Life Sciences, Physical Sciences and Earth Sciences, Mathematics and Computer Sciences,
Psychology and Scoail Sciences and Engineering.

#### Below is a dashboard of number of  **Doctorates** by **State** for each **type of degree**. \

""")


for col in df_codes.columns:
    df_codes[col] = df_codes[col].astype(str)





selected_field = st.sidebar.selectbox("Field:", list(df_codes.iloc[:,1:7].columns))

# df_codes['text'] = ("State:" + df_codes['State'] + '<br>' + \
#  "{} Doctorates".format(str(selected_field)) + df_codes.loc[df_codes.State, df_codes[str(selected_field)]])

st.write("""

As mentioned in the blog posts, the purpose of these dashboards are to further highlight the popularity of specific types of Doctorate degrees.
There is a filter on the left that allows you to choose the Field of Study of interest. Additionally, you can click on the lasso or box to
zoom in on the plot for an easier viewing experience.


""")

fig = go.Figure(data=go.Choropleth(
    locations= df_codes['code'], # Spatial coordinates
    z = df_codes[str(selected_field)], # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    autocolorscale = False,
    colorscale = 'Reds',
    text=df_codes['State'], # hover text
    colorbar_title = "Number of Doctorates",
))

fig.update_layout(
    title_text = 'Map of Doctorates by State',
    geo_scope='usa', # limite map scope to USA
)

st.plotly_chart(fig, use_container_width = True)


fig1 = go.Figure(go.Bar(
            y=(df_codes[str(selected_field)].astype(float)),
            x= df_codes['State'],
            marker_color = 'indianred'))
fig1.update_layout(xaxis_tickangle=-90, title_text = "Number of Doctorates by State")

st.plotly_chart(fig1, use_container_width = True)
