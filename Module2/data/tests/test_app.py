"""Tests for the app."""
import pytest
import numpy as np
from app import process_data, create_dataframe

def test_process_data():
    """Test data processing with numpy."""
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    assert result == 3.0

def test_create_dataframe():
    """Test dataframe creation."""
    data = {"name": ["Alice", "Bob"], "age": [25, 30]}
    df = create_dataframe(data)
    assert len(df) == 2
    assert "name" in df.columns

def test_numpy_array():
    """Test numpy array operations."""
    arr = np.array([1, 2, 3])
    assert arr.sum() == 6
