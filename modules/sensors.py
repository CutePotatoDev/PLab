import abc


class Sensor(abc.ABC):
    """ Base sensor class, contains only 'value' variable
        and it's setter and getter.
    """
    def __init__(self, vcc=5, value=0):
        self._vcc = vcc
        self._gnd = 0
        self._value = value

    @property
    def vcc(self):
        return self._vcc

    @vcc.setter
    def vcc(self, vcc):
        self._vcc = vcc

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    @abc.abstractmethod
    def out(self):
        pass


class TMP35(Sensor):
    @property
    def out(self):
        temperature = self._value

        vout = 0.001 * temperature

        # Set boundries of sensor.
        if vout < 0.01:
            vout = 0.01
        elif vout > 2:
            vout = 2

        if vout > self._vcc:
            vout = self._vcc

        return vout
