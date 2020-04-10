# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:41:00 2020

@author: Mihir Mehta
"""

import numpy as np
from xgboost import XGBClassifier,XGBRegressor
from hyperopt import hp, fmin, STATUS_OK, STATUS_FAIL

class HPOpt_cls(object):

    def __init__(self, x_train, x_test, y_train, y_test):
        self.x_train = x_train
        self.x_test  = x_test
        self.y_train = y_train
        self.y_test  = y_test

    def process(self, fn_name, space, trials, algo, max_evals):
        fn = getattr(self, fn_name)
        try:
            result = fmin(fn=fn, space=space, algo=algo, max_evals=max_evals, trials=trials)
        except Exception as e:
            return {'status': STATUS_FAIL,
                    'exception': str(e)}
        return result, trials

    def xgb_reg(self, para):
        reg = XGBClassifier(**para['reg_params'],silent = True)
        return self.train_reg(reg, para)

    def train_reg(self, reg, para):
        reg.fit(self.x_train, self.y_train,
                eval_set=[(self.x_train, self.y_train), (self.x_test, self.y_test)],
                **para['fit_params'])
        pred = reg.predict(self.x_test)
        loss = para['loss_func'](self.y_test, pred)
        return {'loss': loss, 'status': STATUS_OK}


#define parameters for HYPEROPT
xgb_reg_params = {
    'learning_rate':    hp.choice('learning_rate',    np.arange(0.01, 0.31, 0.05)),
    'max_depth':        hp.choice('max_depth',        np.arange(2, 9, 1, dtype=int)),
    'min_child_weight': hp.choice('min_child_weight', np.arange(2, 9, 1, dtype=int)),
    'colsample_bytree': hp.choice('colsample_bytree', np.arange(0.4, 1.1, 0.1)),
    'subsample':        hp.choice('subsample', np.arange(0.4, 1.1, 0.1)),
    'n_estimators':     hp.choice('n_estimators',np.concatenate([np.arange(10,110,10),np.arange(110,150,40)]) ),
    'reg_alpha': hp.choice('reg_alpha',np.arange(0,1.1,0.1)),
    'reg_lambda': hp.choice('reg_lambda',np.arange(0,1.1,0.1))
}
xgb_fit_params = {'eval_metric': 'auc',
    'early_stopping_rounds': 50,
    'verbose': False}


class HPOpt_reg(object):

    def __init__(self, x_train, x_test, y_train, y_test):
        self.x_train = x_train
        self.x_test  = x_test
        self.y_train = y_train
        self.y_test  = y_test

    def process(self, fn_name, space, trials, algo, max_evals):
        fn = getattr(self, fn_name)
        try:
            result = fmin(fn=fn, space=space, algo=algo, max_evals=max_evals, trials=trials)
        except Exception as e:
            return {'status': STATUS_FAIL,
                    'exception': str(e)}
        return result, trials

    def xgb_reg(self, para):
        reg = XGBRegressor(**para['reg_params'],silent = True)
        return self.train_reg(reg, para)

    def train_reg(self, reg, para):
        reg.fit(self.x_train, self.y_train,
                eval_set=[(self.x_train, self.y_train), (self.x_test, self.y_test)],
                **para['fit_params'])
        pred = reg.predict(self.x_test)
        loss = para['loss_func'](self.y_test, pred)
        return {'loss': loss, 'status': STATUS_OK}

xgb_fit_params_r = {
    'eval_metric': 'rmse',
    'early_stopping_rounds': 50,
    'verbose': False
#    ,"eval_set" : [[X_valid, Y_valid]]
}


iterations =1000
lr_rt = np.arange(0.01, 0.51, 0.05)
mx_de =  np.arange(2, 9, 1, dtype=int)
mn_chd = np.arange(2, 9, 1, dtype=int)
col_tr = np.arange(0.4, 1.1, 0.1)
sub_sm = np.arange(0.4, 1.1, 0.1)
n_est = np.concatenate([np.arange(10,110,10),np.arange(110,150,40)])
alph = np.arange(0,1.1,0.1)
lamd = np.arange(0,1.1,0.1)

par_v_nm = [lr_rt,mx_de,mn_chd,col_tr,sub_sm,n_est,alph,lamd]
par_a_nm = ['learning_rate','max_depth','min_child_weight','colsample_bytree','subsample','n_estimators','reg_alpha','reg_lambda']

par_va_nm= {}

for i in range(0,len(par_v_nm)):
    par_va_nm.update({par_a_nm[i]:par_v_nm[i]})

