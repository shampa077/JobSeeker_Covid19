import numpy as np
import pandas as pd
import streamlit as st
import geopandas

st.title('JobSeeker in Australia')

# @st.cache
# def load_data():
#     aus_lgas = pd.read_excel('Data/AUS_LGA.xlsx')
#     aus_lgas.rename(columns={"LGA_CODE19":"LGA_CODE"},inplace=True)
#     aus_lgas.LGA_CODE=aus_lgas.LGA_CODE.astype(float)

#     xls = pd.ExcelFile('Data/may_data_use.xlsx')

#     sheets= ['JSCI demographics - LGA',
#     'DLA demographics - LGA',
#     'Q1 education - LGA',
#     'Q2 mostly doing- LGA',
#     'Q3 hours worked - LGA',
#     'Q4 English - LGA',
#     'Q5 transport - LGA',
#     'DLA Q6 internet - LGA']
#     dfs_social=pd.DataFrame([])
#     for each in sheets:
#         df=pd.read_excel(xls, each,header=2)
#         collist=[df.columns[0],df.columns[1]]+[each+"_"+ df.columns[i] for i in range(2,len(df.columns))]
#         print(collist)
#         df.columns=collist
#         if len(dfs_social)==0:
#             dfs_social=df
#         else:
#             dfs_social=dfs_social.merge(df,on=['LGA_NAME','LGA_CODE'],how="left")
#         print(df)
#     dfs_social=dfs_social.merge(aus_lgas,on="LGA_CODE",how="left")

#     df_postcode= pd.read_csv('Data/suburbs.csv',sep=",")
#     df_postcode[['value1','value2']]=df_postcode["local_goverment_area"].str.split('(',expand=True)
#     df_postcode['value1']=df_postcode['value1'].str.strip()

#     df_jobseeker_count=pd.read_excel("Data/jobseeker-payment-and-youth-allowance-recipients-monthly-profile-may-2020.xlsx",sheet_name="Table 4 - By SA2",header=6)
#     #df_jobseeker_count["SA2"]=df_jobseeker_count["SA2"].astype(str)
#     df_jobseeker_count=df_jobseeker_count[:2293]
#     df_jobseeker_count['JobSeeker Payment']=np.where(df_jobseeker_count['JobSeeker Payment']=="<5",0,df_jobseeker_count['JobSeeker Payment'])

#     aus_sa2 = pd.read_excel('Data/AUS_SA2.xlsx')
#     print(type(aus_sa2.SA2_5DIG16[0]))
#     print(type(df_jobseeker_count.SA2[0]))
#     df_jobseeker_count=aus_sa2.merge(df_jobseeker_count,right_on='SA2',left_on="SA2_5DIG16",how="left")
#     return df_jobseeker_count

# data_load_state = st.text('Loading data...')
# data = load_data()
# data_load_state.text("Done! (using st.cache)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# # Some number in the range 0-23
# number_to_filter = st.slider('Count', min(data['JobSeeker Payment']), 50, max(data['JobSeeker Payment']))
# filtered_data = data[data['JobSeeker Payment'] <=number_to_filter]

# st.subheader('Map of locations where number of application less than equal to %s' % number_to_filter)
# st.map(filtered_data)


df = pd.DataFrame(
    {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
st.write(gdf.head())
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = world[world.continent == 'South America'].plot(
    color='white', edgecolor='black')
gdf.plot(ax=ax, color='red')
st.pyplot()