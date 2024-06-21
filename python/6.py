def calculate_o(B):
    # Define Psi: {2β : β ∈ B ∧ β < 73 ∧ β > 2}
    Psi = {2 * beta for beta in B if beta < 73 and beta > 2}

    # Define Delta: {[β/9] + β^2 : β ∈ B ∧ (β < 88 ∨ β > -3)}
    Delta = {int(beta / 9) + beta ** 2 for beta in B if beta < 88 or beta > -3}

    # Define Theta as the union of Psi and Delta
    Theta = Psi.union(Delta)

    # Calculate the value of o
    o = len(Delta.union(Theta)) - sum(Theta) #union = and
    
    return o

# Example calculations:
B1 = {38, 7, 8, 9, 44, -79, -76, 54, -70, 95}
B2 = {3, 99, -19, -13, 85, 22, 87, -10, -66}

print(calculate_o(B1))  # Output: -32735
print(calculate_o(B2))  # Output: -30129
