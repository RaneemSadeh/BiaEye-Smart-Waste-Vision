from ultralytics import YOLO

def train_waste_detection_model():
    """
    Train YOLOv11 model for waste detection
    """
    seeds = [42, 123, 456, 789, 1011]
    for seed in seeds:
        print(f"\n --Training with seed: {seed} --")
        model = YOLO('yolo11s.pt')
        
        model.train(
            data='data.yaml',          # Path to your dataset configuration
            epochs=5,                 # Number of training epochs
            imgsz=640,                  # Image size
            batch=16,                   # Batch size (reduce if you get memory errors)
            patience=50,                # Early stopping patience
            save=True,                  # Save checkpoints
            plots=True,                 # Generate training plots
            device='cpu',                   # Use GPU 0, use 'cpu' if no GPU
            project='runs/detect',      # Project directory
            name=f'train_seed_{seed}',  # Experiment name with the seed value
            exist_ok=True,              # Overwrite existing experiment
            pretrained=True,            # Use pretrained weights
            optimizer='auto',           # Optimizer (auto, SGD, Adam, AdamW)
            verbose=True,               # Verbose output
            seed=seed,                    # Random seed for reproducibility
            deterministic=True,         # Deterministic mode
            single_cls=False,           # Train as single-class (set True if only 1 class)
            rect=False,                 # Rectangular training
            cos_lr=False,               # Cosine learning rate scheduler
            close_mosaic=10,            # Disable mosaic augmentation for final epochs
            resume=False,               # Resume training from last checkpoint
            amp=True,                   # Automatic Mixed Precision training
            fraction=1.0,               # Dataset fraction to train on
            profile=False,              # Profile ONNX and TensorRT speeds
            freeze=None,                # Freeze layers (None, int, or list)
            hsv_h=0.015,               # HSV-Hue augmentation
            hsv_s=0.7,                 # HSV-Saturation augmentation
            hsv_v=0.4,                 # HSV-Value augmentation
            degrees=15.0,               # Rotation augmentation
            translate=0.1,             # Translation augmentation
            scale=0.5,                 # Scale augmentation
            shear=0.0,                 # Shear augmentation
            perspective=0.0,           # Perspective augmentation
            flipud=0.0,                # Vertical flip probability
            fliplr=0.5,                # Horizontal flip probability
            mosaic=1.0,                # Mosaic augmentation probability
            mixup=0.0,                 # Mixup augmentation probability
            copy_paste=0.0,            # Copy-paste augmentation probability
        )

if __name__ == "__main__":
    train_waste_detection_model()