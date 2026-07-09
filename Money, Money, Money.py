def calculate_years(principal, interest_rate, tax_rate, desired):
    years = 0
    # Continue looping as long as the current principal is less than the desired sum
    while principal < desired:
        # 1. Calculate interest earned this year
        yearly_interest = principal * interest_rate
        
        # 2. Calculate tax on that interest
        # (Only the year's accrued interest is taxed, not the principal)
        tax_on_interest = yearly_interest * tax_rate
        
        # 3. Update principal by adding net interest (after tax)
        principal += (yearly_interest - tax_on_interest)
        
        # 4. Increment the year counter
        years += 1
        
    return years

# Example usage:
# P = 1000.00, I = 0.05, T = 0.18, D = 1100.00
# Result should be 3
print(calculate_years(1000.00, 0.05, 0.18, 1100.00))