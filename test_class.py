import matplotlib.pyplot as plt
import numpy as np
import random
from random import *

counts = 1000000


class cpb:
    tob = []
    alc = []

    @staticmethod
    def alcohol():

        '''
        To calculate various aspects related to Alcoholism related variability.
        ll_cc: life years lost to chronic conditions
        ll_ac: life years lost to acute conditions
        m_cc: morbidity related quality added life years lost from chronic conditions
        m_ac: morbidity related quality added life years lost from acute conditions
        tot_ll: total quality added life years lost
        d_sc: delivery of screening and counseling
        a_sc: adherence with screening
        e_sc: effectiveness of counseling at changing behavior
        e_cc: efficacy of behavior change at reducing chronic conditions
        e_ac: efficacy of behavior change at reducing acute conditions
        e_w: weighted efficacy of behavior change at reducing total QAL lost
        p_ll: predicted QALs lost
        gain_ql_alc: quality added life years gained
        alc: appended list of quality of life years gained
        '''


        for i in range(0, counts):
            ll_cc = 45000 * 20
            ll_cc = uniform(0.80 * ll_cc, 1.20 * ll_cc)  # ll_cc: Range: =/- 20%
            ll_ac = 45000 * 10
            ll_ac = uniform(0.80 * ll_ac, 1.20 * ll_ac)  # ll_ac: Range: =/- 20%
            m_cc = 40000 * 20
            m_cc = uniform(0.60 * m_cc, 1.40 * m_cc)
            m_ac = 40000 * 10
            m_ac = uniform(0.60 * m_ac, 1.40 * m_ac)  # m_ac: Range: =/- 40%
            tot_ll = ll_cc + ll_ac + m_cc + m_ac
            d_sc = uniform(0.05, 0.25)
            a_sc = uniform(0.8, 0.95)
            e_sc = uniform(0.10, 0.35)
            e_cc = uniform(0.75, 1)
            e_ac = uniform(0.10, 0.50)
            e_w = 1 / tot_ll * (e_cc * (ll_ac + m_ac) + e_ac * (ll_cc + m_cc))
            p_ll = tot_ll / (1 - d_sc * e_sc * e_w)
            gain_ql_alc = p_ll * a_sc * e_sc * e_w
            alc = alc.append(gain_ql_alc)
            return alc
        cpb.alcohol()




    @staticmethod
    def tobacco():
        '''To calculate various aspects related to Smoking related variability.
        sm: life years lost to chronic conditions
        q_sm: life years lost to acute conditions
        sm_il: morbidity related quality added life years lost from chronic conditions
        per_sm: morbidity related quality added life years lost from acute conditions
        f_sm: total quality added life years lost
        rel_sm: delivery of screening and counseling
        m_sm: adherence with screening
        a_m: effectiveness of counseling at changing behavior
        t_sc: efficacy of behavior change at reducing chronic conditions
        eff: efficacy of behavior change at reducing acute conditions
        p_burden: weighted efficacy of behavior change at reducing total QAL lost
        tob: predicted QALs lost'''

        for i in range(0, counts):
            sm = uniform(397500, 510000)  # a: Number of ever smokers in birth-cohort of 1,000,000
            q_sm = 5.65  # b: Average gains in life expentancy for one quit
            q_sm = uniform(0.75 * q_sm, 1.25 * q_sm)
            sm_il = 177266  # c: QALYs lost to smoking atributable illness in birth cohort
            sm_il = uniform(0.5 * sm_il, 1.5 * sm_il)
            per_sm = sm_il / sm  # d: QALYs lost to smoking-attributable illnesss per smoker
            f_sm = uniform(0.47, 0.57)  # e: Portion of ever-smokers who are former smokers
            rel_sm = uniform(0.20, 0.56)  # f: Relative risk of SA disease for former smokers compared to current ones
            m_sm = per_sm / (f_sm * rel_sm + (1 - f_sm))  # g: QALYs lost from smoking morbidity percontinuing smoker
            a_m = m_sm - m_sm * rel_sm  # h: QALYs saved from avoided morbidity per smoker quit
            t_sc = uniform(0.05, 0.25)  # Delivery of screening and counseling
            eff = 0.030  # j: Long-term effectiveness of repeated counseling in inducing quits
            p_burden = sm * (q_sm + a_m) * eff  # k: Clinically preventable burden (QALYs saved)
            tob = tob.append(p_burden)
        return tob

#sorted_alc = sorted(alcohol())
#sorted_tob = sorted()

#class conf_int:
    #sorted_alc = sorted(alc)
    #lower_limit1 = sorted_alc[int(0.025 * counts)]
    #upper_limit1 = sorted_alc[int(0.975 * counts)]

    #sorted_tob = sorted(tob)
    #lower_limit2 = sorted_tob[int(0.025 * counts)]
    #upper_limit2 = sorted_tob[int(0.975 * counts)]


cpb.alcohol()



