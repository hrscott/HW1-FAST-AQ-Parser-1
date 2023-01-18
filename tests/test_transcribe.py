# write tests for transcribes
import pathlib
import sys
import os
from seqparser import (FastaParser, FastqParser, transcribe, reverse_transcribe)

SEQ1="ATCGCGCGCGACGTGCATGCATGCTTGATCA"

SEQ_w_U="AUCGTAGCTAGUAGCTGAUGATCGATCA"

SEQ1_rev="ACTAGTTCGTACGTACGTGCAGCGCGCGCTA"

SEQ1_rev_with_missing_base="ACTAGTTCGTACGTA GTGCAGCGCGCGCTA"

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

# testing to see if  Value Error is thrown when "U" is aberrantly present in DNA seq fed to transcribe function
def test_transcribe_uracils_present():
  
    transcribe(SEQ_w_U)
    assert True 

# testing  to see if transcribe and reverse transcribe functions are working properly by produceing the same output from mirrored sequence input
# (SEQ1 and SEQ1_rev)
def test_transcribe_and_reverse_transcribe_functional():

    trans=transcribe(SEQ1)
    rev_trans= reverse_transcribe(SEQ1_rev)
    assert trans==rev_trans

    

