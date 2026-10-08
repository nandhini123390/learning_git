print("ESG Calculator")

def calculate_emission(activity, emission_factor):
    return activity * emission_factor

def calculate_electricity_emission(kwh, emission_factor):
    return kwh * emission_factor