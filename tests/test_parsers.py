# write tests for parsers

from seqparser import (FastaParser, FastqParser, transcribe, reverse_transcribe)
import pathlib
import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def get_data_path(which):
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    if which == "fasta":
        return data_dir / "test.fa"
    else:
        return data_dir / "test.fq"

def get_testcase_fasta(reference):
    data_dir = pathlib.Path.cwd().resolve()
    if reference == "fasta":
        return data_dir / "missing_value.fa"
    else:
        return data_dir / "test.fq"


def open_fasta_reference():
    f = pathlib.Path.cwd().resolve()/ "test.fa"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip(), f.readlines()))
    return seqs 

def open_fastq_reference():
    f = pathlib.Path.cwd().resolve()/ "test.fq"
    with f.open() as f:
        seqs = list(map(lambda l: l.strip(), f.readlines()))
    return seqs 



# testing whether line count in seqparsed(test.fa) file is correctly 1/2 of that of the count of the same 
# unparsed test.fa file 

def test_FastaParser_intended_linecount():
    
    parsed_data=list(FastaParser(get_data_path("fasta"))) 

    unparsed_data= open_fasta_reference()

    assert len(unparsed_data)==2*(len(parsed_data))
    

# testing whether list elements in seqparsed(test.fa) file contain any whitespace (there should be none)

def test_FastaParser_no_whitespace():
    
    parsed_data=list(FastaParser(get_data_path("fasta"))) 
    
    res=False
    for i in parsed_data:
        if (i.count(" ")<1):
            res=True
            break
    assert str(res)=="True"

# testing whether line count in seqparsed(test.fq) file is correctly 1/2 of that of the count of the same 
# unparsed test.fq file 

def test_FastqParser_intended_linecount():
    
    parsed_data=list(FastqParser(get_data_path("not"))) 

    unparsed_data= open_fastq_reference()

    assert len(unparsed_data)==4*(len(parsed_data))
