# Probiotic Bacteria Classifier

A command-line tool for classifying probiotic bacteria based on their morphological characteristics. This tool uses machine learning to predict bacterial classifications from observable features.

## Overview

This classifier helps microbiologists and researchers identify probiotic bacteria by analyzing their key morphological characteristics. It uses a pre-trained AutoSklearn model to make predictions based on standard microbiological observations.

## Features

- Rapid classification of probiotic bacteria
- Batch processing capability through CSV files
- Based on standard microbiological characteristics
- Uses machine learning for accurate predictions
- Easy-to-use command line interface

## Requirements

- Python 3.x
- pandas
- joblib
- auto-sklearn

## Installation

```bash
pip install pandas joblib auto-sklearn
```

## Usage

Basic command:

```bash
python cli_inference.py data/input.csv -o data/output.csv
```

### Required Input Features

The input CSV must contain these morphological characteristics:

| Feature | Description |
|---------|------------|
| Form/Shape | Overall bacterial colony form |
| colony Color | Color of the bacterial colony |
| Colony margin | Edge characteristics of the colony |
| Gram's Staining | Gram stain reaction result |
| Cell shape | Microscopic cell morphology |

### Example Input Format

```csv
Form/Shape,colony Color,Colony margin,Gram's Staining,Cell shape
Circular,White,Entire,Positive,Rod
Irregular,Cream,Undulate,Negative,Cocci
...
```

## Quick Start

1. Prepare your data in CSV format with the required features
2. Run the classifier:
   ```bash
   python cli_inference.py data/your_samples.csv -o results/classification.csv
   ```
3. Check the output file for classification results

## Directory Structure

```
.
├── cli_inference.py           # Main classifier script
├── model/
│   └── autosklearn_model.pkl  # Pre-trained classification model
└── data/                     # Data directory
    └── Result.csv           # Default output location
```

## Model Information

The classifier uses a pre-trained AutoSklearn model optimized for probiotic bacteria classification. The model has been trained on a comprehensive dataset of known probiotic bacterial characteristics.

## Output

The script will add a 'label' column to your data containing the classification results. Results are saved in CSV format for easy integration with other analysis tools.

## Technical Notes

- Automatically handles one-hot encoding of categorical features
- Creates output directories if they don't exist
- Preserves original feature data in output file
- Includes prediction labels for each sample

## Version Information
- Last Updated: 2025-11-09 13:02:12 UTC
- Maintained by: ArtBioDesign

## Support

For issues or questions about the probiotic bacteria classifier, please create an issue in the repository.

## Note

This tool is designed for research and laboratory use. Results should be verified using standard microbiological techniques when used in clinical or industrial applications.