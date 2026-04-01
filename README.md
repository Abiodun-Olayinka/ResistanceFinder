# 🍌 ResistanceFinder: Banana Pangenome Analysis for TR4 Resistance

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

**ResistanceFinder** is a professional bioinformatics pipeline that identifies candidate TR4 resistance genes from the banana pangenome. It integrates verified QTL regions from published literature with gene annotations from the Banana Genome Hub to prioritize targets for marker-assisted selection.

### Why This Matters

Fusarium wilt Tropical Race 4 (TR4) is devastating global banana production. This pipeline helps breeders:
- Identify resistance genes from wild relatives
- Develop molecular markers for selection
- Accelerate breeding programs by 3-5 years

## Key Features

- ✅ **Verified References**: Uses peer-reviewed QTL data (Zorrilla 2023, Ferreira 2024)
- ✅ **Modular Design**: Clean, reusable Python code
- ✅ **Reproducible**: Fixed random seeds and environment configuration
- ✅ **Professional Outputs**: Publication-quality figures and comprehensive reports
- ✅ **Breeder-Ready**: KASP marker design and prioritization scores

## Quick Start

### Prerequisites

```bash
# Clone the repository
git clone https://github.com/Abiodun-Olayinka/ResistanceFinder.git
cd ResistanceFinder

# Install dependencies
pip install -r requirements.txt
# OR with conda
conda env create -f environment.yml
conda activate resistancefinder
