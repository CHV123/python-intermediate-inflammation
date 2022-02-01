""" Module containing functions and objects to store and generate
    patient data
"""


def attach_names(data, names):
    """ Attach a set of patient data to the provided names

    :param data: The patient data, a 1D array per patient
    :param names: A 1D array of patient names

    :return output: The tuple of data and patient names

    """

    assert len(data) == len(names)
    output = []

    for data_row, name in zip(data, names):
        output.append({'name': name,
                       'data': data_row})

    return output
