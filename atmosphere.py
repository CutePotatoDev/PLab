from utils import ICAOConst as con
import math


class ICAOAtmosphere():
    # Temperatures and vertical temperature gradients.
    # Geopotential altitude - H.
    # Temperature - T.
    # Temperature gradient - β.
    LAYERS = [
        {"H": -5.00e3, "T": 320.65, "β": -6.50e-3, "p": 1.77687e5, "name": "Troposphere"},
        {"H": 0.00e3, "T": 288.15, "β": -6.50e-3, "p": 1.01325e5, "name": "Troposphere"},
        {"H": 11.00e3, "T": 216.65, "β": 0.00e-3, "p": 2.26320e4, "name": "Tropopause"},
        {"H": 20.00e3, "T": 216.65, "β": 1.00e-3, "p": 5.47487e3, "name": "Stratosphere"},
        {"H": 32.00e3, "T": 228.65, "β": 2.80e-3, "p": 8.68014e2, "name": "Stratosphere"},
        {"H": 47.00e3, "T": 270.65, "β": 0.00e-3, "p": 1.10906e2, "name": "Stratopause"},
        {"H": 51.00e3, "T": 270.65, "β": -2.80e-3, "p": 6.69384e1, "name": "Mesosphere"},
        {"H": 71.00e3, "T": 214.65, "β": -2.00e-3, "p": 3.95639e0, "name": "Mesosphere"},
        {"H": 80.00e3, "T": 196.65, "β": -2.00e-3, "p": 8.86272e-1, "name": "Mesosphere"},
    ]

    def __init__(self):
        self._h = 0     # Geometric altitude.
        self._H = 0     # Geopotential altitude.
        self._T = 0     # Temperature.

    def _getLayerParams(self, H):
        """ Get atmosphere layer data by given geopotential altitude.
        H     (float): Geopotential altitude (height).
        """

        if H < -5.00e3:
            return ICAOAtmosphere.LAYERS[0]

        layer = list(filter(lambda x: x["H"] <= H, ICAOAtmosphere.LAYERS))[-1]
        return layer

    @property
    def geomAltitude(self):
        return self._h

    @geomAltitude.setter
    def geomAltitude(self, val):
        self._h = val
        self._H = self.geomHTogeopH(val)

    @property
    def geopAltitude(self):
        return self._H

    @geopAltitude.setter
    def geopAltitude(self, val):
        self._H = val
        self._h = self.geopHTogeomH(val)

    def geomHTogeopH(self, alt):
        """ Convert geometric height to geopotential height.
        alt     (float): Geometric altitude (height), altitude from see level.
        """
        return (con.r * alt) / (con.r + alt)

    def geopHTogeomH(self, alt):
        """ Convert geopotential height to geometric height.
        alt     (float): Geopotential altitude (height).
        """
        return (con.r * alt) / (con.r - alt)

    @property
    def pressure(self):
        """ Pressure on current geopotential altitude.
        """
        H_b, T_b, beta, p_b, _ = self._getLayerParams(self._H).values()

        if beta == 0.0:
            return p_b * math.exp(-(con.g_0 / con.R * self._T) * (self._H - H_b))
        else:
            return p_b * (1 + (beta / T_b) * (self._H - H_b)) ** -(con.g_0 / (beta * con.R))

    @property
    def density(self):
        """ Density on current geopotential altitude.
        """
        return self.pressure / (con.R * self._T)
    