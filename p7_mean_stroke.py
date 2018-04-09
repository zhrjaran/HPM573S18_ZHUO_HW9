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

# graph histogram of number of strokes
Figs.graph_histogram(
    data=simOutputs.get_num_of_stroke(),
    title='Number of strokes of patients with Stroke ',
    x_label='Stroke numbers',
    y_label='Counts',
    bin_width=1
)
# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs, 'Without therapy:')

#############################################
# create a cohort with treatment
cohortwith = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.WITH)

# simulate the cohort
simOutputswith = cohortwith.simulate()

# graph histogram of number of strokes
Figs.graph_histogram(
    data=simOutputswith.get_num_of_stroke(),
    title='Number of strokes of patients with Stroke under treatment ',
    x_label='Stroke numbers',
    y_label='Counts',
    bin_width=1
)
# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputswith, 'With therapy:')