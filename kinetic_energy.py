# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def calculate_kinetic_energy(mass, distance, time):
    distance_in_km = distance.value
    distance_unit = distance.unit
    
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit
            distance_in_km = distance.value * 9.461e12
            distance_unit = "km"
        else:
            print ("unit is Unknown")
            return
    
    speed = distance_in_km/time # [km per sec]
    
    mass_in_kg = mass.value
    mass_unit = mass.unit
    
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            mass_in_kg = mass.value * 1.98892e30 # [kg]
            mass_unit = 'kg'
        else:
            print ("unit is Unknown")
            return

    kinetic_energy = 0.5 * mass_in_kg * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))