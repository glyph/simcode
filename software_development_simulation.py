
from characteristic import attributes


@attributes(['created', 'last_modified'])
class Block(object):
    """
    A block of PsyLisp code.

    (You can think of this sort of like a "line" but it is intentionally
    somewhat vaguer than a "line" of code so we don't get bogged down in
    discussions of the limitations of SLOC as a metric.)
    """



@attributes(['implemented_features', 'defects', 'blocks'])
class Program(object):
    """
    A L{Program} is some code.
    """



@attributes(['program', 'time_to_exercise', 'implemented_at', 'specification'])
class Feature(object):
    """
    A Feature is an attribute of a L{Program} which is useful to a user in some
    way.
    """



@attributes(['estimated_completion'])
class Specification(object):
    """
    A specification is a description of a L{Feature} or a fix for a L{Defect};
    a unit of work for a L{Programmer} to perform.
    """




@attributes(['program', 'introduced_on', 'affects_blocks'])
class Defect(object):
    """
    A L{Defect} in a L{Program} degrades its functionality and impedes a
    L{User} trying to exercise a L{Feature}.
    """
    # How do I represent that a defect might be reintroduced?



@attributes(['blocks_exercised', 'features_validated',
             'defects_regressed', 'time_to_run'])
class AutomatedTest(object):
    """
    An automated test.
    """



@attributes(['blocks_per_hour', 'defects_per_block'])
class Programmer(object):
    """
    A L{Programmer} modifies a L{Program}.
    """

    def implement(self, when, specification):
        """
        Implement a L{Specification} at the given time.
        """

