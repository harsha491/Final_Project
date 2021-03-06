

# Title: Monte Carlo Intervension

## Team Member(s): harsha491


# Monte Carlo Simulation Scenario & Purpose:
(be sure to read the instructions given in course Moodle)

The purpose of this project is to simulate the health impact and savings a small NGO serving 300-500 people can have through simple interventions and counseling for clinically preventable diseases over a period of three years.
After comments on moodle I also tried in to factor individual health care costs for a variable percentage of intervention level and a lariable percentage of effectiveness or adherence to the intervention.

## Simulation's variables of uncertainty

Number of people visiting the NGO for health related issues

Fluctuations year on year for three years

Clinically Preventable Disease vulnerability

Possible chronic or acute side effects of the existing condition

Effectiveness of Intervention

Long term adherence to intervention


## Hypothesis or hypotheses before running the simulation:

Simple intervensions of clinically preventable diseases can have a lasting impact on quality of life and save thousands of dollars in health care.
My results have proved that there is a considerable health care cost saved with simple health interventions. An individual can save between $100-$1000 a year by adhering to councelling on Alcohol and over $1000 a year in health care costs calculated based on the quality of adjusted life years by keeping away from smoking. 

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

The program is intended to look at health care costs an NGO would be able to save by converting the quality adjusted life years of interventions on alcohol consumption and smoking. For this purpose the program considers the NGO serves anywhere between 300-500 patients a year with a random fluctuation over three year period. The mean has been calculated for a cohort of 4,000,000 population and health care effects and loss to chronic and acute diseases have been factored in using existing literature over clinically preventable burden.

For a random Monte Carlo simulation the results for alchol intervention are as follows:

Patients: 406
Year on fluctuation: 0.14802505875409966
Monetary value of one QALY:  147880

Alcohol Mean QALYS/year:  1.18551115266

Alcohol_Stdev_QALYS/year:  0.799210074467

Monetary value (Mean):  175313.389255

Monetary value (Stdev):  118187.185812

At Adherence with screening of 23.30 % and a behavior change factor of 75.39 %, average quality savings for individual per year 431.81 Dollars for 100000 simulations


This gives and idea on how muc a small Non-Government Organization or a primary health care centre can save in health care costs and benefet the quality of life of people through simple interventions.
An NGO working in public health could take up clinically preventable burdens (smoking, alcohol, hiv, influenza, hypertension, and many more) more vigorously and save thousands of dollars on an average every year in health care costs and improve quality of life.

the code was adjusted multiple times to get closer to literature available on CPBs and WHO metrics. The code was also modified in order to see impacts on individual health care.



## Instructions on how to use the program:
Run the file Alcohol to find simulated results for cohort, individual intervention, related histograms, impact of the NGO and impact on individual health care cost.
Run the file Tobacco to find simulated results for cohort, individual intervention, related histograms, impact of the NGO and impact on individual health care cost.

### Modify values in Alcohol to simulate for various outcomes :
alc_chr: Alcohol-attributable life years lost to chronic conditions and Range: =/- 20%

alc_acu: Alcohol-attributable life years lost to acute conditions and Range: =/- 20%

alc_m_chr: Alcohol-attributable morbidity-related QALYs lost from chronic conditions

alc_m_acu: Alcohol-attributable morbidity-related QALYs lost from acute conditions

alc_scr: Delivery of screening and counseling

alc_adh: Adherence with screening

alc_scr_eff: Effectiveness of counseling at changing behaviour

alc_eff_chr: Efficacy of behaviour change at reducing chronic conditions

alc_eff_acu: Efficacy of behaviour change at reducing acute conditions

alc_t_eff: Weighted efficacy of behaviour change at reducing total alcohol-attributable QALYs lost

alc_patient_volume: number of patients interviened by the NGO

Fluctuation: year on year patient traffic fluctuation

QALY_dollars: QALYs converted to dollars



### Modify values in Tobacco to simulate for various outcomes :
frm_sm: Portion of ever-smokers who are former smokers

rel_rsk: Relative risk of smoking disease for former smokers compared to current

beh_ch =  change in behavior

ff_sm: Long-term effectiveness of counseling inducing quits

patient_volume: number of patients interviened by the NGO

Fluctuation: year on year patient traffic fluctuation

QALY_dollars: QALYs converted to dollars





## All Sources Used:
https://academic.oup.com/heapol/article/21/5/402/578296
https://www.cdc.gov/nchs/data/nvsr/nvsr65/nvsr65_08.pdf
http://prevent.org/data/files/initiatives/smokingcessationadviceandhelptoquit.pdf
http://www.prevent.org/data/files/initiatives/alcohol%20misuse%20screening%20and%20behavioral%20counseling.pdf
https://en.wikipedia.org/wiki/Quality-adjusted_life_year

