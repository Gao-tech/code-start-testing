# 🚀 AWS Lambda Cold Start Comparison: Go vs Python vs Node.js

> “Same API Gateway. Same test interval. Same project. Just three runtimes walking into the cold...”

This project compares AWS Lambda **cold start performance** and **developer experience** across three runtimes: **Go**, **Python**, and **Node.js**.

---

## 🔍 Why Use AWS X-Ray?

AWS X-Ray is a powerful tool for visualizing and analyzing serverless performance:

- ✅ End-to-end latency tracking
- ✅ Cold start vs execution time breakdown
- ✅ Visual request flow mapping

**Complementary Tools:**

- **CloudWatch Logs**: Raw logs
- **X-Ray**: Performance trace visualization

---

## 🧪 Experimental Setup

### Identical Conditions

All Lambda functions use:

- Same API Gateway endpoint
- Same return response: `{"message": "..."}`
- ARM64 architecture
- X-Ray enabled
- Triggered via EventBridge at 15-minute intervals
- 123 traces collected over 10 hours

### Deployment Method

```bash
rm -rf .aws-sam
sam build && sam deploy --s3-bucket <fresh-bucket>

cold-start-testing/
├── go/                # Go 1.24 (ARM64)
│   ├── main.go
│   ├── go.mod
│   ├── go.sum
│   └── Makefile
├── python/            # Python 3.12
│   ├── app.py
│   └── requirements.txt
├── nodejs/            # Node.js 20.x
│   ├── app.js
│   └── package.json
└── template.yaml      # SAM configuration

Visual Breakdown

|-------------------- Total Duration: 1000ms ---------------------|
|         Cold Start (Init: 552.28ms)        | Execution (447.72ms) |
|               55.228%                      |      44.772%          |


Runtime | Cold Start Rate | Notes
Node.js | 100%            | High churn, suspected early recycling
Go      | 65%             | ~35% warm starts, better container reuse
Python  | Negligible      | 0.5% overhead for long-running functions



Runtime | Execution Duration (ms) | Cold Start Overhead (%)
Go      | ~250ms                  | ~40%
Node.js | ~500ms                  | ~55%
Python  | ~3min+                  | <1% (negligible)
```
