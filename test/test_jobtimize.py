# coding: utf-8

""
import sys
sys.path.append("..")

""
from Jobtimize import jobscrap
import pytest

""
class TestJobtimize:
    searchList = ["Data Analyst nantes"]
    countryList = ["FR", "QS"]
    
    scraped = jobscrap(searchList, countryList)
    
    def test_dimension(self):
        assert self.scraped.shape[1] == 9
    
    def test_falseCountry(self):
        assert "QS" not in self.scraped["country"].unique()