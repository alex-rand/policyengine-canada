from policyengine_canada.model_api import *


class non_refundable_tax_credits(Variable):
    value_type = float
    entity = Household
    label = "Non-refundable tax credits"
    unit = CAD
    definition_period = YEAR

    formula = sum_of_variables("gov.cra.tax.income.credits.non_refundable")
