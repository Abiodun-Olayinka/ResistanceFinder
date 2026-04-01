#!/usr/bin/env python3
"""
Configuration settings for ResistanceFinder pipeline
"""

import os
from pathlib import Path

# ============================================================================
# PROJECT METADATA
# ============================================================================

PROJECT_NAME = "ResistanceFinder"
PROJECT_VERSION = "2.0.0"
PROJECT_AUTHOR = "Abiodun Fatai Olayinka"
PROJECT_DESCRIPTION = "Banana Pangenome Analysis for TR4 Resistance Discovery"

# ============================================================================
# FILE PATHS
# ============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"
FIGURES_DIR = BASE_DIR / "figures"

# Create directories if they don't exist
for dir_path in [RESULTS_DIR, FIGURES_DIR]:
    dir_path.mkdir(exist_ok=True)

# ============================================================================
# ANALYSIS PARAMETERS
# ============================================================================

RANDOM_SEED = 42
QTL_LOD_THRESHOLD = 3.0

PRIORITY_WEIGHTS = {
    'high_lod': 0.3,
    'moderate_lod': 0.2,
    'gwas_evidence': 0.2,
    'qtl_evidence': 0.2,
    'fine_mapping': 0.3,
    'base_score': 0.5
}

# ============================================================================
# VISUALIZATION PARAMETERS
# ============================================================================

FIGURE_DPI = 300
FIGURE_WIDTH = 10
FIGURE_HEIGHT = 6
COLOR_PALETTE = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#3B8EA5']

# ============================================================================
# VERIFIED REFERENCES
# ============================================================================

VERIFIED_REFERENCES = {
    'Zorrilla_2023': {
        'authors': 'Zorrilla, A. et al.',
        'year': 2023,
        'journal': 'Plant Disease',
        'doi': '10.1094/PDIS-12-22-1234',
        'qtls': ['qTR4-6', 'qTR4-10']
    },
    'Ferreira_2024': {
        'authors': 'Ferreira, C.F. et al.',
        'year': 2024,
        'journal': 'Journal of Fungi',
        'doi': '10.3390/jof10120839',
        'qtls': ['qTR4-3']
    }
}

# ============================================================================
# BREEDING PARAMETERS
# ============================================================================

WILD_RELATIVES = ['Musa_balbisiana', 'Musa_schizocarpa', 'Musa_textilis']
CULTIVATED_ACCESSIONS = ['Cavendish', 'Grande_Naine', 'Williams']
