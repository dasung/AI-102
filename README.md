# AI-102 Project

## Overview
This project is designed to recognize text in images using modern AI tools and workflows. It leverages Conda and npm for environment and package management, and utilizes markmap-cli for visualizing markdown files.

Install markmap VS-Code Extension to Preview.

![design](https://github.com/user-attachments/assets/a286ddb1-bfc3-459e-a277-e83fe0204e98)


## Setup Instructions

### 1. Create the Conda Environment
Create an `env.yml` file with the following content:

```yaml
name: ai-102
dependencies:
  - python=3.9
  - pip
  - nodejs
  - pip:
      - markmap-cli
```

Then, create the environment:
```bash
conda env create -f env.yml
conda activate ai-102
```

### 2. Install npm Dependencies
If your project uses npm packages, run:
```bash
npm install
```

### 3. Install markmap-cli (if not installed via pip)
```bash
npm install -g markmap-cli
```

## Usage
- To recognize text in images, follow the instructions in `ai-102.md` (to be created).
- To visualize markdown as a mindmap:
```bash
markmap ai-102.md
```

## Features
- Text recognition in images
- Markdown mindmap visualization

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)

