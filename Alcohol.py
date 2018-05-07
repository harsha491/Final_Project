import matplotlib.pyplot as plt
import numpy as np
import random
from random import *

counts = 100000  # number of Monte Carlo simulations
alc = []  # empty list to be filled for quality adjusted life years gained

# =================================================================================
# CALCULATIONS FOR QALYS GAINED DUE TO INTERVENTION IN ALCOHOL CONSUMPTION
# =================================================================================
for i in range(0, counts):
    # calculating QALYs lost to chronic and acute conditions due to alcohol in birth cohort of 4,000,000
    alc_chr = np.random.randint(650000, 700000)  # alc_chr: Alcohol-attributable life years lost to chronic conditions
    alc_chr = uniform(0.80 * alc_chr, 1.20 * alc_chr)  # Range: =/- 20%
    alc_acu = np.random.randint(1300000, 1800000)  # alc_acu: Alcohol-attributable life years lost to acute conditions
    alc_acu = uniform(0.80 * alc_acu, 1.20 * alc_acu)  # Range: =/- 20%
    alc_m_chr = np.random.randint(350000,
                                  400000)  # alc_m_chr: Alcohol-attributable morbidity-related QALYs lost from chronic conditions
    alc_m_chr = uniform(0.60 * alc_m_chr, 1.40 * alc_m_chr)  # Range: =/- 40%
    alc_m_acu = np.random.randint(100000,
                                  120000)  # alc_m_acu: Alcohol-attributable morbidity-related QALYs lost from acute conditions
    alc_m_acu = uniform(0.60 * alc_m_acu, 1.40 * alc_m_acu)  # Range: =/- 40%
    alc_t_lost = alc_chr + alc_acu + alc_m_chr + alc_m_acu  # Total alcohol-attributable QALYs lost

    # calculating effects of screening
    alc_scr = uniform(0.02, 0.7)  # Delivery of screening and counseling
    alc_adh = uniform(0.2, 0.95)  # Adherence with screening
    alc_scr_eff = uniform(0.20, 0.85)  # Effectiveness of counseling at changing behaviour
    alc_eff_chr = uniform(0.65, 1)  # Efficacy of behaviour change at reducing chronic conditions
    alc_eff_acu = uniform(0.20, 0.80)  # Efficacy of behaviour change at reducing acute conditions
    alc_t_eff = 1 / alc_t_lost * (alc_eff_acu * (alc_acu + alc_m_acu) + alc_eff_chr * (alc_chr + alc_m_chr))
    # Weighted efficacy of behaviour change at reducing total alcohol-attributable QALYs lost
    # calculating quality adjusted life years lost and gained
    alc_y_lost = alc_t_lost / (1 - alc_scr * alc_scr_eff * alc_t_eff)  # Predicted alcohol-attributable QALYs lost
    alc_y_gain = alc_y_lost * alc_adh * alc_scr_eff * alc_t_eff  # QALYS gained, CPB
    alc.append(alc_y_gain)

alc_sorted = sorted(alc)


def cohort_alc(plt):
    """
    This function calculates the mean and standard deviation of quality adjusted life years to the cohort of 4,000,000
    population. It also plots histogram showing QALYs within the cohort over entire Monte Carlo Simulation bracket.
    lowerlimit:lower fixed quantile limit
    upperlimit: upper fixed quantile limit
    bins: fixed number of bins
    return: plt

    """

    lowerlimit = alc_sorted[int(0.025 * counts)]
    upperlimit = alc_sorted[int(0.975 * counts)]
    print("\nQALYS GAINED IN COHORT:\n")
    print("Mean for QALYs gained (CPB): " + str(int(np.mean(alc_sorted))))
    print("Standard deviation for QALYs gained (CPB): " + str(int(np.std(alc_sorted))))
    print("Confidence interval: [" + str(int(lowerlimit)) + ", " + str(int(upperlimit)) + "]")
    print("Number of simulations: " + str(len(alc_sorted)))

    # Build Histogram and Graph
    bins = np.arange(0, 1000000, 5000)  # fixed bin size
    plt.xlim([0, 600000])
    plt.xticks(range(0, 600000, 100000))
    plt.hist(alc_sorted, bins=bins, alpha=0.5)

    # Cohort calculations Graph
    plt.title('Histogram results')
    plt.xlabel('Cohort: Calculated QALYs for alcohol screening and intervention')
    plt.ylabel('Frequency (arb. units)')
    plt == plt.show()
    return plt


NI_alc = 206000000  # number of person years above 15 years old for a cohort of 4,000,000
alc_final = [i / NI_alc for i in alc_sorted]


def inter_alc(plt):
    """
    This function calculates the quality of life years gained per individual intervention taking into account
    all interventions and constructing confidence intervals, calculating the mean and standard deviation of years gained
    and plots histogram showing QALYs/intervention over entire Monte Carlo Simulation bracket.
    lowerlimit:lower fixed quantile limit
    upperlimit: upper fixed quantile limit
    bins: fixed number of bins
    return: plt

    """
    print("\n\nQALYS GAINED PER INDIVIDUAL INTERVENTION:\n")
    print("Number of interventions in the cohort: ", NI_alc)

    lowerlimit = alc_final[int(0.025 * counts)]
    upperlimit = alc_final[int(0.975 * counts)]

    print("Mean for QALYs gained (CPB): " + str((np.mean(alc_final))))
    print("Standard deviation for QALYs gained (CPB): " + str((np.std(alc_final))))
    print("Confidence interval: [" + str((lowerlimit)) + ", " + str((upperlimit)) + "]")
    print("Number of simulations: " + str(len(alc_final)))

    bins = np.arange(0, 0.0035, 0.000005)  # fixed bin size
    plt.xlim([0, 0.0035])
    plt.hist(alc_final, bins=bins, alpha=0.5)
    plt.title('Histogram results')
    plt.xlabel('Calculated QALYs/intervention')
    plt.ylabel('Frequency (arb. units)')
    plt == plt.show()
    return plt


alc_intervention_mean = np.mean(alc_final)
alc_intervention_stdev = np.std(alc_final)


# ===========================================
# IMPACT OF NGO INTERVENTION ON ALCOHOL
# ===========================================
def impact_alc():
    """
    This function calculates the mean quality adjusted life years for a period of three years after taking fluctuations
    of patient traffic into account and calculates the monetory value saved.
    Term1: previous year with patient fluctuation of 0.2
    Term2: current year patient volume
    Term3: next year patient volume with fluctuation of 0.2
    return: none
    >>>patient_volume=300
    >>>Fluctuation = 0.2
    >>>QALY_dollars = 132200
    Alcohol Mean QALYS/year:  0.41458903907
    Alcohol_Stdev_QALYS/year:  0.156845352146
    Monetary value (Mean):  41458.903907
    Monetary value (Stdev):  15684.5352146

    >>>patient_volume= 300
    >>>Fluctuation = 0
    >>>QALY_dollars = 100
    Alcohol Mean QALYS/year:  0.413815868588
    Alcohol_Stdev_QALYS/year:  0.156432947411
    Monetary value (Mean):  41.3815868588
    Monetary value (Stdev):  15.6432947411


    """
    # alc_patient_volume = np.random.randint(300,500)
    alc_patient_volume = 300  # number of patients interviened by the NGO
    Fluctuation = np.random.random()  # year on year patient traffic fluctuation
    QALY_dollars = np.random.randint(125000, 150000)  # QALYs converted to dollars

    QALYs_year_mean = alc_intervention_mean * alc_patient_volume
    # Var(AB)=Var(A)Var(B)+Var(A)Mean2(B)+Mean2(A)Var(B)
    Term1 = (alc_intervention_stdev * alc_patient_volume * Fluctuation) ** 2
    Term2 = (alc_intervention_stdev * alc_patient_volume) ** 2
    Term3 = (alc_intervention_mean * alc_patient_volume * Fluctuation) ** 2

    QALYs_year_stdev = (Term1 + Term2 + Term3) ** 0.5
    print("Impact of NGO:\n")
    print("Patients:", alc_patient_volume)
    print("Year on fluctuation:", Fluctuation)
    print("Monetary value of one QALY: ", QALY_dollars)
    print("Alcohol Mean QALYS/year: ", QALYs_year_mean)
    print("Alcohol_Stdev_QALYS/year: ", QALYs_year_stdev)
    print("Monetary value (Mean): ", QALYs_year_mean * QALY_dollars)
    print("Monetary value (Stdev): ", QALYs_year_stdev * QALY_dollars)
    print("At Adherence with screening of {0:.2f}".format(alc_adh * 100),
          "% and a behavior changefactor of {0:.2f}".format(alc_t_eff * 100), "%")
    print("Quality savings for individual per year {0:.2f}".format(QALYs_year_mean * QALY_dollars / alc_patient_volume),
          "Dollars for", counts, "simulations")


if __name__ == '__main__':
    """
    Call all functions.
    """

    print("\nCALCULATIONS FOR ALCOHOL INTERVENTION:\n")
    cohort_alc(plt)
    inter_alc(plt)
    impact_alc()



