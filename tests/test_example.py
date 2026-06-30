"""Example test to demonstrate pytest.

Copy this pattern for your own tests!
"""

import pytest
import pandas as pd


@pytest.fixture
# def sample_df():
#     """Sample DataFrame for testing."""
#     return pd.DataFrame({
#         'id': [1,2,3],
#         'name': ['Alice', 'Bob', 'Charlie']
#     })

def sample_df():
    """Sample DataFrame for testing."""
    return pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'Gary']
    })


def test_example_len(sample_df):
    """Example test - shows pytest working."""
    assert len(sample_df) == 4

def test_example_id(sample_df):
    """Example test - shows pytest working."""
    assert 'id' in sample_df.columns

def test_example_unique(sample_df):
    """Example test - shows pytest working."""
    assert sample_df['id'].is_unique

def test_example_id_no_nulls(sample_df):
    """Ensure the ID column contains no missing values."""
    assert sample_df['id'].isnull().sum() == 0

def test_example_expected_columns(sample_df):
    """Verify all required columns exist in the DataFrame."""
    expected_cols = ['id', 'name']  # Replace with your actual columns
    assert all(col in sample_df.columns for col in expected_cols)



