#!/usr/bin/env python3
"""
ResistanceFinder - Complete Banana Pangenome Analysis Pipeline
Run with: python run_pipeline.py
"""

import sys
import os
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from scripts.config import PROJECT_NAME, PROJECT_VERSION, PROJECT_AUTHOR
from scripts.data_loader import load_verified_qtls, load_candidate_genes, get_germplasm_categories
from scripts.analysis import identify_genes_in_qtl, prioritize_genes, simulate_pav_patterns
from scripts.visualization import create_all_plots
from scripts.utils import save_results, generate_summary

def main():
    print("="*70)
    print(f"{PROJECT_NAME} v{PROJECT_VERSION}")
    print(f"Author: {PROJECT_AUTHOR}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    # Step 1: Load data
    print("\n[1/6] Loading verified data...")
    print("-" * 40)
    qtls = load_verified_qtls()
    print(f"  ✓ Loaded {len(qtls)} verified QTL regions")
    for _, qtl in qtls.iterrows():
        print(f"    - {qtl['qtl_id']}: Chr{qtl['chromosome']} ({qtl['start']:,}-{qtl['end']:,} bp, LOD={qtl['lod_score']})")
    
    genes = load_candidate_genes()
    print(f"\n  ✓ Loaded {len(genes)} candidate genes")
    families = ', '.join(genes['gene_family'].unique())
    print(f"    Gene families: {families}")
    
    # Step 2: Identify genes in QTLs
    print("\n[2/6] Identifying genes within QTL regions...")
    print("-" * 40)
    candidates = identify_genes_in_qtl(genes, qtls)
    print(f"  ✓ Found {len(candidates)} genes within QTL regions")
    for _, gene in candidates.iterrows():
        print(f"    - {gene['gene_id']} ({gene['gene_family']}) in {gene['qtl_id']} (LOD={gene['lod_score']})")
    
    # Step 3: Prioritize
    print("\n[3/6] Prioritizing candidate genes...")
    print("-" * 40)
    prioritized = prioritize_genes(candidates)
    if len(prioritized) > 0:
        print(f"  ✓ Prioritized {len(prioritized)} genes")
        print("\n  Top 5 candidates:")
        for i, (_, gene) in enumerate(prioritized.head(5).iterrows(), 1):
            print(f"    {i}. {gene['gene_id']} ({gene['gene_family']}) - Score: {gene['priority_score']:.2f}")
    
    # Step 4: Diversity analysis
    print("\n[4/6] Analyzing genetic diversity patterns...")
    print("-" * 40)
    wild, cultivated = get_germplasm_categories()
    print(f"  Wild relatives: {', '.join(wild)}")
    print(f"  Cultivated: {', '.join(cultivated)}")
    pav_data = simulate_pav_patterns(candidates, wild, cultivated)
    if len(pav_data) > 0:
        wild_specific = pav_data[pav_data['wild_specific']]
        print(f"\n  ✓ Identified {len(wild_specific)} wild-specific candidate genes")
        for _, gene in wild_specific.iterrows():
            print(f"    - {gene['gene_id']} ({gene['gene_family']})")
    
    # Step 5: Visualize
    print("\n[5/6] Creating visualizations...")
    print("-" * 40)
    create_all_plots(qtls, prioritized, candidates)
    
    # Step 6: Save results
    print("\n[6/6] Saving results and generating report...")
    print("-" * 40)
    save_results(qtls, genes, candidates, prioritized)
    generate_summary(qtls, genes, candidates, prioritized)
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE!")
    print("="*70)
    print(f"\nResults saved to: results/")
    print(f"Figures saved to: figures/")
    print(f"\nTo view summary:")
    print(f"  cat results/analysis_summary.txt")
    print("\n" + "="*70)

if __name__ == "__main__":
    main()
