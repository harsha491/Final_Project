import random
from random import *
import matplotlib.pyplot as plt
import numpy as np

counts = 100000
La = []
Lk = []

# alcohol
for i in range(0, counts):
    a1 = np.random.randint(650000, 700000)  # a1: Alcohol-atributable life years lost to chronic conditions
    a1 = uniform(0.80 * a1, 1.20 * a1)  # a1: Range: =/- 20%
    a2 = np.random.randint(1300000, 1800000)  # a2: Alcohol-atributable life years lost to acute conditions
    a2 = uniform(0.80 * a2, 1.20 * a2)  # a2: Range: =/- 20%
    a3 = np.random.randint(350000,
                           400000)  # a3: Alcohol-atributable morbidity-related QALYs lost from chronic conditions
    a3 = uniform(0.60 * a3, 1.40 * a3)  # a3: Range: =/- 40%
    a4 = np.random.randint(100000, 120000)  # a4: Alcohol-atributable morbidity-related QALYs lost from acute conditions
    a4 = uniform(0.60 * a4, 1.40 * a4)  # a4: Range: =/- 40%
    a5 = a1 + a2 + a3 + a4  # Total alcohol-attributable QALYs lost
    a6 = uniform(0.05, 0.25)  # Delivery of screening and counseling
    a8 = uniform(0.8, 0.95)  # Adherence with screening
    a9 = uniform(0.6, 0.9)  # Average sensitivity of CAGE & AUDIT questionnaires
    a10 = uniform(0.10, 0.35)  # Effectiveness of counseling at changing behaviour
    a11 = uniform(0.75, 1)  # Efficacy of behaviour change at reducing chronic conditions
    a12 = uniform(0.10, 0.50)  # Efficacy of behaviour change at reducing chronic conditions
    a13 = 1 / a5 * (a11 * (a2 + a4) + a12 * (
                a1 + a3))  # Weighted efficacy of behaviour change at reducing total alcohol-attributable QALYs lost
    a7 = a5 / (1 - a6 * a10 * a13)  # Predicted alcohol-attributable QALYs lost
    a14 = a7 * a8 * a9 * a10 * a13  # QALYS gained, CPB
    La.append(a14)

Lsorted_alc = sorted(La)

# tobacco

for i in range(0, counts):
    a = uniform(1500000, 2000000)  # a: Number of ever smokers in birth-cohort of 4,000,000
    b = 5.65  # b: Average gains in life expentancy for one quit
    b = uniform(0.75 * b, 1.25 * b)
    c = np.random.randint(600000, 850000)  # c: QALYs lost to smoking atributable illness in birth cohort
    c = uniform(0.5 * c, 1.5 * c)
    d = c / a  # d: QALYs lost to smoking-attributable illnesss per smoker
    e = uniform(0.47, 0.57)  # e: Portion of ever-smokers who are former smokers
    f = uniform(0.20, 0.56)  # f: Relative risk of SA disease for former smokers compared to current ones
    g = d / (e * f + (1 - e))  # g: QALYs lost from smoking morbidity percontinuing smoker
    h = g - g * f  # h: QALYs saved from avoided morbidity per smoker quit
    j = 0.03  # j: Long-term effectiveness of repeated counseling in inducing quits
    k = a * (b + h) * j  # k: Clinically preventable burden (QALYs saved)
    Lk.append(k)

Lsorted_tob = sorted(Lk)


def cohort_alc():
    lowerlimit = Lsorted_alc[int(0.025 * counts)]
    upperlimit = Lsorted_alc[int(0.975 * counts)]
    print("\n\nQALYS GAINED IN COHORT:\n")
    print("Mean for QALYs gained (CPB): " + str(int(np.mean(Lsorted_alc))))
    print("Standard deviation for QALYs gained (CPB): " + str(int(np.std(Lsorted_alc))))
    print("Confidence interval: [" + str(int(lowerlimit)) + ", " + str(int(upperlimit)) + "]")
    print("Number of simulations: " + str(len(Lsorted_alc)))

    bins = np.arange(0, 1000000, 5000)  # fixed bin size
    plt.xlim([0, 600000])
    plt.xticks(range(0, 600000, 100000))
    plt.hist(La, bins=bins, alpha=0.5)
    plt.title('Histogram results')
    plt.xlabel('Cohort: Calculated QALYs for alcohol screening and intervention')
    plt.ylabel('Frequency (arb. units)')
    plt.show()


def cohort_tob():
    lowerlimit = Lsorted_tob[int(0.025 * counts)]
    upperlimit = Lsorted_tob[int(0.975 * counts)]
    print("\n\nQALYS GAINED IN COHORT")
    print("Mean for QALYs gained (CPB): " + str(int(np.mean(Lsorted_tob))))
    print("Standard deviation for QALYs gained (CPB): " + str(int(np.std(Lsorted_tob))))
    print("Confidence interval: [" + str(int(lowerlimit)) + ", " + str(int(upperlimit)) + "]")
    print("Number of simulations: " + str(len(Lsorted_tob)))
    bins = np.arange(0, 1000000, 2000)  # fixed bin size
    plt.xlim([200000, 600000])
    plt.xticks(range(200000, 600000, 100000))
    plt.hist(Lk, bins=bins, alpha=0.5)
    plt.title('Histogram results')
    plt.xlabel('Cohort: Calculated QALYs for tobacco screening and intervention')
    plt.ylabel('Frequency (arb. units)')
    plt.show()


NI = np.random.randint(206000000, 226000000)
Lfinal_alc = [i / NI for i in Lsorted_alc]


def inter_alc():
    print("\n\nQALYS GAINED PER INDIVIDUAL INTERVENTION:\n")

    print("Number of interventions in the cohort: ", NI)

    lowerlimit = Lfinal_alc[int(0.025 * counts)]
    upperlimit = Lfinal_alc[int(0.975 * counts)]

    print("Mean for QALYs gained (CPB): " + str((np.mean(Lfinal_alc))))
    print("Standard deviation for QALYs gained (CPB): " + str((np.std(Lfinal_alc))))
    print("Confidence interval: [" + str((lowerlimit)) + ", " + str((upperlimit)) + "]")
    print("Number of simulations: " + str(len(Lfinal_alc)))

    bins = np.arange(0, 0.0035, 0.000005)  # fixed bin size
    plt.xlim([0, 0.0035])
    plt.hist(Lfinal_alc, bins=bins, alpha=0.5)
    plt.title('Histogram results')
    plt.xlabel('Calculated QALYs/intervention')
    plt.ylabel('Frequency (arb. units)')
    plt.show()


alc_intervention_mean = np.mean(Lfinal_alc)
alc_intervention_stdev = np.std(Lfinal_alc)
alc_patient_volume = np.random.randint(300, 500)
Fluctuation = 0.20
QALY_dollars = np.random.randint(125000, 150000)


def impact_alc():
    QALYs_year_mean = alc_intervention_mean * alc_patient_volume
    # Var(AB)=Var(A)Var(B)+Var(A)Mean2(B)+Mean2(A)Var(B)
    Term1 = (alc_intervention_stdev * alc_patient_volume * Fluctuation) ** 2
    Term2 = (alc_intervention_stdev * alc_patient_volume) ** 2
    Term3 = (alc_intervention_mean * alc_patient_volume * Fluctuation) ** 2

    QALYs_year_stdev = (Term1 + Term2 + Term3) ** 0.5
    print("Impact of NGO:\n")
    print("Patients:", alc_patient_volume)
    print("Alcohol Mean QALYS/year: ", QALYs_year_mean)
    print("Alcohol_Stdev_QALYS/year: ", QALYs_year_stdev)
    print("Monetary value (Mean): ", QALYs_year_mean * QALY_dollars)
    print("Monetary value (Stdev): ", QALYs_year_stdev * QALY_dollars)


NI2 = np.random.randint(206000000, 226000000)
Lfinal_tob = [i / NI2 for i in Lsorted_tob]


def inter_tob():
    print("\n\nQALYS GAINED PER INDIVIDUAL INTERVENTION")

    print("Number of interventions in the cohort: ", NI2)

    lowerlimit = Lfinal_tob[int(0.025 * counts)]
    upperlimit = Lfinal_tob[int(0.975 * counts)]

    print("Mean for QALYs gained (CPB): " + str((np.mean(Lfinal_tob))))
    print("Standard deviation for QALYs gained (CPB): " + str((np.std(Lfinal_tob))))
    print("Confidence interval: [" + str((lowerlimit)) + ", " + str((upperlimit)) + "]")
    print("Number of simulations: " + str(len(Lfinal_tob)))

    bins = np.arange(0, 0.0100, 0.000005)  # fixed bin size
    plt.xlim([0, 0.0025])
    plt.hist(Lfinal_tob, bins=bins, alpha=0.5)
    plt.title('Histogram results')
    plt.xlabel('Calculated QALYs/intervention')
    plt.ylabel('Frequency (arb. units)')
    plt.show()


tob_intervention_mean = np.mean(Lfinal_tob)
tob_intervention_stdev = np.std(Lfinal_tob)
tob_patient_volume = np.random.randint(300, 500)


def impact_ngo_tob():
    QALYs_year_mean = tob_intervention_mean * tob_patient_volume
    # Var(AB)=Var(A)Var(B)+Var(A)Mean2(B)+Mean2(A)Var(B)
    Term1 = (tob_intervention_stdev * tob_patient_volume * Fluctuation) ** 2
    Term2 = (tob_intervention_stdev * tob_patient_volume) ** 2
    Term3 = (tob_intervention_mean * patient_volume * Fluctuation) ** 2

    QALYs_year_stdev = (Term1 + Term2 + Term3) ** 0.5

    print("Impact of NGO on tobacco")
    print("Patient volume: ", tob_patient_volume)
    print("Monetary value of one QALY: ", QALY_dollars)
    print("Tobacco Mean QALYS/year: ", QALYs_year_mean)
    print("Tobacco Stdev QALYS/year: ", QALYs_year_stdev)
    print("Monetary value (Mean): ", QALYs_year_mean * QALY_dollars)
    print("Monetary value (Stdev): ", QALYs_year_stdev * QALY_dollars)


if __name__ == '__main__':
    print("\nCALCULATIONS FOR ALCOHOL INTERVENTION:\n")
    cohort_alc()
    inter_alc()
    impact_alc()

    print("\nCALCULATIONS FOR Tobacco INTERVENTION:\n")
    cohort_tob()
    inter_tob()
    impact_ngo_tob()



