import numpy as np
import pandas as pd
import streamlit as st
import geopandas
import matplotlib.pyplot as plt


st.title('JobSeeker in Australia')

def plot_map(df,title):
    #gdf.plot(ax=ax, color='red')
    max_v=df['JobSeeker Payment'].max()
    #title="Heat Map of Job Seeker Payment may 2020"
    fig, ax = plt.subplots(1, figsize=(40, 20))
    ax.axis('off')
    ax.set_title(title, fontdict={'fontsize': '40', 'fontweight' : '3'})
    color = 'Oranges'
    vmin, vmax = 0, 231
    sm = plt.cm.ScalarMappable(cmap=color, norm=plt.Normalize(vmin=0, vmax=max_v))
    sm._A = []
    cbar = fig.colorbar(sm)
    cbar.ax.tick_params(labelsize=20)
    if len(df)>0:
        df.plot('JobSeeker Payment', cmap=color, linewidth=0.8, ax=ax, edgecolor='0.8', figsize=(40,20))


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

 
aus_lgas = geopandas.read_file('Data/LGA_2019_AUST.shp')
aus_lgas.rename(columns={"LGA_CODE19":"LGA_CODE"},inplace=True)
aus_lgas.LGA_CODE=aus_lgas.LGA_CODE.astype(float)

df_jobseeker_count=pd.read_excel("Data/jobseeker-payment-and-youth-allowance-recipients-monthly-profile-may-2020.xlsx",sheet_name="Table 4 - By SA2",header=6)
df_jobseeker_count["SA2"]=df_jobseeker_count["SA2"].astype(str)
df_jobseeker_count=df_jobseeker_count[:2293]
df_jobseeker_count['JobSeeker Payment']=np.where(df_jobseeker_count['JobSeeker Payment']=="<5","5",df_jobseeker_count['JobSeeker Payment'])
df_jobseeker_count['JobSeeker Payment']=np.where(df_jobseeker_count['JobSeeker Payment']=="","0",df_jobseeker_count['JobSeeker Payment'])

df_jobseeker_count['JobSeeker Payment']=df_jobseeker_count['JobSeeker Payment'].astype(int)
df_jobseeker_count["JobSeeker Payment"]=df_jobseeker_count["JobSeeker Payment"].fillna(0)
aus_sa2 = geopandas.read_file('Data/SA2_2016_AUST.shp')
print(type(aus_sa2.SA2_5DIG16[0]))
print(type(df_jobseeker_count.SA2[0]))
df_jobseeker_count=aus_sa2.merge(df_jobseeker_count,right_on='SA2',left_on="SA2_5DIG16",how="left")

#df_jobseeker_count["coords"] = np.where(df_jobseeker_count.geometry.isnull(),(0,0), 
 #list(df_jobseeker_count.geometry.centroid.coords)[0])
 
df_jobseeker_count["coords"]=df_jobseeker_count.geometry
 
df_jobseeker_count["coords"].apply(lambda x: (x.centroid.coords.xy[0][0],x.centroid.coords.xy[1][0]) if x is not None else (0,0))
df = pd.DataFrame(
    {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
df=pd.DataFrame([])

df_postcode= pd.read_csv('Data/suburbs.csv',sep=",")
df_postcode[['value1','value2']]=df_postcode["local_goverment_area"].str.split('(',expand=True)
df_postcode['value1']=df_postcode['value1'].str.strip()
#df_postcode.rename(columns={"lat":"Latitude","lng":"Longitude"},inplace=True)
gdf = geopandas.GeoDataFrame(
    df_postcode, geometry=geopandas.points_from_xy(df_postcode.lng, df_postcode.lat))
st.write(gdf.head())

plot_map(df_jobseeker_count,"Heat Map of Job Seeker Payment may 2020 Australia")
st.pyplot(legend=True)
# Create a list of possible values and multiselect menu with them in it.
state = df_jobseeker_count.STE_NAME16.unique()
state_SELECTED = st.multiselect('Select State', state)

mask_state = df_jobseeker_count['STE_NAME16'].isin(state_SELECTED)
data = df_jobseeker_count[mask_state]

if len(data)>0:
    SA2s = data.SA4_NAME16.unique()
    SA2_SELECTED = st.multiselect('Select SA2', SA2s)

    # Mask to filter dataframe
    mask_sa2 = data['SA4_NAME16'].isin(SA2_SELECTED)

    data = data[mask_sa2]
plot_map(data,"Heat Map of Job Seeker Payment may 2020 SA2")
#hour_to_filter = st.slider('Count',5, int(np.max(df_jobseeker_count["JobSeeker Payment"])), 10)

#filtered_data = df_jobseeker_count[df_jobseeker_count["JobSeeker Payment"] == hour_to_filter]
#world = geopandas.read_file(geopandas.datasets.get_path('naturalesarth_lowres'))
# =============================================================================
# ax = world[world.continent == 'South America'].plot(
#     color='white', edgecolor='black')
# =============================================================================

#ax = df_jobseeker_count.plot(
#   colormap='jet', edgecolor='black',column='JobSeeker Payment')

#.legend(loc='center left',bbox_to_anchor=(1.0, 0.5))
#ax.legend(scatterpoints=1, frameon=False, labelspacing=1, title='JobSeeker Payment Count')



#for idx, row in data.iterrows():
 #   plt.annotate(s=row['SA3_NAME16'], xy=row['coords'],
  #               horizontalalignment='center')
#plt.show()
st.pyplot(legend=True)

