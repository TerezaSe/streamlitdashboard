import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import plotly.graph_objects as go
import plotly.express as px



##################
#data
##################
engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")
df_bikes = pd.read_sql(sql='select * from edinburgh_bikes', con=engine)


##################
#vizualizace
##################


st.title('Moje prvni appka')

st.write('Toto je moje prvni aplikace, kterou delam')

page = st.sidebar.radio('Select page',['Test','Thompson'])
if page == 'Mapa':
    st.write('Mapa používání sdílených dat v Edinbourgu')
    fig = px.scatter_mapbox(df_temp,lat='start_station_latitude', lon='start_station_longitude')
    fig.update_layout(mapbox_style="open-street-map")
    fig.show()

if page == 'Thompson':
    st.write('Thompson sampling')
