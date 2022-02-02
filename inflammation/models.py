"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row
contains inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: 2D data array containing inflammation data
    :returns: the means of the input inflammation data

    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array.

    :param data: 2D data array containing inflammation data
    :returns: the maximums of the 2D data array

    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array.

    :param data: 2D data array containing inflammation data
    :returns: the minimums of the 2D data array

    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0

    :param data: 2D data array containing inflammation data (ndarray)
    :returns: Normalised inflammation data from the input (ndarray)

    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')

    if len(data.shape) != 2:
        raise ValueError('inflammation array should be 2-dimensional')

    if not isinstance(data, np.ndarray):
        raise TypeError

    maxima = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / maxima[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


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


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Patient(Person):
    """ A patient in an inflammation study"""
    def __init__(self, name, observations=None):
        super().__init__(name)
        self.observations = []
        if observations is not None:
            self.observations = observations

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation

    def __str__(self):
        return self.name

    @property
    def last_observation(self):
        return self.observations[-1]


class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)


class Doctor(Person):
    """A minimal doctor class for keeping track of patient assignment"""
    def __init__(self, name, patients=None):
        super().__init__(name)
        self.patients = []
        if patients is not None:
            self.patients.append(patients)

    def add_patient(self, patient):
        """Returns list of patients"""
        if patient is Patient:
            self.patients.append(patient)
        else:
            raise ValueError("Added patient must be of patient class")

        return self.patients

    def __str__(self):
        return self.name

    @property
    def patient_list(self):
        return self.patients
