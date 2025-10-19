# 3D Print Connector - Blender Addon

![Blender](https://img.shields.io/badge/Blender-3.0+-orange.svg)
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-GPL--3.0-green.svg)
![Version](https://img.shields.io/badge/Version-1.3.3-brightgreen.svg)

**[English](README.md) | [Türkçe](docs/README-tr.md)**

**3D Print Connector** is a powerful Blender addon that creates professional **tenon-mortise** joints between two objects. Designed for precise and reliable connections in your 3D printing projects.

## ✨ Features

- 🔧 **Precise Tenon-Mortise Joints**: Perfect-fitting connections between two objects
- 📏 **Millimeter-Based Tolerance Control**: Separate precision settings for X, Y, Z axes
- ⚙️ **Smart Unit System**: Compatible with all Blender unit systems (mm, cm, m, inch)
- 🔄 **Automatic Chamfering**: Professional edge finishing on connector pieces
- 🎯 **User-Friendly Interface**: Step-by-step guided simple usage
- 🌍 **Multi-Language Support**: Turkish and English interface
- ⚡ **Automatic Boolean Operations**: Fast and clean cutting operations

## 🎯 Use Cases

- **3D Printing Projects**: Splitting large parts into smaller sections
- **Modular Designs**: Interlocking toys and scale models
- **Furniture & Decoration**: Woodworking-style joints
- **Engineering Applications**: Precise mechanical connections
- **Prototyping**: Designs requiring quick assembly/disassembly

## 📦 Installation

### Automatic Installation (Recommended)

1. [Download the latest release](https://github.com/makin38/3D-Print-Connector/blob/master/3d-print-connector.py) (`.py` file)
2. Open Blender
3. Go to `Edit > Preferences > Add-ons`
4. Click `Install...` button
5. Select the downloaded `.py` file
6. Enable "3D Print Connector" addon ✅

### Manual Installation

```bash
# Find your Blender scripts folder
~/AppData/Roaming/Blender/3.x/scripts/addons/  # Windows
~/Library/Application Support/Blender/3.x/scripts/addons/  # macOS
~/.config/blender/3.x/scripts/addons/  # Linux

# Copy eklentim133.py to this folder
```

## 🚀 Quick Start

### Step 1: Open the Addon
Press `N` in Blender to open the side panel and find the **"3D Print Connector"** tab.

### Step 2: Prepare Your Objects
```
Example Scenario:
• Main Part (large object) - the main piece to be joined
• Second Part - part to be connected to the main piece
• Connector Piece - tenon piece that will join the two parts
```

### Step 3: Make Selections
1. Select the **main part** → Click `Select Object 1` button ✅
2. Select the **second part** → Click `Select Object 2` button ✅
3. Select the **connector piece** → Click `Select Connector Piece` button ✅

### Step 4: Adjust Tolerances
```
Recommended Values:
• X Axis: 0.2 mm (side tolerance)
• Y Axis: 0.2 mm (side tolerance)
• Z Axis: 0.5 mm (depth tolerance - looser)
• Chamfer: 0.5 mm (edge smoothing)
```

### Step 5: Create!
Click the `Create Mortises` button and watch the magic! ✨

## ⚙️ Detailed Settings

### Tolerance Control

| Axis | Description | Recommended Value | Usage |
|------|-------------|-------------------|-------|
| **X** | Side tolerance | 0.1-0.3 mm | Small for tight fit |
| **Y** | Side tolerance | 0.1-0.3 mm | Small for tight fit |
| **Z** | Depth tolerance | 0.3-0.8 mm | Larger for easy insertion |

### Chamfer Settings

- **0.0 mm**: No chamfer (sharp edges)
- **0.3-0.5 mm**: Standard chamfer (recommended)
- **1.0+ mm**: Large chamfer (aesthetic appearance)

### Unit System Support

The addon automatically detects Blender's unit settings:

```
✅ Supported Units:
• Millimeters (mm) - default
• Centimeters (cm)
• Meters (m)
• Inches (inch)
• Feet

💡 Tolerance values are ALWAYS in millimeters!
```

## 🎬 Video Examples

### Basic Usage
![Basic Usage](docs/images/basic-usage.gif)

### Advanced Tolerance Settings
![Tolerance Settings](docs/images/tolerance-settings.gif)

## 🔧 Technical Details

### Algorithm
1. **Connector Analysis**: Calculates dimensions of selected connector piece
2. **Tolerance Application**: Adds specified tolerance values on each axis
3. **Boolean Operation**: Performs precise mortise (groove) cutting
4. **Chamfer Application**: Applies edge smoothing only to connector piece

### Performance
- ⚡ **Fast Processing**: Completes in seconds
- 🎯 **Precise Calculation**: Micron-level accuracy
- 💾 **Memory Friendly**: Efficient even with large meshes

### Compatibility
- **Blender**: 3.0+ (LTS)
- **Python**: 3.7+
- **Platform**: Windows, macOS, Linux

## 🛠️ Troubleshooting

### Common Issues

#### Problem: "Boolean operation failed"
```
Solution:
1. Ensure meshes are manifold
2. Apply scale to objects (Ctrl+A)
3. Clean up duplicate vertices
```

#### Problem: Tolerance too tight/loose
```
Solution:
1. Set Z axis (depth) to 0.5mm
2. Start with X,Y axes at 0.2mm
3. Make test prints to fine-tune
```

#### Problem: Chamfer not applying properly
```
Solution:
1. Apply scale to connector object
2. Check for non-manifold edges in mesh
3. Reduce chamfer value (0.3-0.5mm)
```

### Debug Mode
View detailed information in Blender Console (`Window > Toggle System Console`):

```python
=== UNIT SYSTEM INFORMATION ===
Blender Unit Settings: MILLIMETERS
Scale: 0.001
1 Blender Unit = 1.000 mm
X Tolerance: 0.2 mm = 0.000200 BU
```

## 🤝 Contributing

This project is open source and we welcome your contributions!

### Development Environment
```bash
git clone https://github.com/makin38/3d-print-connector.git
cd 3d-print-connector

# Test in Blender development mode
blender --background --python eklentim133.py
```

### Types of Contributions
- 🐛 **Bug Reports**: [Issues](https://github.com/makin38/3d-print-connector/issues)
- 💡 **Feature Suggestions**: Share your new ideas
- 🌍 **Translation**: Add new language support
- 📖 **Documentation**: README and wiki improvements
- 💻 **Code**: Pull requests are always welcome

### Development Guidelines
1. Follow **PEP 8** Python code standards
2. Write comments in **English**
3. **Test**: Test your changes in different scenarios
4. **Document**: Update README for new features

## 📋 Roadmap

### v1.4.0 (Next Release)
- [ ] 🔄 **Batch Processing**: Multiple object support
- [ ] 📐 **Custom Connector Shapes**: Round, hexagonal, custom
- [ ] 💾 **Preset System**: Save tolerance settings
- [ ] 🎨 **Material Automation**: Auto material assignment for print colors

### v1.5.0 (Long Term)
- [ ] 🤖 **AI Optimization**: Automatic tolerance suggestions
- [ ] 📱 **Export Optimization**: STL/3MF export settings
- [ ] 🔗 **Slicer Integration**: Direct slicer export
- [ ] 📊 **Analysis Tools**: Print cost calculation

## 📄 License

This project is published under the **GPL-3.0** license. See [LICENSE](LICENSE) file for details.

```
3D Print Connector - Blender Addon for Tenon-Mortise Connections
Copyright (C) 2024 Mustafa Akin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.
```

## 👨‍💻 Developer

**Mustafa Akin**
- 📧 Email: [makin38@gmail.com](mailto:makin38@gmail.com) | [makin38@hotmail.com](mailto:makin38@hotmail.com)
- 🐱 GitHub: [@makin38](https://github.com/makin38)

## 🙏 Acknowledgments

- **Blender Foundation**: For the amazing 3D software
- **3D Printing Community**: For testing and feedback
- **Open Source Community**: For inspiration and support

---

## 📸 Screenshots

### Main Interface
![Main Interface](docs/images/main-interface.png)

### Tolerance Settings
![Tolerance Settings](docs/images/tolerance-settings.png)

### Result Example
![Result](docs/images/result-example.png)

---

## 🚀 Try It Now!

```bash
# Quick test:
1. Create two cubes (Add > Mesh > Cube)
2. Use third cube as connector
3. Run the addon!
```

**⭐ If you like the project, don't forget to give it a star!**

---

*This addon was developed with love ❤️ and lots of coffee ☕.*
