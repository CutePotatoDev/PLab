
class Constant():
    # Constants related to standard atmosphere.
    STD_TEMPERATURE = 15   # °C
    STD_TEMPERATURE_LAPSE_RATE = -0.0065    # K/m

    # Physical constants.
    UNIVERSAL_GAS_CONSTANT = 8.3144598  # N·m/(mol·K)
    GRAVITATIONAL_ACCELERATION = 9.80665    # m/s2
    AIR_MOLAR_MASS = 0.0289644  # kg/mol

    # NASA/TP-2006-213486
    # Notes on Earth Atmospheric Entry for Mars Sample Return Missions (Page: 20)
    EARTH_MEAN_RADIUS = 6356766     # m


class ICAOConst():
    # Standard acceleration due to gravity. It conforms with latitude 𝜑 = 45°32'33"
    # using Lambert’s equation of the acceleration due to gravity as a function of latitude 𝜑.
    g_0 = 9.80665    # m/s^2

    # Sea level mean molar mass, as obtained from the perfect gas law when introducing the
    # primary constants P0, ρ0, T0, R*
    M_0 = 28.964420     # kg/kmol

    # Avogadro constant.
    N_A = 602.257e24  # kmol

    # Sea level atmospheric pressure.
    P_0 = 101.325e3   # Pa

    # Universal gas constant.
    R_ast = 8314.32  # J/(K * kmol) or kg * m^2/(s^2 * K * kmol)

    # Specific gas constant.
    R = 287.05287   # J/(K * kg) or m^2/(K * s^2)

    # Sutherland’s empirical constants in the equation for dynamic viscosity.
    S = 110.4   # K
    Beta_S = 1.458e6  # kg/(m * s * K^(1/2))

    # Temperature of the ice point at mean sea level.
    T_i = 273.15    # K

    # Sea level temperature.
    T_0 = 288.15    # K

    # Celsius temperature of the ice point at mean sea level.
    t_i = 0.0    # °C

    # Celsius sea level temperature.
    t_0 = 15.0  # °C

    # Adiabatic index, the ratio of the specific heat of air at constant pressure to its specific heat at constant volume.
    Kappa = 1.4

    # Sea level atmospheric density.
    rho_0 = 1.225   # kg/m^3

    # Effective collision diameter of an air molecule, taken as constant with altitude.
    sigma = 0.365e-9  # m

    # Nominal earth’s radius.
    r = 6356766     # m


def celciusToKelvin(temp):
    return temp + 273.15

def kelvinToCelcius(temp):
    return temp - 273.15

def mBarTohPa(val):
    return val


def inHgTohPA(val):
    return val * 33.8639


def PaTohPa(val):
    """ Convert Pascals to Hectopascals.
    val     (float): Atmospheric pressure in Pascals.
    """
    return val / 100
