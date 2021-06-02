# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:47:40 2021

@author: varma
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import math


pickle_in = open("best_model.pkl","rb")
model=pickle.load(pickle_in)



Mean_encoded_Income={90003: 100885.0,
 90004: 68555.01999999999,
 90006: 48859.675,
 90008: 115060.87,
 90012: 63786.8,
 90019: 45909.16,
 90022: 94156.55,
 90025: 154011.2,
 90032: 68103.7,
 90034: 112655.73,
 90035: 44191.55,
 90039: 121328.92,
 90042: 71952.75,
 90043: 73395.0,
 90044: 119775.95,
 90045: 88504.36,
 90047: 62684.848,
 90048: 68014.91,
 90049: 23933.54,
 90056: 146926.6,
 90059: 188652.92,
 90061: 85786.95,
 90064: 126758.05500000001,
 90065: 95731.35,
 90066: 114742.73,
 90069: 82783.43,
 90077: 108352.46333333333,
 90201: 150536.28000000003,
 90210: 63404.753333333334,
 90212: 87222.2,
 90220: 87915.71333333333,
 90221: 163986.525,
 90222: 89866.85,
 90230: 117729.0,
 90240: 84356.17,
 90241: 170692.77666666667,
 90242: 52592.07,
 90245: 46262.015,
 90247: 130172.56,
 90248: 76824.0,
 90249: 152346.75,
 90250: 61736.265,
 90254: 37626.0,
 90260: 84925.7,
 90262: 132956.96,
 90265: 48809.52666666667,
 90266: 117841.51666666668,
 90272: 85371.0,
 90274: 90081.715,
 90275: 127788.53399999999,
 90277: 200087.94999999998,
 90280: 116983.0,
 90291: 129378.3,
 90301: 232.0,
 90303: 124675.4,
 90304: 36992.0,
 90402: 69504.6,
 90403: 53960.72,
 90404: 116546.68,
 90501: 93207.366,
 90502: 179893.97,
 90503: 143858.6133333333,
 90504: 102857.38,
 90505: 128854.58,
 90601: 135180.4925,
 90602: 85502.275,
 90603: 49147.299999999996,
 90604: 86500.37999999999,
 90606: 143133.13,
 90620: 97977.31800000001,
 90630: 98122.36666666665,
 90631: 52611.7825,
 90638: 83223.62400000001,
 90640: 35357.215,
 90650: 103036.02714285713,
 90660: 121130.75,
 90670: 54304.5325,
 90680: 75538.685,
 90701: 46523.625,
 90703: 139806.86000000002,
 90706: 153497.855,
 90710: 24089.0,
 90712: 89852.08333333333,
 90713: 124167.325,
 90717: 81814.62,
 90720: 140404.4,
 90731: 134728.70500000002,
 90732: 107703.49,
 90742: 197808.55,
 90744: 153092.19,
 90745: 62354.41750000001,
 90746: 98549.6725,
 90755: 2925.69,
 90806: 144198.88333333333,
 90807: 89959.2025,
 90808: 88584.235,
 90813: 69446.82500000001,
 90814: 25646.075,
 90815: 89353.29999999999,
 91001: 46719.49,
 91011: 155660.35,
 91016: 177199.56,
 91024: 121160.155,
 91104: 82920.44,
 91107: 199708.63,
 91208: 32189.375,
 91214: 77758.985,
 91306: 97841.38333333335,
 91307: 89078.675,
 91311: 101839.73,
 91324: 154596.71,
 91326: 156128.7,
 91331: 67090.81,
 91335: 76938.2,
 91343: 49708.0,
 91345: 210099.11,
 91352: 108119.47333333334,
 91355: 31645.96,
 91364: 58521.833333333336,
 91367: 77927.2,
 91405: 124470.87,
 91406: 84750.51,
 91436: 100081.2,
 91504: 69977.7,
 91505: 58053.0,
 91605: 114714.14,
 91702: 151067.03999999998,
 91706: 45289.92,
 91711: 201498.9,
 91722: 53966.700000000004,
 91724: 135834.12,
 91733: 84259.98,
 91741: 72828.83333333333,
 91744: 160116.3,
 91745: 88162.9625,
 91746: 126763.84,
 91748: 55960.795,
 91750: 32614.27,
 91752: 103524.985,
 91765: 96404.02,
 91766: 165622.06,
 91767: 78275.02666666667,
 91768: 100928.46,
 91773: 117751.69,
 91775: 138051.26,
 91776: 103213.11,
 91780: 76377.29000000001,
 91789: 141749.98285714287,
 91791: 100515.06999999999,
 91792: 23922.8,
 91801: 86670.09,
 91803: 53121.83,
 92201: 112823.17777777779,
 92203: 101549.87,
 92210: 159452.8,
 92211: 108317.20714285715,
 92220: 58025.48571428571,
 92223: 127163.45,
 92234: 67180.3625,
 92240: 57375.97,
 92253: 88148.644,
 92260: 107671.36333333333,
 92262: 88619.04333333332,
 92264: 110080.59199999999,
 92270: 81523.00333333331,
 92501: 109314.57999999999,
 92503: 115105.0090909091,
 92504: 115400.58499999999,
 92505: 93812.26250000001,
 92506: 101086.865,
 92507: 94920.72333333334,
 92508: 128111.1,
 92509: 37153.6875,
 92543: 77355.7,
 92544: 89649.59,
 92553: 124664.40333333334,
 92555: 133481.53,
 92557: 89436.43000000001,
 92562: 79825.61666666667,
 92563: 69443.98666666666,
 92571: 122425.53,
 92582: 116589.4,
 92583: 25675.3,
 92584: 122526.23000000001,
 92585: 208299.35,
 92587: 96350.74500000001,
 92592: 100529.05333333334,
 92595: 3616.0,
 92596: 41483.776666666665,
 92602: 23112.77,
 92604: 35908.86,
 92606: 110329.465,
 92610: 27402.3,
 92612: 223768.01,
 92614: 131203.91,
 92617: 21468.73,
 92618: 231630.0,
 92620: 130349.98599999999,
 92625: 92705.0,
 92626: 106125.24,
 92627: 67202.43666666666,
 92630: 81045.42666666667,
 92646: 38701.67,
 92647: 85110.426,
 92648: 75863.23,
 92649: 98489.9475,
 92651: 75947.88500000001,
 92653: 108805.40666666666,
 92656: 61808.2,
 92660: 75897.43250000001,
 92661: 1252.0,
 92662: 30655.99,
 92663: 81222.905,
 92672: 144461.57,
 92675: 106669.07,
 92676: 123196.2,
 92677: 74553.18250000001,
 92679: 96242.04000000001,
 92683: 85174.56857142858,
 92688: 100575.87,
 92691: 177548.2,
 92692: 50051.545,
 92694: 48126.7,
 92701: 63052.3,
 92703: 144841.46,
 92704: 124811.25999999998,
 92705: 133995.7157142857,
 92706: 91254.43,
 92707: 141749.03,
 92708: 182951.41999999998,
 92780: 100518.1175,
 92782: 144100.35,
 92801: 98239.85444444444,
 92802: 121725.0175,
 92804: 117516.5988888889,
 92805: 98997.962,
 92806: 83657.16,
 92807: 86692.76333333334,
 92808: 98340.03363636365,
 92821: 156587.33333333334,
 92823: 221180.07,
 92831: 100522.57,
 92833: 83596.94666666667,
 92835: 50248.456000000006,
 92840: 57169.658333333326,
 92841: 67063.4,
 92844: 91355.7,
 92860: 78196.4,
 92861: 83629.15,
 92865: 52250.45,
 92867: 98986.32375000001,
 92869: 106350.53166666668,
 92870: 55669.32666666667,
 92879: 47297.75,
 92880: 60198.704999999994,
 92881: 66516.5,
 92882: 146340.27,
 92883: 135793.1,
 92886: 60186.03875000001,
 92887: 39994.7}

uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df=df.drop(['Unnamed: 0'],axis=1)
    df=df.sort_values(by=['Created Date'])
    
    df['Created Date']=pd.to_datetime(df['Created Date'])
    df=df.replace({'Zip':Mean_encoded_Income})
    
    df['f1']=np.abs(df['Completed_Jobs'])*np.abs(df['Zip'])
    df['f2']=np.sqrt(df['Completed_Jobs']**3)*np.abs(df['Avg_Sales'])
    df['f3']=np.abs(np.sqrt(df['Completed_Jobs']) - np.sqrt(df['tech_count']))
    df['f4']=np.log(np.sqrt(df['Completed_Jobs'])*df['TMAX']**3)
    
    
    df['year'] = df['Created Date'].dt.year
    df['month'] = df['Created Date'].dt.month
    


    

    df['quarter'] = df['Created Date'].dt.quarter
    
    date=df['Created Date']
    
    df=df.drop(['Created Date'],axis=1)
    
    df['year'] = df['year'].map({2019: 0, 2020: 1,2021:2})
    
    df['month_cos']= np.cos(2 * np.pi * (df['month']/12))
    df['quarter_sin'] = np.sin(2 * np.pi * (df['quarter']/4))
    
    
    df=df.drop(['Completed_Jobs','TMAX','tech_count','Avg_Sales','Zip','month','quarter'],axis=1)
    
    
    prediction=model.predict(df)
    
    
    
    new_df=pd.DataFrame({'Date':date,'Predicted':prediction})
    
    new_df = new_df.rename(columns={'Date':'index'}).set_index('index')
    
    st.line_chart(new_df)


    
    
    
    
    
    
    
    
    
    


    