import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort without treatment
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.WITHOUT)

# simulate the cohort
simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients with Stroke',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs, 'Without therapy:')


########################################################
# create a cohort with treatment
cohortwith = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.WITH)

# simulate the cohort
simOutputswith = cohortwith.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputswith.get_survival_curve(),
    title='Survival curve with Treatment',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputswith.get_survival_times(),
    title='Survival times of patients with Stroke receive treatment',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputswith, 'With therapy:')