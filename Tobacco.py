import random
from random import *
import matplotlib.pyplot as plt
import numpy as np

tob = []  # empty list to be filled for quality added life years gained
counts = 100000  # NUMBER OF MONTE CARLO SIMULATIONS

# =================================================================================
# CALCULATIONS FOR QALYS GAINED DUE TO INTERVENTION IN TOBACCO CONSUMPTION
# =================================================================================
for i in range(0, counts):
    smokers = uniform(1500000, 2000000)  # smokers: Number of ever smokers in birth-cohort of 4,000,000
    le_gain = 5.65  # le_gain: Average gains in life expectancy for one quit
    le_gain = uniform(0.75 * le_gain, 1.25 * le_gain)  # Range: =/- 25%
    le_lost = np.random.randint(600000, 850000)  # le_lost: QALYs lost to smoking attributable illness in birth cohort
    le_lost = uniform(0.7 * le_lost, 1.3 * le_lost)  # Range: =/- 30%
    le_per_sm = le_lost / smokers  # le_per_sm: QALYs lost to smoking-attributable illness per smoker
    frm_sm = uniform(0.47, 0.57)  # frm_sm: Portion of ever-smokers who are former smokers
    rel_rsk = uniform(0.20, 0.56)  # rel_rsk: Relative risk of smoking disease for former smokers compared to current
    q_loss = le_per_sm / (frm_sm * rel_rsk + (1 - frm_sm))  # q_loss: QALYs lost from morbidity per continuing smoker
    q_saved = q_loss - q_loss * rel_rsk  # q_saved: QALYs saved from avoided morbidity per smoker quit
    beh_ch = uniform(0.2, 0.8)  # change in behavior
    eff_sm = uniform(0.03 * beh_ch, 0.8 * beh_ch)  # eff_sm: Long-term effectiveness of counseling inducing quits
    prevent = smokers * (le_gain + q_saved) * eff_sm  # prevent: Clinically preventable burden (QALYs saved)
    tob.append(prevent)

tob_sorted = sorted(tob)


def cohort_tob():
    """
    This function calculates the mean and standard deviation of quality added life years to the cohort of 4,000,000
    population. It also plots histogram showing QALYs within the cohort over entire Monte Carlo Simulation bracket.
    lowerlimit:lower fixed quantile limit
    upperlimit: upper fixed quantile limit
    bins: fixed number of bins
    return: plt

    """
    lowerlimit = tob_sorted[int(0.025 * counts)]
    upperlimit = tob_sorted[int(0.975 * counts)]
    print("\n\nQALYS GAINED IN COHORT")
    print("Mean for QALYs gained (CPB): " + str(int(np.mean(tob_sorted))))
    print("Standard deviation for QALYs gained (CPB): " + str(int(np.std(tob_sorted))))
    print("Confidence interval: [" + str(int(lowerlimit)) + ", " + str(int(upperlimit)) + "]")
    print("Number of simulations: " + str(len(tob_sorted)))

    # Build Histogram and Graph
    bins = np.arange(0, 1000000, 2000)  # fixed bin size
    plt.xlim([200000, 600000])
    plt.xticks(range(200000, 600000, 100000))
    plt.hist(tob_sorted, bins=bins, alpha=0.5)

    # Cohort calculations Graph
    plt.title('Histogram results')
    plt.xlabel('Cohort: Calculated QALYs for tobacco screening and intervention')
    plt.ylabel('Frequency (arb. units)')
    plt == plt.show()
    return plt


NI = 226000000  # number of person years above 15 years old for a cohort of 4,000,000
tob_final = [i / NI for i in tob_sorted]


def intervention_tobacco():
    """
    This function calculates the quality of life years gained per individual intervention taking into account
    all interventions and constructing confidence intervals, calculating the mean and standard deviation of years gained
    and plots histogram showing QALYs/intervention over entire Monte Carlo Simulation bracket.
    lowerlimit:lower fixed quantile limit
    upperlimit: upper fixed quantile limit
    bins: fixed number of bins
    return: plt

    """

    # Calculate the QALYs gained by intervention
    print("\n\nQALYS GAINED PER INDIVIDUAL INTERVENTION")
    print("Number of interventions in the cohort: ", NI)
    lowerlimit = tob_final[int(0.025 * counts)]
    upperlimit = tob_final[int(0.975 * counts)]

    # Calculate Mean and Standard Deviation
    print("Mean for QALYs gained (CPB): " + str((np.mean(tob_final))))
    print("Standard deviation for QALYs gained (CPB): " + str((np.std(tob_final))))
    print("Confidence interval: [" + str((lowerlimit)) + ", " + str((upperlimit)) + "]")
    print("Number of simulations: " + str(len(tob_final)))

    # Build Histogram and Graph
    bins = np.arange(0, 0.0100, 0.000005)  # fixed bin size
    plt.xlim([0, 0.0025])
    plt.hist(tob_final, bins=bins, alpha=0.5)
    plt.title('Histogram results')
    plt.xlabel('Calculated QALYs/intervention')
    plt.ylabel('Frequency (arb. units)')
    plt == plt.show()
    return plt


tob_intervention_mean = np.mean(tob_final)
tob_intervention_stdev = np.std(tob_final)


# ===========================================
# IMPACT OF NGO INTERVENTION ON TOBACCO
# ===========================================

def impact_ngo_tobacco():
    """
    This function calculates the mean quality added life years for a period of three years after taking fluctuations
    of patient traffic into account and calculates the monetary value saved.
    patient_volume: number of people being intervened in a single year
    Fluctuation: year on year fluctuation of people visiting the NGO for health related issues
    QALY_dollars: Quality adjusted life years gained in terms of dollars
    Term1: previous year with patient fluctuation
    Term2: current year patient volume
    Term3: next year patient volume with fluctuation
    return: none

    >>>patient_volume=300
    >>>Fluctuation = 0.2
    >>>QALY_dollars = 132200
    Tobacco Mean QALYS/year:  0.420881330332
    Tobacco Stdev QALYS/year:  0.107850728675
    Monetary value (Mean):  55640.5118698
    Monetary value (Stdev):  14257.8663308

    >>>patient_volume= 300
    >>>Fluctuation = 0
    >>>QALY_dollars = 100000
    Tobacco Mean QALYS/year:  0.420614748869
    Tobacco Stdev QALYS/year:  0.0664539296649
    Monetary value (Mean):  42061.4748869
    Monetary value (Stdev):  6645.39296649

    """

    patient_volume = np.random.randint(300, 500)
    Fluctuation = np.random.random()
    QALY_dollars = np.random.randint(125000, 150000)

    QALYs_year_mean = tob_intervention_mean * patient_volume

    # Var(AB)=Var(A)Var(B)+Var(A)Mean2(B)+Mean2(A)Var(B)
    Term1 = (tob_intervention_stdev * patient_volume * Fluctuation) ** 2
    Term2 = (tob_intervention_stdev * patient_volume) ** 2
    Term3 = (tob_intervention_mean * patient_volume * Fluctuation) ** 2

    QALYs_year_stdev = (Term1 + Term2 + Term3) ** 0.5

    print("Impact of NGO:\n")
    print("Patient volume: ", patient_volume)
    print("Year on fluctuation:", Fluctuation)
    print("Monetary value of one QALY: ", QALY_dollars)
    print("Tobacco Mean QALYS/year: ", QALYs_year_mean)
    print("Tobacco Stdev QALYS/year: ", QALYs_year_stdev)
    print("Monetary value (Mean): ", QALYs_year_mean * QALY_dollars)
    print("Monetary value (Stdev): ", QALYs_year_stdev * QALY_dollars)
    print("At long term effectiveness of councelling {0:.2f}".format(eff_sm * 100),
          "% and a behavior changefactor of {0:.2f}".format(beh_ch * 100), "%")
    print("Quality savings for individual per year {0:.2f}".format(QALYs_year_mean * QALY_dollars / patient_volume),
          "Dollars for", counts, "simulations")


if __name__ == '__main__':
    cohort_tob()
    intervention_tobacco()
    impact_ngo_tobacco()