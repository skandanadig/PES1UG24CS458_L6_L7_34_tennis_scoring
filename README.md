# Tennis Scoring System — Lab 6 & Lab 7

**Course:** Software Engineering Lab  
**Repository:** [skandanadig/L6_L7_34_tennis_scoring](https://github.com/skandanadig/L6_L7_34_tennis_scoring)

---

## Overview

This repository contains the laboratory implementations and test suites for:
1. **Lab 6: Code and Branch Coverage Analysis** (`/lab6`)
2. **Lab 7: Fuzz Testing with Hypothesis** (`/lab7`)

The project models a tennis scoring system that tracks points in a game (including deuce and advantage), determines set winners, and computes match status across multi-set matches (best-of-3 or best-of-5).

---

## Repository Structure

```
├── README.md                                  # Root Documentation
├── lab6/                                      # Lab 6: Code & Branch Coverage
│   ├── README.md                              # Lab 6 Overview
│   ├── tennis_scoring.py                      # Application module under test
│   ├── test_tennis_scoring.py                 # Comprehensive test suite (100% coverage)
│   ├── CodeCoverageTest_tennis_scoring.py     # Statement/Code coverage tests (100%)
│   ├── BranchCoverageTest_tennis_scoring.py   # Branch coverage tests (100%)
│   ├── code_coverage_report.png               # Terminal screenshot: Statement coverage report
│   └── branch_coverage_report.png             # Terminal screenshot: Branch coverage report
└── lab7/                                      # Lab 7: Fuzz Testing
    ├── README.md                              # Lab 7 Overview
    ├── tennis_scoring.py                      # Module under test
    └── test_tennis_scoring.py                 # Hypothesis property-based fuzz tests
```

---

## Lab 6: Code and Branch Coverage Analysis

### Objectives
- Measure statement (line) coverage and branch coverage using `pytest` and Python's `coverage` library.
- Design targeted test cases covering all edge conditions and decision branches to achieve $\ge 90\%$ (achieved **100%**).
- Generate coverage analysis reports and terminal output screenshots.

### Coverage Results
- **Statement / Code Coverage:** **100%** (38 / 38 statements covered)
- **Branch Coverage:** **100%** (30 / 30 branches covered, 0 missed)

### Running Lab 6 Tests and Reports

1. **Navigate to the Lab 6 directory:**
   ```bash
   cd lab6
   ```

2. **Run Code Coverage:**
   ```bash
   python3 -m coverage run -m pytest test_tennis_scoring.py
   python3 -m coverage report -m
   ```

3. **Run Branch Coverage:**
   ```bash
   python3 -m coverage run --branch -m pytest test_tennis_scoring.py
   python3 -m coverage report -m
   ```

4. **Run Deliverable Test Suites Independently:**
   ```bash
   pytest CodeCoverageTest_tennis_scoring.py
   pytest BranchCoverageTest_tennis_scoring.py
   ```

---

## Setup & Dependencies

Install required testing packages via `pip`:

```bash
pip install pytest coverage hypothesis
```
