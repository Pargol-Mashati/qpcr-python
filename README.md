# qPCR Analysis Script

This repository contains a Python script for processing qPCR data using the ΔΔCt method.

## Input Format
The script expects a QuantStudio Excel output with:
- Metadata in the first 21 rows (skipped automatically)
- Columns starting from row 22 with headers including "Sample", "Target", "Cq", etc.

## Features
- Cleans raw QuantStudio Excel output
- Filters and normalizes Ct values
- Calculates relative expression
- Outputs a clean Excel file with results

## Requirements
- Python 3
- pandas
- numpy
- openpyxl (for Excel export)

## How to Run
1. Place your raw `.xlsx` file in the same folder
2. Update the filename in the script
3. Run the script using:

 ## Output
The final Excel file includes:
- Filtered and cleaned Ct values
- ΔCt and normalized relative expression
- A column for each processed result (e.g., `normalized`, `average`)

## Author
Made by Pargol 
