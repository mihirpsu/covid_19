# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:11:51 2020

@author: Mihir Mehta
"""

import folium

def gen_map(data_penn,high_res_county_geo):
    # map generation
    #initiate US MAP
    map_1 =  folium.Map(location=[47, -102], zoom_start=7,no_touch=False)
    
    #add probability score color gradient
    # Add choropleth layer
    map_1.choropleth(
     geo_data=high_res_county_geo,
     name='choropleth',
     data=data_penn,
     columns=["GEOID","one_prb"],
     key_on='properties.GEO_ID',
     fill_color='YlOrRd',
     fill_opacity=0.7,
     line_opacity=1,
     sdafdsa=True
    )
    
    #add each county to the map
    for i in range(0,data_penn.shape[0]):
        tooltip=data_penn.iloc[i,2]
        #print(tooltip)
        #folium.Marker
        popup_html = """ 
        <b>{cntd} {St}</b><br>
        <b>Population Density:</b> {ppd}<br>
        <b>Number of Cases as of Date:</b> {cc}<br>
        <b>Diabetes Percentage:</b> {dp}%<br>
        <b>Hypertension Percentage:</b> {htp}%<br>
        <b>70+ Pop Percentage:</b> {ap}%<br>
        <b>Cancer Crude Rate:</b> {cp}<br>
        <b>CRD Crude Rate:</b> {crd}<br>
        <b>Susceptibility Index :</b> {prb}<br>
        <b>Vulnerability Index:</b> {exm}<br>
        <b>Population :</b> {pp}<br>
        """.format(cntd=data_penn.iloc[i,2],ppd="%.2f" % round(data_penn.loc[i,"pop_den_permile"],2),\
                  cc="%.2f" % round(data_penn.loc[i,"Confirmed"],2),\
                                    dp="%.2f" % round(data_penn.loc[i,"diab_perc"],2),\
                  htp="%.2f" % round(data_penn.loc[i,"hyper_perc"],2),ap="%.2f" % round(data_penn.loc[i,"old_perc"],2),\
                    cp = "%.2f" % round(data_penn.loc[i,"CRUDE_RATE"],2), crd = "%.2f" % round(data_penn.loc[i,"CRD_MR"],2),\
                  pp=f'{data_penn.loc[2,"TOT_POP"]:,}' , St =data_penn.iloc[i,1],\
                  prb=data_penn.loc[i,"RankPEf"]
                   ,\
                  exm= data_penn.loc[i,"RankPEf"])
        iframe = folium.IFrame(html=popup_html, width=320, height=240)
        popup1 = folium.Popup(iframe, max_width=2650)
        if data_penn.loc[i,"Confirmed"] >0:
                color= "red"
        else:
                color = "green"
        folium.CircleMarker([data_penn.loc[i,"Latitude"], data_penn.loc[i,"Longitude"]]
                      , popup=popup1, tooltip=tooltip, radius=1, color=color).add_to(map_1)
    return(map_1)
    
    #save the map
    