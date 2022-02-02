"""Tests for the Doctor model."""


def test_create_doctor():
    from inflammation.models import Patient, Doctor

    # Create Doctor with no Patients
    name = 'Emmi'
    doc = Doctor(name)
    assert doc.name == name

    # Create Doctor with Patient
    pname = 'Bob'
    pat1 = Patient(pname)
    dname = 'Alice'
    doc1 = Doctor(dname, pat1)
    assert doc1.name == dname
    assert doc1.patients[0].name == pat1.name
