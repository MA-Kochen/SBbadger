
import os

from processRNG import runRNG
from math import exp
from scipy.special import zeta
from buildNetworks import Settings
Settings.addDegradationSteps = True


def in_dist(k):
    return k**(-2) / zeta(2)


def out_dist(k):
    return k**(-2) / zeta(2)


if __name__ == "__main__":

    runRNG(
        group_name='test_group',
        # output_dir=<your directory here>),
        overwrite=True,
        n_models=10,
        n_species=10,
        # cut_off=0.5,

        # in_dist=in_dist,
        # out_dist=out_dist,
        # verbose_exceptions=True,

        # add_E=True,

        kinetics=['mass_action', 'trivial', ['kf', 'kr', 'kc', 'deg']],
        # kinetics=['mass_action', 'uniform', ['kf', 'kr', 'kc'], [[0.0, 100], [0.0, 100], [0.0, 100]]],
        # kinetics=['mass_action', 'loguniform', ['kf', 'kr', 'kc', 'deg'], [[0.01, 100], [0.01, 100], [0.01, 100], [0.01, 100]]],
        # kinetics=['mass_action', 'norm', ['kf', 'kr', 'kc'], [[1, 1], [1, 1], [1, 1]]],
        # kinetics=['mass_action', 'lognorm', ['kf', 'kr', 'kc'], [[exp(1), 1], [exp(1), 1], [exp(1), 1]]],

        # kinetics=['mass_action', 'uniform', ['kf0', 'kr0', 'kc0', 'kf1', 'kr1', 'kc1',
        #                                      'kf2', 'kr2', 'kc2', 'kf3', 'kr3', 'kc3'],
        #           [[0.0, 100], [0.0, 100], [0.0, 100], [0.0, 100], [0.0, 100], [0.0, 100],
        #            [0.0, 100], [0.0, 100], [0.0, 100], [0.0, 100], [0.0, 100], [0.0, 100]]],

        # kinetics=['mass_action', 'loguniform', ['kf0', 'kr0', 'kc0', 'kf1', 'kr1', 'kc1',
        #                                         'kf2', 'kr2', 'kc2', 'kf3', 'kr3', 'kc3', 'deg'],
        #           [[0.01, 100], [0.01, 100], [0.01, 100], [0.01, 100], [0.01, 100], [0.01, 100],
        #            [0.01, 100], [0.01, 100], [0.01, 100], [0.01, 100], [0.01, 100], [0.01, 100], [0.01, 100]]],

        # kinetics=['mass_action', 'norm', ['kf0', 'kr0', 'kc0', 'kf1', 'kr1', 'kc1',
        #                                   'kf2', 'kr2', 'kc2', 'kf3', 'kr3', 'kc3'],
        #            [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
        #             [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]],

        # kinetics=['mass_action', 'lognorm', ['kf0', 'kr0', 'kc0', 'kf1', 'kr1', 'kc1',
        #                                      'kf2', 'kr2', 'kc2', 'kf3', 'kr3', 'kc3'],
        #            [[exp(1), 1], [exp(1), 1], [exp(1), 1], [exp(1), 1], [exp(1), 1], [exp(1), 1],
        #             [exp(1), 1], [exp(1), 1], [exp(1), 1], [exp(1), 1], [exp(1), 1], [exp(1), 1]]],

        # kinetics=['hanekom', 'trivial', ['v', 'k', 'keq']],
        # kinetics=['hanekom', 'uniform', ['v', 'k', 'keq'], [[0.0, 100], [0.0, 100], [0.0, 100]]],
        # kinetics=['hanekom', 'loguniform', ['v', 'k', 'keq'], [[0.01, 100], [0.01, 100], [0.01, 100]]],
        # kinetics=['hanekom', 'normal', ['v', 'k', 'keq'], [[1, 1], [1, 1], [1, 1]]],
        # kinetics=['hanekom', 'lognormal', ['v', 'k', 'keq'], [[exp(1), 1], [exp(1), 1], [exp(1), 1]]],

        # kinetics=['hanekom', 'trivial', ['v', 'ks', 'kp', 'keq', 'deg']],
        # kinetics=['hanekom', 'uniform', ['v', 'ks', 'kp', 'keq'], [[0.0, 100], [0.0, 100], [0.0, 100], [0.0, 100]]],
        # kinetics=['hanekom', 'loguniform', ['v', 'ks', 'kp', 'keq'], [[0.01, 100], [0.01, 100], [0.01, 100], [0.01, 100]]],
        # kinetics=['hanekom', 'normal', ['v', 'ks', 'kp', 'keq'], [[1, 1], [1, 1], [1, 1], [1, 1]]],
        # kinetics=['hanekom', 'lognormal', ['v', 'ks', 'kp', 'keq'], [[exp(1), 1], [exp(1), 1], [exp(1), 1], [exp(1), 1]]],

        # the reference reaction rate 'v' is drawn from the provided distribution while the reference concentrations are
        # always drawn from the uniform distribution with the provided range.
        # kinetics=['lin_log', 'trivial', ['v', 'hs']],
        # kinetics=['lin_log', 'uniform', ['v', 'hs'], [[0.0, 100], [0.0, 100]]],
        # kinetics=['lin_log', 'loguniform', ['v', 'hs'], [[0.01, 100], [0.0, 100]]],
        # kinetics=['lin_log', 'normal', ['v', 'hs'], [[1, 1], [0.0, 100]]],
        # kinetics=['lin_log', 'lognormal', ['v', 'hs'], [[exp(1), 1], [0.0, 100]]],

        # "rev_prob" is currently only valid for mass-action and lin-log kinetics.
        # It is ignored if hanekom is specified.
        # rev_prob=[0, 0, 0, 0],
        rev_prob=[0.5, 0.5, 0.5, 0.5],
        # rev_prob=[1, 1, 1, 1],

        # rxn_prob=[1.0, 0.0, 0.0, 0.0],
        # rxn_prob=[0.0, 1.0, 0.0, 0.0],
        # rxn_prob=[0.0, 0.0, 1.0, 0.0],
        # rxn_prob=[0.0, 0.0, 0.0, 1.0],
        rxn_prob=[0.25, 0.25, 0.25, 0.25],

        ic_params='trivial'
        # ic_params=['dist', 0, 10],
        # ic_params=['list', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    )
