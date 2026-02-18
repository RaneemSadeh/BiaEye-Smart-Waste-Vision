<div align="center">

#  BiaEye: AI-Powered Illegal Waste Detection & Urban Analytics

<img width="80%" alt="BiaEye System" src="https://github.com/RaneemSadeh/BiaEye-Smart-Waste-Vision/blob/main/Sadeh10.png" />

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![YOLOv11](https://img.shields.io/badge/Model-YOLOv11-orange.svg)](https://arxiv.org/abs/2410.17725)
[![IEEE Access](https://img.shields.io/badge/Published-IEEE%20Access-blue.svg)](https://doi.org/10.1109/ACCESS.2024.0429000)
[![COP29](https://img.shields.io/badge/Showcased-COP29%20Baku-brightgreen.svg)](https://unfccc.int/cop29)

**BiaEye** is an intelligent urban waste management system that detects illegal dumping in real time, empowers local communities, and delivers actionable geospatial intelligence to municipalities. It integrates state-of-the-art AI, GIS analytics, and citizen engagement to address one of today's most pressing environmental challenges.

>  **Incubated** by Jordan's Ministry of Digital Economy and Entrepreneurship &nbsp;

</div>


##  Vision

BiaEye transforms waste management from **reactive cleanup** to **proactive prevention**. By equipping existing municipal infrastructure with AI-powered eyes, it enables cities to detect, analyze, and respond to illegal dumping before it escalates into a public health or environmental crisis.

---

##  The Problem

Global municipal solid waste is projected to reach **3.4 billion tonnes by 2050** — a ~70% increase over current levels. Illegal dumping alone costs municipalities an estimated **$8–10 billion annually** in remediation worldwide.

Traditional monitoring systems fall critically short:

| Challenge | Impact |
|---|---|
| Manual inspections cover only **5–10%** of metro areas weekly | Vast enforcement blind spots |
| Only **15–20%** of illegal dumping incidents are detected | Most violations go unaddressed |
| Static routing wastes **60–80%** of collection budgets | Inefficient resource allocation |
| Reactive-only systems can't predict emerging hotspots | Environmental damage accumulates unchecked |

---

##  Core Features

| Feature | Description |
|---|---|
|  **Real-Time Detection** | YOLOv11 model runs on cameras mounted on garbage trucks, identifying illegal dumping as it happens |
|  **Geospatial Analytics** | GIS dashboard maps waste hotspots, guides bin placement, and optimizes collection routes |
|  **Automated Reporting** | Weekly geotagged reports sent to authorities (e.g., Greater Amman Municipality) |
|  **Citizen App** | Residents report incidents and earn rewards for verified cleanups |
|  **Privacy by Design** | Automated blurring of faces, license plates, and house numbers before any data is stored |
|  **Edge Computing** | On-device inference via NVIDIA Jetson Nano — no cloud upload required |

---


**Key components:**

1. **Data Capture** — AI-powered cameras on municipal vehicles scan routes during normal operation
2. **Anonymization** — OpenCV Haar Cascades + MTCNN blur identifiers before any storage
3. **AI Detection** — Optimized YOLOv11n detects waste at **5.47 FPS** on edge hardware
4. **Geotagging** — Every detection is stamped with GPS coordinates and timestamp
5. **Geospatial Analysis** — GIS tools identify hotspots, dead zones, and optimal bin locations
6. **Reporting** — Automated alerts and summaries dispatched to city teams
7. **Community Feedback Loop** — Residents track progress and receive incentives for clean-up actions

---

##  Technology Stack

```
AI / ML
├── YOLOv11n    — Primary detection model (deployed)
├── YOLOv8n     — Benchmarked
└── YOLOv5n     — Benchmarked

Framework & Tools
├── Python 3.x
├── PyTorch
├── Roboflow    — Dataset annotation & management
└── GIS         — Geospatial visualization

Hardware
├── Training:   NVIDIA GeForce RTX 3050
└── Inference:  NVIDIA Jetson Nano 2GB ($59, 5–10W)

Data
├── ~1,000–3,000 primary images (Amman, Jordan)
├── Kaggle public datasets (global urban waste)
└── Augmented to ~8,000–15,000 training samples
```

---

##  Model Performance

Three YOLO variants were trained and rigorously evaluated on the same dataset. YOLOv11 was selected for deployment based on its superior **real-world robustness** in challenging urban conditions — not just its validation metrics.

### Benchmark Results

| Model | Speed (FPS) | mAP@0.5:0.95 | Params |
|-------|-------------|--------------|--------|
| **YOLOv11** | **5.47** | 0.427 | **2.5M** |
| YOLOv8 | 4.91 | **0.479** | 2.7M |
| YOLOv5 | **7.38** | 0.128 | 7.2M |

> **Why YOLOv11?** Although YOLOv8 achieved the highest mAP on the curated validation set, qualitative testing on real Amman street images showed YOLOv11 consistently outperformed at detecting **small scattered items**, **partially occluded waste**, and **novel cluttered scenes** — the conditions that matter most in deployment.

### Generalization Health

| Metric | Value |
|--------|-------|
| Training mAP@0.5:0.95 | 0.512 |
| Validation mAP@0.5:0.95 | 0.427 |
| Train–Val gap | 16.6% (within the accepted <20% threshold) |

### Training Configuration

```python
model     = 'yolov11n.pt'   # Nano — edge-optimized
epochs    = 20
img_size  = 320
batch     = 8
lr        = 0.001
dropout   = 0.15
hardware  = 'NVIDIA RTX 3050'
precision = 'FP16 (half=True)'
```

---

##  Geospatial Analytics

BiaEye's GIS dashboard turns raw detections into municipal intelligence:

- **Hotspot Identification** — Reveals areas with chronic illegal dumping patterns
- **Route Optimization** — Adjusts collection paths dynamically, reducing fuel costs by up to **15%**
- **Bin Allocation** — Guides strategic placement of new bins using population density + waste accumulation data
- **Dead Zone Detection** — Flags under-served areas at highest risk of becoming informal dump sites
- **Trend Analysis** — Monitors change over time to evaluate the effectiveness of interventions

---

##  Community Reward System

Behavior change is as important as detection. BiaEye closes the loop with a **citizen incentive platform**:

- Residents report illegal dumping via a mobile-friendly interface
- Each verified report earns **reward points**
- Points are redeemable for **discounts on water, electricity, or municipal services**
- If cleanup is confirmed in a follow-up truck scan → **area residents are rewarded**
- If waste persists → residents receive a **nudge notification** with local data

This gamified civic participation system is the **first of its kind** to directly link AI detection outcomes to community behavioral change.

---

##  Privacy & Ethics

BiaEye is built on a **privacy-by-design** philosophy. Unlike surveillance systems, it detects waste — not people.

| Measure | Implementation |
|---|---|
| **Face blurring** | OpenCV Haar Cascades + MTCNN, automatic |
| **License plate & house number obfuscation** | Automated before storage |
| **Data retention** | Raw images deleted after **7 days**; anonymized versions retained for **2 years** |
| **Access control** | Role-based access for authorized municipal staff with audit logging |
| **Geofencing** | Recording automatically disabled near military bases, schools, hospitals, and government buildings |
| **Consent & transparency** | Clear truck signage, public awareness campaigns, and a policy website |
| **Standards** | Aligned with Jordan's data protection law and GDPR-inspired principles |

No facial recognition. No behavioral profiling. No personal data sold or shared.

---

##  UN SDG Alignment

BiaEye directly supports four UN Sustainable Development Goals:

| SDG | Contribution |
|-----|-------------|
| **SDG 8** — Decent Work & Economic Growth | Reduces cleanup costs; creates data annotation, maintenance, and engagement jobs |
| **SDG 9** — Industry, Innovation & Infrastructure | Demonstrates AI integration into existing municipal infrastructure |
| **SDG 11** — Sustainable Cities & Communities | Cleaner urban spaces, smarter services, empowered citizens |
| **SDG 13** — Climate Action | Reduces landfill methane emissions; optimizes truck routes to lower fuel consumption |

---

##  Achievements

-  **Finalist** — GJU "Creative Solutions" Competition
-  **Incubated** — Jordan's Ministry of Digital Economy and Entrepreneurship
-  **Presented** — Artificial Intelligence with No Borders (United Arab Emirates)


---

##  Getting Started

> **Note:** Full deployment requires truck-mounted cameras and municipal integration. The steps below cover local model inference.

### Prerequisites

```bash
pip install ultralytics torch torchvision opencv-python
```

### Run Inference on an Image

```python
from ultralytics import YOLO

model = YOLO('yolov11n.pt')  # or path to fine-tuned weights
results = model('your_image.jpg')
results[0].show()
```

### Training on Custom Data

```python
from ultralytics import YOLO

model = YOLO('yolov11n.pt')
model.train(
    data='data.yaml',
    epochs=20,
    imgsz=320,
    batch=8,
    lr0=0.001,
    dropout=0.15,
    half=True
)
```

### Dataset Structure

```
dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/
```

> All annotations use a single class: `Trash`. Bounding boxes were drawn manually in Roboflow.

---

## Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| Phase 1 | YOLOv11 model training & validation | Complete |
| Phase 2 | Field deployment in Amman | Complete |
| Phase 3 | Expanded Jordan-specific dataset | In Progress |
| Phase 4 | Gamified community leaderboards | In Progress |
| Phase 5 | Mask R-CNN segmentation integration | Planned |
| Phase 6 | 6–12 month behavioral impact study | Planned |
| Phase 7 | Multi-city deployment | Planned |

---


##  Team

| Name | Role | Institution |
|------|------|-------------|
| **Raneem Yahya Sadeh** | Lead Researcher & Founder | Al Hussein Technical University |
| **Huthaifa Al-Omari** | Co-Author | Al Hussein Technical University |
| **Murad A. Yaghi** | Principal Investigator (Senior IEEE Member) | Al Hussein Technical University |

---

<div align="center">

**Built with in Amman, Jordan — for cities everywhere.**

</div>
