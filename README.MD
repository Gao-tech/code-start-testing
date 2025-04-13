# AWS Lambda X-Ray Analysis Toolkit

Analyze AWS Lambda performance (Python/Node.js/Go) using X-Ray traces while keeping production deployments clean.

## Features

- 📊 Cold start comparisons
- ⏱ Duration distribution analysis
- 🕒 Time-based invocation patterns

## Setup

```bash
# Clone repo
git clone https://github.com/yourusername/code-start-testing.git
cd code-start-testing/analysis

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt  # pandas, matplotlib, seaborn
```

## Usage

```bash
./run_analysis.sh  # Generates CSV + plots in analysis/plots/
```

## Project Structure

```
.
├── src/                  # Production Lambdas (Python/Node.js/Go)
├── analysis/             # Local analysis tools
│   ├── venv/            # Python virtual env
│   ├── parse_xray_traces.py # Main script
│   └── run_analysis.sh  # Execution wrapper
└── xray_logs/           # X-Ray trace data
```

## Sample Output

![Cold Start Rates](plots/cold_start_rates.png)
