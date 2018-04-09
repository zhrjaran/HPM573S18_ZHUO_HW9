
# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals

DELTA_T = 1       # years


# probability matrix of 4 state
PROB_MATRIX = [
    [0.75,  0.15,    0.0,    0.1],   # Well
    [0.0,   0.0,     1.0,    0.0],   # Stroke
    [0.0,   0.25,    0.55,  0.20],  # Post-Stroke
    [0.0,   0.0,     0.0,    1.0],# Dead
    ]

# treatment relative risk
TREATMENT_RR = 0.65
BLEEDING_RR= 1.05
