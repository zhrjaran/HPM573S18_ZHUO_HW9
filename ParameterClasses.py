from enum import Enum
import numpy as np
import scipy.stats as stat
import math as math
import InputData as Data
import scr.MarkovClasses as MarkovCls
import scr.RandomVariantGenerators as Random
import scr.ProbDistParEst as Est


class HealthStats(Enum):
    """ health states of patients with HIV """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    DEAD = 3


class Therapies(Enum):
    """ without vs. with therapy """
    WITHOUT = 0
    WITH = 1


class _Parameters:

    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL

        # transition probability matrix of the selected therapy
        self._prob_matrix = []
        # treatment relative risk
        self._treatmentRR = 0
        self._bleedingRR = 0


    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]


class ParametersFixed(_Parameters):
    def __init__(self, therapy):

        # initialize the base class
        _Parameters.__init__(self, therapy)

        # calculate transition probabilities between stroke states
        self._prob_matrix = calculate_prob_matrix()

        # update the transition probability matrix if combination therapy is being used
        if self._therapy == Therapies.WITH:
            # treatment relative risk
            self._treatmentRR = Data.TREATMENT_RR
            self._bleedingRR = Data.BLEEDING_RR
            # calculate transition probability matrix for the combination therapy
            self._prob_matrix = calculate_prob_matrix_combo(
                matrix_without=self._prob_matrix, treat_rr=Data.TREATMENT_RR,
                bleed_rr= Data.BLEEDING_RR)

def calculate_prob_matrix():
    """ :returns transition probability matrix for hiv states under mono therapy"""

    # create an empty matrix populated with zeroes
    prob_matrix = []
    for s in HealthStats:
        prob_matrix.append([0] * len(HealthStats))
        prob_matrix[s.value][:] = Data.PROB_MATRIX[s.value][:]

    return prob_matrix


def calculate_prob_matrix_combo(matrix_without, treat_rr, bleed_rr):
    """
        :param matrix_without: (list of lists) transition probability matrix under without therapy
        :param treat_rr: relative risk of treatment
        :returns (list of lists) transition probability matrix under therapy """

    # create an empty list of lists
    matrix_with = []

    for l in matrix_without:
         matrix_with.append([0] * len(l))

        # populate the with matrix
    for s in HealthStats:
        if s in [HealthStats.POST_STROKE]:
            matrix_with[s.value][s.value-1] = treat_rr * matrix_without[s.value][s.value-1]
            matrix_with[s.value][s.value+1] = treat_rr * bleed_rr * matrix_without[s.value][s.value+1]
            matrix_with[s.value][s.value] = 1 - (matrix_with[s.value][s.value - 1]+
                                                matrix_with[s.value][s.value + 1])
        else:
            matrix_with[s.value][:] = matrix_without[s.value][:]

    return matrix_with




#print(calculate_prob_matrix())
#print(calculate_prob_matrix_combo(Data.PROB_MATRIX, Data.TREATMENT_RR, Data.BLEEDING_RR))