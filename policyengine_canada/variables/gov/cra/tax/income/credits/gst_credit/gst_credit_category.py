from policyengine_canada.model_api import *


class GSTCreditCategory(Enum):
    HEAD = "Head"
    SPOUSE = "Spouse"
    CHILD = "Child"


class gst_credit_category(Variable):
    value_type = Enum
    entity = Person
    possible_values = GSTCreditCategory
    default_value = GSTCreditCategory.HEAD
    definition_period = YEAR

    def formula(person, period, parameters):
        return select(
            [
                person("is_head", period),
                person("is_spouse", period),
                person(
                    "is_eldest_child_in_single_household_for_gst_credit",
                    period,
                ),
                person("is_child_for_gst_credit", period)
                & ~person(
                    "is_eldest_child_in_single_household_for_gst_credit",
                    period,
                ),
            ],
            [
                GSTCreditCategory.HEAD,
                GSTCreditCategory.SPOUSE,
                GSTCreditCategory.SPOUSE,
                GSTCreditCategory.CHILD,
            ],
            default=0,
        )
