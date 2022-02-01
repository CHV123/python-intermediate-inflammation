""" Tests for the library functions"""

import numpy as np
import numpy.testing as npt
import pytest


@pytest.mark.parametrize(
    "test_data, test_names, expected",
    [
        ([[1., 2., 3.], [4., 5., 6.]],
         ['Alice', 'Dave'],
         [{
                'name': 'Alice',
                'data': [1., 2., 3.],
         }, {
                'name': 'Dave',
                'data': [4., 5., 6.],
         }, ]),
    ])
def test_attach_names(test_data, test_names, expected):
    """Test attach names works for test case of names and data"""
    from inflammation.library import attach_names
    npt.assert_array_equal(attach_names(test_data, test_names), np.array(expected))
