def calculate_credit_score(income, debt):
    """Calculate credit score based on total income and debt."""
    dti = (debt / income) * 100 if income > 0 else 0  # Calculate Debt-to-Income Ratio (DTI)

    # Determine credit score based on DTI
    if dti < 20:
        return 800  # Excellent
    elif dti < 30:
        return 740  # Very Good
    elif dti < 40:
        return 670  # Good
    elif dti < 50:
        return 580  # Fair
    else:
        return 300  # Poor
