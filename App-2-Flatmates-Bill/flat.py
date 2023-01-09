class Bill:
    """
    bill class, keeps record of bills, amount, duration
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates:
    """
    flatmates, keeps record of flatmates, bill, share, number of days in flat
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight

        return to_pay
