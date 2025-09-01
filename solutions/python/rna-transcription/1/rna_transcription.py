from typing import Dict

DNA_TO_RNA_MAPPING: Dict[str, str] = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}

def to_rna(dna_strand):
    rna_compliment: str = ''
    for nucleotide in dna_strand:
        if nucleotide not in DNA_TO_RNA_MAPPING:
            raise ValueError(f'"{nucleotide}" is not a valid DNA nucleotide')
        rna_compliment += DNA_TO_RNA_MAPPING[nucleotide]
    return rna_compliment
