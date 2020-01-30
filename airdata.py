import utils
from utils import Constant as const


class ADC():
    def __init__(self, initpres=1013.25, staticpres=1013.25, temperature=15):
        self._initpres = initpres
        self._staticpres = staticpres

        self._temperature = temperature

    # Barometric latitude formula.
    # ip - Initial pressure (hPa).
    # cp - Current pressure (hPa).
    # temp - temperature (Kelvin).
    def _barometricFormula(self, ip, cp, temp):
        # Basically adapted Hypersometric formula.
        # http://asciimath.org/
        # h = ((((P_(0))/P)^(1/5.257) - 1) * (T + 273.15)) / 0.0065

        sq = (const.GRAVITATIONAL_ACCELERATION * const.AIR_MOLAR_MASS) / (const.UNIVERSAL_GAS_CONSTANT * const.STD_TEMPERATURE_LAPSE_RATE)
        sq = 1 / sq * -1

        fu = (((ip / cp) ** sq) - 1) * temp

        return fu / const.STD_TEMPERATURE_LAPSE_RATE * -1

    def updateStaticPreasure(self, val):
        self._staticpres = val

    # Indicated altitude, refers to the measurement indicated on the altimeter in aircraft.
    # An altimeter measures the atmospheric pressure at the aircraft’s flight altitude and
    # then compares it to the pressure value set by the pilot.
    @property
    def indicatedAlt(self):
        return self._barometricFormula(self._initpres, self._staticpres, utils.celciusToKelvin(const.STD_TEMPERATURE))

    # This is the altitude of the aircraft above the standard datum plane, the theoretical
    # location where at 15 degrees Celsius the altimeter setting will equal 29.92 inches of
    # mercury.
    # All aircraft flying above 18,000 feet MSL are required to set their altimeters to 29.92
    # inches Hg. This means that all aircraft flying in the flight levels will have the same
    # altimeter setting.
    @property
    def preasureAlt(self):
        # 29.92 Hg = 1013.2 hPa
        return self._barometricFormula(utils.inHgTohPA(29.92), self._staticpres, utils.celciusToKelvin(const.STD_TEMPERATURE))

    # Density altitude is pressure altitude corrected for non-standard temperature.
    @property
    def densityAlt(self):
        return self._barometricFormula(utils.inHgTohPA(29.92), self._staticpres, utils.celciusToKelvin(self._temperature))
    