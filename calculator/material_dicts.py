#__author__ = 'Micah'
#
#PL = {
#			.007: .00001085	},
#			.008: .00001418,
#			.0085: .00001601,
#			.009: .00001794,
#			.0095: .00001999,
#			.010: .00002215,
#			.0105: .00002442,
#			.011: .00002680,
#			.0115: .00002930,
#			.012: .00003190,
#			.013: .00003744,
#			.0135: .00004037,
#			.014: .00004342,
#			.015: .00004984,
#			.016: .00005671,
#			.017: .00006402,
#			.018: .00007177,
#			.019: .00007997,
#			.020: .00008861,
#			.022: .00010722,
#			.024: .00012760,
#			.026: .00014975
#			};
#			double[][] PB = {
#			.020: .00008106,
#			.021: .00008944,
#			.022: .00009876,
#			.023: .00010801,
#			.024: .00011682,
#			.025: .00012686,
#			.026: .00013640,
#			.027: .00014834,
#			.029: .00017381,
#			.030: .00018660,
#			.032: .00021018,
#			.034: .00023887,
#			.035: .00025365,
#			.036: .00026824,
#			.039: .00031124,
#			.042: .00036722,
#			.045: .00041751,
#			.047: .00045289,
#			.049: .00049151,
#			.052: .00055223,
#			.053: .00056962,
#			.056: .00063477,
#			.059: .00070535
#			};
#			double[][] XS = {
#			.018: .00006153,
#			.020: .00007396,
#			.021: .00008195,
#			.022: .00009089,
#			.024: .00010742,
#			.026: .00012533,
#			.028: .00014471,
#			.030: .00017002,
#			.032: .00019052,
#			.034: .00021229,
#			.036: .00023535,
#			.038: .00025969,
#			.040: .00028995,
#			.042: .00031685,
#			.046: .00037449,
#			.048: .00040523,
#			.050: .00043726,
#			.052: .00047056,
#			.054: .00052667,
#			.056: .00056317,
#			.070: .00087444
#			};
#			double[][] NW = {
#			.017: .00005524,
#			.018: .00006215,
#			.019: .00006947,
#			.020: .00007495,
#			.021: .00008293,
#			.022: .00009184,
#			.024: .00010857,
#			.026: .00012671,
#			.028: .00014666,
#			.030: .00017236,
#			.032: .00019347,
#			.034: .00021590,
#			.036: .00023964,
#			.038: .00026471,
#			.039: .00027932,
#			.042: .00032279,
#			.044: .00035182,
#			.046: .00038216,
#			.048: .00041382,
#			.049: .00043014,
#			.052: .00048109,
#			.056: .00057598,
#			.059: .00064191,
#			.060: .00066542,
#			.062: .00070697,
#			.064: .00074984,
#			.066: .00079889,
#			.068: .00084614,
#			.070: .00089304,
#			.072: .00094124,
#			.074: .00098869,
#			.080: .00115011,
#		;
#			double[][] HR = {
#			.022: .00011271,
#			.024: .00013139,
#			.026: .00015224,
#			.030: .00019916,
#			.032: .00022329,
#			.036: .00027556,
#			.039: .00032045,
#			.042: .00036404,
#			.046: .00043534,
#			.052: .00054432,
#			.056: .00062758
#		;

PL = {.0085: .00001601,
      .008: .00001418,
      .007: .00001085}


def get_material_dict(string_material):
    if string_material == 'PL':
        return PL
