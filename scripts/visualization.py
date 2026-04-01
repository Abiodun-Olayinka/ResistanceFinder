#!/usr/bin/env python3
"""
Visualization module for ResistanceFinder pipeline
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from .config import FIGURES_DIR, FIGURE_DPI, FIGURE_WIDTH, FIGURE_HEIGHT

def setup_plot_style():
    """Configure matplotlib style"""
    plt.rcParams['figure.figsize'] = (FIGURE_WIDTH, FIGURE_HEIGHT)
    plt.rcParams['savefig.dpi'] = FIGURE_DPI
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12

def create_qtl_plot(qtls, output_file="verified_qtl_regions.png"):
    """Create QTL region visualization"""
    setup_plot_style()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['#2E86AB', '#A23B72', '#F18F01']
    
    for idx, (_, qtl) in enumerate(qtls.iterrows()):
        width = qtl['end'] - qtl['start']
        ax.barh(qtl['qtl_id'], width, left=qtl['start'],
                color=colors[idx % len(colors)], edgecolor='black', alpha=0.7)
        ax.text(qtl['start'] + width/2, idx, f"LOD={qtl['lod_score']}", 
                ha='center', va='center', fontweight='bold')
    
    ax.set_xlabel('Position (bp)')
    ax.set_ylabel('QTL')
    ax.set_title('Verified QTL Regions for TR4 Resistance\n(Zorrilla et al. 2023; Ferreira et al. 2024)')
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / output_file, dpi=FIGURE_DPI, bbox_inches='tight')
    plt.close()
    print(f"✓ Created: figures/{output_file}")

def create_gene_family_plot(candidates, output_file="gene_family_distribution.png"):
    """Create gene family distribution plot"""
    setup_plot_style()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    family_counts = candidates['gene_family'].value_counts()
    colors = plt.cm.Set3(range(len(family_counts)))
    
    bars = ax.bar(family_counts.index, family_counts.values, color=colors, edgecolor='black')
    ax.set_xlabel('Gene Family')
    ax.set_ylabel('Count')
    ax.set_title('Candidate Resistance Gene Families\nWithin Verified QTL Regions')
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    for bar, val in zip(bars, family_counts.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, str(val), ha='center')
    
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / output_file, dpi=FIGURE_DPI, bbox_inches='tight')
    plt.close()
    print(f"✓ Created: figures/{output_file}")

def create_priority_plot(prioritized, output_file="priority_scores.png"):
    """Create priority scores plot"""
    if len(prioritized) == 0:
        return
    
    setup_plot_style()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    top_genes = prioritized.head(10)
    colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(top_genes)))
    
    ax.barh(top_genes['gene_id'], top_genes['priority_score'], color=colors, edgecolor='black')
    ax.set_xlabel('Priority Score')
    ax.set_ylabel('Gene ID')
    ax.set_title('Top 10 Prioritized Candidate Genes for TR4 Resistance')
    ax.set_xlim(0, 1)
    ax.grid(axis='x', alpha=0.3)
    
    for i, (_, row) in enumerate(top_genes.iterrows()):
        ax.text(row['priority_score'] + 0.02, i, f"{row['priority_score']:.2f}", va='center')
    
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / output_file, dpi=FIGURE_DPI, bbox_inches='tight')
    plt.close()
    print(f"✓ Created: figures/{output_file}")

def create_chromosome_map(candidates, qtls, output_file="chromosome_map.png"):
    """Create chromosome map"""
    if len(candidates) == 0:
        return
    
    setup_plot_style()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    chrom_positions = {3: 0, 6: 1, 8: 2, 10: 3}
    chrom_lengths = {3: 35000000, 6: 25000000, 8: 18000000, 10: 15000000}
    
    for chrom in [3, 6, 8, 10]:
        if chrom not in chrom_positions:
            continue
        y_pos = chrom_positions[chrom]
        ax.plot([0, chrom_lengths[chrom]], [y_pos, y_pos], 'k-', linewidth=2)
        
        chr_qtls = qtls[qtls['chromosome'] == chrom]
        for _, qtl in chr_qtls.iterrows():
            ax.plot([qtl['start'], qtl['end']], [y_pos, y_pos], 'r-', linewidth=8, alpha=0.5)
            ax.text(qtl['start'] + (qtl['end'] - qtl['start'])/2, y_pos + 0.1, qtl['qtl_id'], ha='center', fontsize=8)
        
        chr_genes = candidates[candidates['chromosome'] == chrom]
        for _, gene in chr_genes.iterrows():
            ax.plot(gene['start'], y_pos, 'o', markersize=8, color='blue', alpha=0.7)
            ax.text(gene['start'], y_pos + 0.15, gene['gene_id'], rotation=45, ha='center', fontsize=7)
    
    ax.set_yticks(list(chrom_positions.values()))
    ax.set_yticklabels([f'Chr {k}' for k in sorted(chrom_positions.keys())])
    ax.set_xlabel('Position (bp)')
    ax.set_title('Chromosome Map of QTL Regions and Candidate Genes')
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / output_file, dpi=FIGURE_DPI, bbox_inches='tight')
    plt.close()
    print(f"✓ Created: figures/{output_file}")

def create_all_plots(qtls, prioritized, candidates):
    """Create all visualizations"""
    print("\nCreating visualizations...")
    print("-" * 40)
    
    create_qtl_plot(qtls)
    if len(prioritized) > 0:
        create_gene_family_plot(prioritized)
    create_priority_plot(prioritized)
    if len(candidates) > 0:
        create_chromosome_map(candidates, qtls)
    
    print("\n✓ Visualizations complete!")
