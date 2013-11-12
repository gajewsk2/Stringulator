__author__ = 'Micah'

PL = {
    .026: .00014975,
    .024: .00012760,
    .022: .00010722,
    .020: .00008861,
    .019: .00007997,
    .018: .00007177,
    .017: .00006402,
    .016: .00005671,
    .015: .00004984,
    .014: .00004342,
    .0135: .00004037,
    .013: .00003744,
    .012: .00003190,
    .0115: .00002930,
    .011: .00002680,
    .0105: .00002442,
    .010: .00002215,
    .0095: .00001999,
    .009: .00001794,
    .0085: .00001601,
    .008: .00001418,
    .007: .00001085}

PB = {
    .059: .00070535,
    .056: .00063477,
    .053: .00056962,
    .052: .00055223,
    .049: .00049151,
    .047: .00045289,
    .045: .00041751,
    .042: .00036722,
    .039: .00031124,
    .036: .00026824,
    .035: .00025365,
    .034: .00023887,
    .032: .00021018,
    .030: .00018660,
    .029: .00017381,
    .027: .00014834,
    .026: .00013640,
    .025: .00012686,
    .024: .00011682,
    .023: .00010801,
    .022: .00009876,
    .021: .00008944,
    .020: .00008106
}


XS = {
    .070: .00087444,
    .056: .00056317,
    .054: .00052667,
    .052: .00047056,
    .050: .00043726,
    .048: .00040523,
    .046: .00037449,
    .042: .00031685,
    .040: .00028995,
    .038: .00025969,
    .036: .00023535,
    .034: .00021229,
    .032: .00019052,
    .030: .00017002,
    .028: .00014471,
    .026: .00012533,
    .024: .00010742,
    .022: .00009089,
    .021: .00008195,
    .020: .00007396,
    .018: .00006153
}

NW = {
    .080: .00115011,
    .074: .00098869,
    .072: .00094124,
    .070: .00089304,
    .068: .00084614,
    .066: .00079889,
    .064: .00074984,
    .062: .00070697,
    .060: .00066542,
    .059: .00064191,
    .056: .00057598,
    .052: .00048109,
    .049: .00043014,
    .048: .00041382,
    .046: .00038216,
    .044: .00035182,
    .042: .00032279,
    .039: .00027932,
    .038: .00026471,
    .036: .00023964,
    .034: .00021590,
    .032: .00019347,
    .030: .00017236,
    .028: .00014666,
    .026: .00012671,
    .024: .00010857,
    .022: .00009184,
    .021: .00008293,
    .020: .00007495,
    .019: .00006947,
    .018: .00006215,
    .017: .00005524
}

HR = {
    .056: .00062758,
    .052: .00054432,
    .046: .00043534,
    .042: .00036404,
    .039: .00032045,
    .036: .00027556,
    .032: .00022329,
    .030: .00019916,
    .026: .00015224,
    .024: .00013139,
    .022: .00011271
}


def get_material_dict(string_material):
    """
    used to retrieve one of the hardcoded dictionaries;
    the dictionaries follow the form: gauge, unit_weight;
    PL: Plain
    PB: Phosphor Bronze
    NW: Nickel Wound
    XS: Stainless Steel
    HR:
    @param string_material: the type of material the string is made of; determines which dictionary to pass back
    @return: the dictionary corresponding to the string
    """
    if string_material == 'PL':
        return PL
    elif string_material == 'PB':
        return PB
    elif string_material == 'XS':
        return XS
    elif string_material == 'NW':
        return NW
    else:
        return HR