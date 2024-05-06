#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   @File Name:     config.py
   @Author:        Luyao.zhang
   @Date:          2023/5/16
   @Description: configuration file
-------------------------------------------------
"""
from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())


# Source
SOURCES_LIST = ["Image", "Video", "Webcam"]


# DL model config
DETECTION_MODEL_DIR = ROOT / 'weights' / 'detection'
Thermal_CBAM = DETECTION_MODEL_DIR / "Thermal_CBAM.pt"
Thermal_ECA = DETECTION_MODEL_DIR / "Thermal_ECA.pt"
Thermal_MHSA = DETECTION_MODEL_DIR / "Thermal_MHSA.pt"
Thermal_SE = DETECTION_MODEL_DIR / "Thermal_SE.pt"
Thermal_V0 = DETECTION_MODEL_DIR / "Thermal_V0.pt"
Thermal_V1 = DETECTION_MODEL_DIR / "Thermal_V1.pt"
Thermal_V2 = DETECTION_MODEL_DIR / "Thermal_V2.pt"

DETECTION_MODEL_LIST = [
    "Thermal_CBAM.pt",
    "Thermal_ECA.pt",
    "Thermal_MHSA.pt",
    "Thermal_SE.pt",
    "Thermal_V0.pt",
    "Thermal_V1.pt",
    "Thermal_V2.pt"]
