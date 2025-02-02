from policyengine_canada.model_api import *


class child_benefit_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Children eligible for Canada Child Benefit"
    definition_period = YEAR

    formula = sum_of_variables(["child_benefit_eligible"])
