from enum import Enum


class CostingMethod(Enum):
    FIFO = 'First in First Out'
    SPECIFIC = 'Specific Identifaction Method'


costing_methods_as_choices = [(c.name, c.value) for c in CostingMethod]
