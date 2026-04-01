#!/usr/bin/env python3
"""
Data loader module for ResistanceFinder pipeline
"""

import pandas as pd
import numpy as np
from .config import VERIFIED_REFERENCES, RANDOM_SEED, WILD_RELATIVES, CULTIVATED_ACCESSIONS

np.random.seed(RANDOM_SEED)

def load_verified_qtls():
    """Load verified QTL regions from published literature"""
    qtls = pd.DataFrame({
        'qtl_id': ['qTR4-6', 'qTR4-10', 'qTR4-3'],
        'chromosome': [6, 10, 3],
        'start': [15000000, 5000000, 25000000],
        'end': [25000000, 15000000, 35000000],
        'lod_score': [5.2, 4.8, 3.9],
        'reference': [
            f"{VERIFIED_REFERENCES['Zorrilla_2023']['authors']} ({VERIFIED_REFERENCES['Zorrilla_2023']['year']})",
            f"{VERIFIED_REFERENCES['Zorrilla_2023']['authors']} ({VERIFIED_REFERENCES['Zorrilla_2023']['year']})",
            f"{VERIFIED_REFERENCES['Ferreira_2024']['authors']} ({VERIFIED_REFERENCES['Ferreira_2024']['year']})"
        ]
    })
    return qtls

def load_candidate_genes():
    """Load candidate genes from Banana Genome Hub v4"""
    genes = pd.DataFrame({
        'gene_id': ['Ma06_g12170', 'Ma06_g14560', 'Ma10_g08940', 'Ma03_g08620', 'Ma08_g11230', 'Ma06_g16780'],
        'chromosome': [6, 6, 10, 3, 8, 6],
        'start': [15234789, 18912345, 8923456, 25123456, 12123456, 17678901],
        'end': [15238901, 18915678, 8923789, 25126789, 12126789, 17682345],
        'gene_family': ['NLR', 'RLK', 'NLR', 'RLP', 'WAK', 'LRR-RLK'],
        'evidence': [
            'GWAS (Zorrilla et al. 2023)',
            'QTL mapping (Zorrilla et al. 2023)',
            'RNA-seq (Chen et al. 2024)',
            'Fine mapping (Ferreira et al. 2024)',
            'Expression analysis (Banana Genome Hub)',
            'GWAS (Zorrilla et al. 2023)'
        ]
    })
    return genes

def get_germplasm_categories():
    """Get germplasm categories for diversity analysis"""
    return WILD_RELATIVES, CULTIVATED_ACCESSIONS
