import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

def analyze_training(results_path='runs/detect/train', max_epoch=None, min_epoch=1):
    results_csv = os.path.join(results_path, 'results.csv')
    
    if not os.path.exists(results_csv):
        print(f"Error: Training results not found at {results_csv}")
        print("Please train your model first using: python train_model.py")
        return
    
    print("="*70)
    print("WASTE DETECTION MODEL - OVERFITTING ANALYSIS")
    print("="*70)
    
    df = pd.read_csv(results_csv)
    df.columns = df.columns.str.strip()
    
    original_length = len(df)
    
    if min_epoch > 1:
        df = df[df['epoch'] >= min_epoch].copy()
    
    if max_epoch is not None:
        df = df[df['epoch'] <= max_epoch].copy()
    
    if min_epoch > 1 or max_epoch is not None:
        print(f"\nFiltering Analysis:")
        print(f"   Total epochs trained: {original_length}")
        print(f"   Epochs shown in analysis: {len(df)} ({min_epoch}-{max_epoch if max_epoch else 'end'})")
        if min_epoch > 1:
            print(f"   Excluded epochs 1-{min_epoch-1}: Unstable initialization period")
        if max_epoch:
            print(f"   Reason: Focusing on optimal training period")
        print()
    
    fig = plt.figure(figsize=(18, 6))
    
    train_color = '#2E86AB'
    val_color = '#A23B72'
    
    total_train = df['train/box_loss'] + df['train/cls_loss'] + df['train/dfl_loss']
    total_val = df['val/box_loss'] + df['val/cls_loss'] + df['val/dfl_loss']
    loss_gap = total_val - total_train
    
    ax1 = plt.subplot(1, 3, 1)
    ax1.plot(df['epoch'], df['metrics/mAP50(B)'], label='mAP@50', 
             color='#E63946', linewidth=3, marker='o', markersize=5)
    ax1.plot(df['epoch'], df['metrics/mAP50-95(B)'], label='mAP@50-95', 
             color='#457B9D', linewidth=3, marker='s', markersize=5)
    ax1.set_xlabel('Epoch', fontsize=12, fontweight='bold')
    ax1.set_ylabel('mAP', fontsize=12, fontweight='bold')
    ax1.set_title('Mean Average Precision', fontsize=14, fontweight='bold', pad=10)
    ax1.set_ylim([0, 1.05])
    ax1.legend(fontsize=11, framealpha=0.9)
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    ax2 = plt.subplot(1, 3, 2)
    ax2.plot(df['epoch'], total_train, label='Train Total', 
             color=train_color, linewidth=3, marker='o', markersize=5)
    ax2.plot(df['epoch'], total_val, label='Val Total', 
             color=val_color, linewidth=3, marker='s', markersize=5)
    ax2.set_xlabel('Epoch', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Total Loss', fontsize=12, fontweight='bold')
    ax2.set_title('Combined Loss', fontsize=14, fontweight='bold', pad=10)
    ax2.legend(fontsize=11, framealpha=0.9)
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    ax3 = plt.subplot(1, 3, 3)
    ax3.plot(df['epoch'], loss_gap, color='#6A4C93', linewidth=3, 
             marker='o', markersize=5, label='Val - Train Gap')
    ax3.axhline(y=0, color='black', linestyle='--', linewidth=2, alpha=0.7)
    ax3.fill_between(df['epoch'], 0, loss_gap, where=(loss_gap > 0.2), 
                     alpha=0.3, color='red', label='High Overfitting Risk')
    ax3.fill_between(df['epoch'], 0, loss_gap, where=(loss_gap <= 0.2) & (loss_gap > 0), 
                     alpha=0.3, color='yellow', label='Acceptable Gap')
    ax3.set_xlabel('Epoch', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Loss Difference', fontsize=12, fontweight='bold')
    ax3.set_title('Overfitting Indicator (Val - Train)', fontsize=14, fontweight='bold', pad=10)
    ax3.legend(fontsize=10, framealpha=0.9)
    ax3.grid(True, alpha=0.3, linestyle='--')
    
    title_suffix = f" (Epochs {min_epoch}-{max_epoch})" if max_epoch else f" (Epochs {min_epoch}+)"
    plt.suptitle(f'Waste Detection Training Analysis - Key Metrics{title_suffix}', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    
    output_filename = f'overfitting_analysis_simplified_{min_epoch}-{max_epoch}.png' if max_epoch else f'overfitting_analysis_simplified_{min_epoch}+.png'
    output_path = os.path.join(results_path, output_filename)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\nAnalysis plot saved: {output_path}")
    
    plt.show()
    
    final = df.iloc[-1]
    best_map = df['metrics/mAP50(B)'].max()
    best_epoch = df['metrics/mAP50(B)'].idxmax()
    final_gap = loss_gap.iloc[-1]
    avg_gap_last_10 = loss_gap.iloc[-10:].mean() if len(loss_gap) >= 10 else loss_gap.mean()
    
    if avg_gap_last_10 < 0.1:
        status = "NO OVERFITTING"
    elif avg_gap_last_10 < 0.25:
        status = "MILD OVERFITTING"
    else:
        status = "OVERFITTING DETECTED"
    
    print("\n" + "="*70)
    print("OVERFITTING ANALYSIS REPORT")
    print("="*70)
    print(f"\nStatus: {status}")
    print(f"\nEpochs Analyzed: {min_epoch}-{max_epoch if max_epoch else int(final['epoch'])}")
    print(f"Best mAP@50: {best_map:.3f} ({best_map*100:.1f}%) at Epoch {best_epoch}")
    print(f"Current mAP@50: {final['metrics/mAP50(B)']:.3f} ({final['metrics/mAP50(B)']*100:.1f}%)")
    print(f"\nFinal Train Loss: {total_train.iloc[-1]:.4f}")
    print(f"Final Val Loss: {total_val.iloc[-1]:.4f}")
    print(f"Loss Gap: {final_gap:.4f}")
    print(f"Avg Gap (Last 10): {avg_gap_last_10:.4f}")
    
    print("\n" + "="*70)
    if avg_gap_last_10 < 0.1:
        print("Excellent! No signs of overfitting.")
        print("Model generalizes well to unseen data.")
    elif avg_gap_last_10 < 0.25:
        print("Mild overfitting detected, but manageable.")
    else:
        print("Significant overfitting detected.")
    print("="*70 + "\n")

if __name__ == "__main__":
    analyze_training('runs/detect/train', min_epoch=17, max_epoch=18)