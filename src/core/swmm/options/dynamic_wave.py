﻿from enum import Enum

from core.inputfile import Section
from core.metadata import Metadata


class InertialDamping(Enum):
    """Options for inertial damping"""
    NONE = 1
    PARTIAL = 2
    FULL = 3


class NormalFlowLimited(Enum):
    """Condition to be checked for supercritical flow"""
    SLOPE = 1
    FROUDE = 2
    BOTH = 3


class ForceMainEquation(Enum):
    """Equation to be used for friction losses"""
    H_W = 1
    D_W = 2


class DynamicWave(Section):
    """SWMM Dynamic Wave Options"""

    SECTION_NAME = "[OPTIONS]"

    #     attribute,             input_name,            label,               default, english, metric, hint
    metadata = Metadata((
        ("inertial_damping",    "INERTIAL_DAMPING",    "Inertial Damping"),
        ("normal_flow_limited", "NORMAL_FLOW_LIMITED", "Normal Flow Limited"),
        ("force_main_equation", "FORCE_MAIN_EQUATION", "Force Main Equation"),
        ("variable_step",       "VARIABLE_STEP",       "Variable Step",        "0.0", "sec", "sec"),
        ("lengthening_step",    "LENGTHENING_STEP",    "Lengthening Step",     "0.0", "sec", "sec"),
        ("min_surface_area",    "MIN_SURFAREA",        "Minimum Surface Area", "0.0"),
        ("max_trials",          "MAX_TRIALS",          "Maximum Trials",       "8"),
        ("head_tolerance",      "HEAD_TOLERANCE",      "Head Tolerance",     "0.005", "ft",  "m"),
        ("minimum_step",        "MINIMUM_STEP",        "Minimum Step",         "0.5", "sec", "sec"),
        ("threads",             "THREADS",             "Threads")))
    """Mapping between attribute name and name used in input file"""

    def __init__(self):
        Section.__init__(self)

        self.inertial_damping = InertialDamping.NONE
        """
        How the inertial terms in the Saint Venant momentum equation
        will be handled under dynamic wave flow routing
        """

        self.normal_flow_limited = NormalFlowLimited.BOTH
        """
        Which condition is checked to determine if flow in a conduit
        is supercritical and should thus be limited to the normal flow
        """

        self.force_main_equation = ForceMainEquation.H_W
        """
        Establishes whether the Hazen-Williams (H-W) or the Darcy-Weisbach (D-W) equation will be used to
        compute friction losses for pressurized flow in conduits that have been assigned a Circular Force
        Main cross-section shape. The default is H-W.
        """

        self.lengthening_step = ''
        """
        Time step, in seconds, used to lengthen conduits under 
        dynamic wave routing, so that they meet the 
        Courant stability criterion under full-flow conditions
        """

        self.variable_step = ''
        """
        Safety factor applied to a variable time step computed for each
        time period under dynamic wave flow routing
        """

        self.min_surface_area = ''
        """
        Minimum surface area used at nodes when computing 
        changes in water depth under dynamic wave routing
        """

        self.max_trials = ''
        """
        The maximum number of trials allowed during a time step to reach convergence
        when updating hydraulic heads at the conveyance system’s nodes. The default value is 8.
        """

        self.head_tolerance = ''
        """
        Difference in computed head at each node between successive trials below
        which the flow solution for the current time step is assumed to have converged.
        The default tolerance is 0.005 ft (0.0015 m).
        """

        self.minimum_step = ''
        """
        Smallest time step allowed when variable time steps are used for dynamic
        wave flow routing. The default value is 0.5 seconds.
        """

        self.threads = ''
        """
        Number of parallel computing threads to use for dynamic wave flow routing
        on machines equipped with multi-core processors.
        """
