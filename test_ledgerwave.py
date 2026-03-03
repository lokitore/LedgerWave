# test_ledgerwave.py
"""
Tests for LedgerWave module.
"""

import unittest
from ledgerwave import LedgerWave

class TestLedgerWave(unittest.TestCase):
    """Test cases for LedgerWave class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerWave()
        self.assertIsInstance(instance, LedgerWave)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerWave()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
