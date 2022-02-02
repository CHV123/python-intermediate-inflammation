""" File containing data persistence functions"""

from inflammation import models
import json
from abc import ABC, abstractmethod


class PatientSerializer:
    """Class for saving and loading data using the JSON serializer class"""
    model = models.Patient

    @classmethod
    def serialize(cls, instances):
        return [{
            'name': instance.name,
            'observations': ObservationSerializer.serialize(instance.observations),
        } for instance in instances]

    @classmethod
    def deserialize(cls, data):
        instances = []

        for item in data:
            item['observations'] = ObservationSerializer.deserialize(item.pop('observations'))
            instances.append(cls.model(**item))

        return instances


class PatientJSONSerializer(PatientSerializer):
    @classmethod
    def save(cls, instances, path):
        with open(path, 'w') as jsonfile:
            json.dump(cls.serialize(instances), jsonfile)

    @classmethod
    def load(cls, path):
        with open(path) as jsonfile:
            data = json.load(jsonfile)

        return cls.deserialize(data)


class Serializer(ABC):
    """Abstract class for inheritance purposes to save and load data"""
    @abstractmethod
    def serialize(cls, instances):
        raise NotImplementedError

    @classmethod
    def save(cls, instances, path):
        raise NotImplementedError

    @abstractmethod
    def deserialize(cls, data):
        raise NotImplementedError

    @classmethod
    def load(cls, path):
        raise NotImplementedError


class ObservationSerializer(Serializer):
    """Saving the observation data for particular patients"""
    model = models.Observation

    @classmethod
    def serialize(cls, instances):
        return [{
            'day': instance.day,
            'value': instance.value,
        } for instance in instances]

    @classmethod
    def save(cls, instances, path):
        raise NotImplementedError

    @classmethod
    def deserialize(cls, data):
        return [cls.model(**d) for d in data]

    @classmethod
    def load(cls, path):
        raise NotImplementedError
