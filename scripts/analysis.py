#!/usr/bin/env python3
"""
Core analysis functions for ResistanceFinder pipeline
"""

import pandas as pd
import numpy as np
from .config import PRIORITY_WEIGHTS, QTL_LOD_THRESHOLD

def identify_genes_in_qtl(genes, qtls):
    """Identify candidate genes that fall within verified QTL regions"""
    candidates = []
    for _, gene in genes.iterrows():
        for _, qtl in qtls.iterrows():
            if (gene['chromosome'] == qtl['chromosome'] and
                gene['start'] >= qtl['start'] and
                gene['end'] <= qtl['end']):
                candidates.append({
                    'gene_id': gene['gene_id'],
                    'gene_family': gene['gene_family'],
                    'chromosome': gene['chromosome'],
                    'start': gene['start'],
                    'end': gene['end'],
                    'qtl_id': qtl['qtl_id'],
                    'lod_score': qtl['lod_score'],
                    'evidence': gene['evidence']
                })
    return pd.DataFrame(candidates) if candidates else pd.DataFrame()

def prioritize_genes(candidates):
    """Prioritize candidate genes based on evidence strength and LOD scores"""
    if len(candidates) == 0:
        return candidates
    
    prioritized = candidates.copy()
    scores = []
    
    for _, gene in prioritized.iterrows():
        score = PRIORITY_WEIGHTS['base_score']
        
        if gene['lod_score'] >= 5.0:
            score += PRIORITY_WEIGHTS['high_lod']
        elif gene['lod_score'] >= 4.0:
            score += PRIORITY_WEIGHTS['moderate_lod']
        
        evidence = str(gene['evidence']).lower()
        if 'gwas' in evidence:
            score += PRIORITY_WEIGHTS['gwas_evidence']
        if 'qtl' in evidence:
            score += PRIORITY_WEIGHTS['qtl_evidence']
        if 'fine mapping' in evidence:
            score += PRIORITY_WEIGHTS['fine_mapping']
        
        scores.append(min(score, 1.0))
    
    prioritized['priority_score'] = scores
    return prioritized.sort_values('priority_score', ascending=False)

def simulate_pav_patterns(candidates, wild_relatives, cultivated):
    """Simulate presence/absence variation patterns (for demonstration)"""
    if len(candidates) == 0:
        return pd.DataFrame()
    
    pav_data = candidates.copy()
    pav_data['present_in_wild'] = np.random.choice([True, False], len(pav_data), p=[0.7, 0.3])
    pav_data['present_in_cultivated'] = np.random.choice([True, False], len(pav_data), p=[0.3, 0.7])
    pav_data['wild_specific'] = pav_data['present_in_wild'] & ~pav_data['present_in_cultivated']
    
    return pav_data

def filter_significant_qtls(qtls, threshold=QTL_LOD_THRESHOLD):
    """Filter QTLs by LOD score threshold"""
    return qtls[qtls['lod_score'] >= threshold].copy()
