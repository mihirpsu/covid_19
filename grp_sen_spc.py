# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:11:26 2020

@author: Mihir Mehta
"""

import pandas as pd

def grp_sen_spc_func(data_penn,vi_1,vi_3,compare_dt):
    #graph
    vi_1["Type"] = "Classification"
    vi_3["Type"] = "Regression"
    v4 = vi_1.append(vi_3)
    v4.columns = ["Weight","Variable","Type"]
    v4["Weight"]=v4["Weight"]*100
    v5 = v4.pivot(index='Type', columns='Variable', values='Weight')
    v5.reset_index(inplace=True)
    v6 = v5.set_index('Type').T
    v6["Total"]=v6.iloc[:,0]+v6.iloc[:,1]
    v7= v6.sort_values("Total",ascending=False)
    v7.drop(columns=["Total"],inplace=True)
     
    
    data_penn["RankPA"] =data_penn["one_prb"].rank(ascending=1)
    data_penn["RankPR"] =data_penn["exp_num"].rank(ascending=1,method="first")
    data_penn["RankPE"] =data_penn["index_t"].rank(ascending=1)
    data_penn["RankPAf"] = pd.qcut(data_penn["RankPA"], 20, labels=range(1,21)).astype(int)
    data_penn["RankPEf"] = pd.qcut(data_penn["RankPE"], 20, labels=range(1,21)).astype(int)
    
    #sensitivity and specificity calculation
    prc_num = data_penn["Con_Ind"].mean()
    def myround(x, base=5):
        return (base * (round(x*100/base)+1))
    prc_risk = 20 - ((myround(prc_num)*20)/100)
    safe_cty = data_penn.query("Confirmed==0.0 and RankPAf<3 and RankPEf<3")["FIPS"].tolist()
    safe_cty_cnt = len(safe_cty)   
    risk_cty = data_penn.query("Confirmed==0.0 and RankPAf>{p} and RankPEf>{p}".format(p=prc_risk))["FIPS"].tolist()
    risk_cty_cnt = len(risk_cty)
    compare_fips =compare_dt[["FIPS","Confirmed"]]
    fail_safe = len(compare_fips.query('FIPS=={sfs}'.format(sfs=safe_cty))["FIPS"].tolist())
    succ_risk = len(compare_fips.query('FIPS=={rsk}'.format(rsk=risk_cty))["FIPS"].tolist())
    spc = round(((safe_cty_cnt-fail_safe)/safe_cty_cnt)*100,2)
    sen = round(((succ_risk/risk_cty_cnt)*100),2)
    return(v7,data_penn,spc,sen)

