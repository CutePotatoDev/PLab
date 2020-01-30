import utils
import airdata
import atmosphere

# adc = airdata.ADC()

# print(adc.indicatedAlt)
# adc.updateStaticPreasure(900)

# print(adc.indicatedAlt)
# print(adc.preasureAlt)

# print(utils.ICAOConst.g0)

atm = atmosphere.ICAOAtmosphere()

# print(atm.geomHTogeopH(10000))
# print(atm.geopHTogeomH(9984.293438772525))
# print(atm._getLayerParams(11000))

atm.geomAltitude = 5500
atm._T = 252.43
print(atm.pressure)
print(atm.density)
