from policyengine_canada.model_api import *


class child_disability_benefit_children(Variable):
    value_type = int
    entity = Household
    label = "Children eligible for the Child Disability Benefit"
    definition_period = YEAR

    formula = sum_of_variables(["child_disability_benefit_eligible"])
