from policyengine_canada.model_api import *


class on_child_care_fee_subsidy(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Care Fee Subsidy"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        province = household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        reduction = household("on_child_care_fee_subsidy_reduction", period)
        full_time = household("full_time_childcare", period)
        full_time_care = household(
            "on_child_care_fee_subsidy_full_time", period
        )
        part_time_care = household(
            "on_child_care_fee_subsidy_part_time", period
        )
        return max_(
            0,
            (
                in_ontario * where(full_time, full_time_care, part_time_care)
                - reduction
            ),
        )
