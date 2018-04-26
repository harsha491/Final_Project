from random import *
import matplotlib.pyplot as plt
import numpy as np
import random

alc = []
tob = []
counts = 1000000  # Number of simulations

# modelling for 1,000,000 population
for i in range(0, counts):
    ll_cc = 45000 * 20  # a1: Alcohol-atributable life years lost to chronic conditions
    ll_cc = uniform(0.80 * ll_cc, 1.20 * ll_cc)  # a1: Range: =/- 20%
    ll_ac = 45000 * 10  # a2: Alcohol-atributable life years lost to acute conditions
    ll_ac = uniform(0.80 * ll_ac, 1.20 * ll_ac)  # a2: Range: =/- 20%
    m_cc = 40000 * 20  # a3: Alcohol-atributable morbidity-related QALYs lost from chronic conditions
    m_cc = uniform(0.60 * m_cc, 1.40 * m_cc)  # a3: Range: =/- 40%
    m_ac = 40000 * 10  # a4: Alcohol-atributable morbidity-related QALYs lost from acute conditions
    m_ac = uniform(0.60 * m_ac, 1.40 * m_ac)  # a4: Range: =/- 40%
    tot_ll = ll_cc + ll_ac + m_cc + m_ac  # Total alcohol-attributable QALYs lost
    d_sc = uniform(0.05, 0.25)  # Delivery of screening and counseling
    a_sc = uniform(0.8, 0.95)  # Adherence with screening

    e_sc = uniform(0.10, 0.35)  # Effectiveness of counseling at changing behaviour
    e_cc = uniform(0.75, 1)  # Efficacy of behaviour change at reducing chronic conditions
    e_ac = uniform(0.10, 0.50)  # Efficacy of behaviour change at reducing acute conditions
    e_w = 1 / tot_ll * (e_cc * (ll_ac + m_ac) + e_ac * (
                ll_cc + m_cc))  # Weighted efficacy of behaviour change at reducing total alcohol-attributable QALYs lost
    p_ll = tot_ll / (1 - d_sc * e_sc * e_w)  # Predicted alcohol-attributable QALYs lost
    gain_ql_alc = p_ll * a_sc * e_sc * e_w  # QALYS gained, CPB

    alc.append(gain_ql_alc)

# modelling for 1,000,000 population
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
    tob.append(p_burden)

# Sort and Calculate Confidence Intervals
sorted_alc = sorted(alc)
lower_limit1 = sorted_alc[int(0.025 * counts)]
upper_limit1 = sorted_alc[int(0.975 * counts)]

sorted_tob = sorted(tob)
lower_limit2 = sorted_tob[int(0.025 * counts)]
upper_limit2 = sorted_tob[int(0.975 * counts)]

# Calculate Mean and Standard Deviation
print("\n\nQuality added life years gained in alcohol cohort")
print("Mean for life years gained (CPB): " + str(int(np.mean(sorted_alc))))
print("Standard deviation for life years gained (CPB): " + str(int(np.std(Lsorted_alc))))
print("Confidence interval: [" + str(int(lower_limit1)) + ", " + str(int(upper_limit1)) + "]")
print("Number of simulations: " + str(len(Lsorted_alc)))

# Calculate Mean and Standard Deviation
print("\n\nQuality added life years gained in smoking cohort")
print("Mean for life years gained (CPB): " + str(int(np.mean(sorted_tob))))
print("Standard deviation for life years gained (CPB): " + str(int(np.std(sorted_tob))))
print("Confidence interval: [" + str(int(lower_limit2)) + ", " + str(int(upper_limit2)) + "]")
print("Number of simulations: " + str(len(sorted_tob)))

# Calculate the QALYs gained by intervention
print("\n\nQuality_per_intervention_alcohol")
NI = int(d_sc * 1000000)
print("Number of interventions in the cohort: ", NI)
final_alc = [i / NI for i in sorted_alc]
lowerlimit_alc = final_alc[int(0.025 * counts)]
upperlimit_alc = final_alc[int(0.975 * counts)]

# Calculate Mean and Standard Deviation
print("Mean quality years gained (CPB): " + str((np.mean(Lfinal_alc))))
print("Standard deviation (CPB): " + str((np.std(Lfinal_alc))))
print("Confidence interval: [" + str((lowerlimit_alc)) + ", " + str((upperlimit_alc)) + "]")
print("Number of simulations: " + str(len(Lfinal_alc)))

# Calculate the QALYs gained by intervention
print("\n\nQuality_per_intervention_tobacco")
NI = int(t_sc * 1000000)
print("Number of interventions in the cohort: ", NI)
final_tob = [i / NI for i in sorted_tob]
lowerlimit_tob = final_tob[int(0.025 * counts)]
upperlimit_tob = final_tob[int(0.975 * counts)]

# Calculate Mean and Standard Deviation
print("Mean quality years gained (CPB): " + str((np.mean(Lfinal_tob))))
print("Standard deviation: " + str((np.std(Lfinal_tob))))
print("Confidence interval: [" + str((lowerlimit_tob)) + ", " + str((upperlimit_tob)) + "]")
print("Number of simulations: " + str(len(Lfinal_tob)))

# Build Histogram and Graph
bins = np.arange(0, 0.0035, 0.000005)  # fixed bin size
plt.xlim([0, 0.0035])
plt.hist(Lfinal_alc, bins=bins, alpha=0.5)
plt.hist(Lfinal_tob, bins=bins, alpha=0.5)
plt.title('Histogram results')
plt.xlabel('Calculated quality/intervention')
plt.ylabel('Frequency (arb. units)')
plt.show()

# Impact of NGO

intervention_mean_alc = np.mean(final_alc)
intervention_stdev_alc = np.std(final_alc)
intervention_mean_tob = np.mean(final_tob)
intervention_stdev_tob = np.std(final_tob)
patient_volume_alc = random.randint(300, 500)
Fluctuation_alc = uniform(0.1, 0.2)
patient_volume_tob = random.randint(300, 500)
Fluctuation_tob = uniform(0.1, 0.2)
quality_years_alc_dollars = random.randint(20000, 500000)
quality_years_tob_dollars = random.randint(20000, 500000)

qual_year_mean_alc = intervention_mean_alc * patient_volume_alc
# Var(AB)=Var(A)Var(B)+Var(A)Mean2(B)+Mean2(A)Var(B)
Term1_alc = (intervention_stdev_alc * patient_volume_alc * Fluctuation_alc) ** 2
Term2_alc = (intervention_stdev_alc * patient_volume_alc) ** 2
Term3_alc = (intervention_mean_alc * patient_volume_alc * Fluctuation_alc) ** 2

qual_year_mean_tob = intervention_mean_tob * patient_volume_tob
Term1_tob = (intervention_stdev_tob * patient_volume_tob * Fluctuation_tob) ** 2
Term2_tob = (intervention_stdev_tob * patient_volume_tob) ** 2
Term3_tob = (intervention_mean_tob * patient_volume_tob * Fluctuation_tob) ** 2

qual_year_stdev_alc = (Term1_alc + Term2_alc + Term3_alc) ** 0.5
qual_year_stdev_tob = (Term1_tob + Term2_tob + Term3_tob) ** 0.5

print("\n\nAlcohol")
print("patient volume:", patient_volume_alc)
print("Fluctuation", Fluctuation_alc)
print("Mean quality/year: ", qual_year_mean_alc)
print("Quality_Stdev/year: ", qual_year_stdev_alc)
print("Monetary value (Mean): ", qual_year_mean_alc * quality_years_alc_dollars)
print("Monetary value (Stdev): ", qual_year_stdev_alc * quality_years_alc_dollars)

print("\n\nTobbaco")
print("patient volume:", patient_volume_tob)
print("Fluctuation", Fluctuation_tob)
print("Mean QALYS/year: ", qual_year_mean_tob)
print("Quality_Stdev/year: ", qual_year_stdev_tob)
print("Monetary value (Mean): ", qual_year_mean_tob * quality_years_tob_dollars)
print("Monetary value (Stdev): ", qual_year_stdev_tob * quality_years_tob_dollars)