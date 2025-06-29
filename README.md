# BiaEye: AI-Powered Urban Waste Management Platform

BiaEye is an intelligent system designed to detect illegal waste dumping in real time, engage local communities, and provide municipalities with actionable insights. It integrates AI, geospatial analytics, and citizen participation to combat rising urban waste. BiaEye was selected for incubation by Jordan's Ministry of Digital Economy and Entrepreneurship and showcased at COP29.

---

## 🌍 Vision

BiaEye transforms waste management from reactive cleanup to proactive prevention. It supports UN SDGs 8, 9, 11, and 13 by:

- Detecting illegal dumping in real time
- Analyzing spatial patterns for smarter waste services
- Empowering communities to take action

---

## ✨ Core Features

- **Real-Time Detection**: Cameras mounted on city vehicles use YOLO AI models to detect illegal dumping instantly
- **Geospatial Analytics**: Maps waste hotspots for smarter bin placement and route planning
- **Automated Reporting**: Sends reports with geotagged images to authorities for fast response
- **Citizen App**: Rewards users for reporting and maintaining clean areas
- **Privacy Compliance**: Automatically blurs personal identifiers in captured images

---

## ⚙️ System Architecture

1. **Data Capture**: Vehicle-mounted cameras scan surroundings
2. **AI Detection**: YOLO model processes live video for illegal waste
3. **Data Transmission**: Captured frames are geotagged and sent to BiaEye servers
4. **Geospatial Analysis**: Dynamic maps show waste trends and recurring hotspots
5. **Reporting**: Automated alerts and weekly summaries sent to municipal teams
6. **Community Loop**: Users are notified, rewarded, or encouraged to improve cleanliness in their area

---

## 🤖 Technology Stack

- **AI Models**: 
  - YOLOv11 (main model): Best balance of accuracy and speed
  - YOLOv8, YOLOv5 (benchmarked)
- **Programming Language**: Python
- **Annotation Tool**: Roboflow
- **Geospatial Tools**: GIS for spatial visualization and analysis
- **Dataset**: Public + custom images collected from Amman

### Model Comparison

| Model    | Inference Time | Accuracy (mAP50-95) | Model Size |
|----------|----------------|---------------------|------------|
| YOLOv11  | 5.8ms          | 0.225               | 2.5M       |
| YOLOv8   | 4.9ms          | 0.479               | 2.7M       |
| YOLOv5   | 7.4ms          | 0.128               | —          |

---

## 🏆 Achievements

- Finalist in GJU “Creative Solutions” Competition
- Incubated by the Ministry of Digital Economy and Entrepreneurship
- Presented at COP29 (Azerbaijan)
- Featured during World Youth Day 2024

---

## 🚀 Roadmap

- **More Data**: Partnering with cities to diversify training datasets
- **Stronger Engagement**: Gamified rewards and community leaderboards
- **Better Detection**: Combining YOLO with segmentation models like Mask R-CNN
- **Impact Study**: 6–12 month analysis of behavioral and environmental outcomes
- **Global Scale**: Deploying BiaEye in more cities worldwide
