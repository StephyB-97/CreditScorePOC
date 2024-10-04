# models.py

class Customer:
    def __init__(self, name, debt, income, credit_score, payment_history):
        self.name = name
        self.debt = debt
        self.income = income
        self.credit_score = credit_score
        self.payment_history = payment_history  # This could be a list of payments

    def calculate_debt_to_income_ratio(self):
        return self.debt / self.income if self.income > 0 else 0

    def get_credit_score_category(self):
        if self.credit_score >= 800:
            return "EXCELLENT"
        elif self.credit_score >= 740:
            return "VERY GOOD"
        elif self.credit_score >= 670:
            return "GOOD"
        elif self.credit_score >= 580:
            return "FAIR"
        else:
            return "POOR"