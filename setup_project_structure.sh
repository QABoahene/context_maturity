#!/bin/bash

###############################################################################
# Script Name:     setup_project_structure.sh
# Author:          Q.A. Boahene
# Description:     Initializes the Context Maturity project with a standard
#                  data science/AI structure, following Cookiecutter-style best
#                  practices, including folder creation and boilerplate setup.
# Created On:      2025-04-17
# Version:         1.0.0
# License:         MIT
###############################################################################

echo "🔧 Setting up Context Maturity project structure..."

# Create folders
mkdir -p data/{raw,processed,external}
mkdir -p notebooks
mkdir -p src/{data,features,models,visualization}
mkdir -p tests
mkdir -p reports/figures
mkdir -p streamlit_app/components

# Move existing folders into new structure
if [ -d "jupyter notebooks" ]; then
    mv "jupyter notebooks"/* notebooks/
    rmdir "jupyter notebooks"
    echo "📁 Moved notebooks"
fi

if [ -d "images" ]; then
    mv images/* reports/figures/
    rmdir images
    echo "🖼️ Moved images to reports/figures"
fi

if [ -d "python files" ]; then
    echo "📦 Found 'python files'. Please move individual scripts to the appropriate src/ subfolder:"
    echo "👉 src/data/, src/features/, src/models/, or src/visualization/"
    echo "   You can do this manually based on what each script does."
fi

# Create .gitignore if not present
if [ ! -f .gitignore ]; then
    echo -e ".DS_Store\n__pycache__/\n*.pyc\n.env/\n.vscode/" > .gitignore
    echo "🛑 Created .gitignore"
fi

# Create README.md with author and project info
if [ ! -f README.md ]; then
    cat <<EOL > README.md
# Context Maturity Project

**Author:** Q.A. Boahene  
**Created:** April 2025  
**License:** MIT  
**Version:** 1.0.0

## Project Overview
The Context Maturity Project analyses how the context and meaning of lyrics evolve across an artist’s discography, using AI, NLP, and visual storytelling.

## Structure
- \`data/\`: Raw, processed, and external datasets
- \`src/\`: Modular scripts for data loading, feature engineering, modelling, and visualisation
- \`notebooks/\`: Jupyter notebooks for EDA and prototyping
- \`streamlit_app/\`: Web UI using Streamlit
- \`reports/\`: Visual outputs, figures, and summaries

## Getting Started
1. Clone the repo
2. Install dependencies: \`pip install -r requirements.txt\`
3. Run: \`streamlit run streamlit_app/app.py\`

EOL
    echo "📝 Created README.md"
fi

# Create basic LICENSE file
if [ ! -f LICENSE ]; then
    cat <<EOL > LICENSE
MIT License

Copyright (c) 2025 Q.A. Boahene

Permission is hereby granted, free of charge, to any person obtaining a copy...
EOL
    echo "📜 Created LICENSE file"
fi

# Create CHANGELOG.md
if [ ! -f CHANGELOG.md ]; then
    cat <<EOL > CHANGELOG.md
# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-04-17
- Initial project scaffolding created
- Folder structure aligned with Cookiecutter standards
- Added boilerplate README, LICENSE, .gitignore

EOL
    echo "🗒️ Created CHANGELOG.md"
fi

# Create requirements.txt if missing
[ -f requirements.txt ] || touch requirements.txt

echo "✅ Project structure set up successfully with author and versioning metadata!"