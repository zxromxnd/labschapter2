# Labs chapter 2

Python labs for learning generators, iterators, and project organization.

## About

This repository contains laboratory work for programming course.

## Labs

### Lab 1: Generators and Iterators

Simple implementation of Python generators and timeout-based iterators.

- Incremental counter generator
- Iterator that runs for specified time
- Calculates running sum and average

**Location** `lab1/`

### Lab 2: Project Setup

Set up proper project structure with configuration files, examples, and documentation.

### Lab 3: Memoization Function

Implementation of memoization decorator with configurable cache eviction strategies.

**Features:**
- Least Recently Used (LRU) eviction
- Least Frequently Used (LFU) eviction
- Time-based cache expiry
- Configurable cache size and TTL

**Location** `lab3/`

## Installation 

Clone the repository:
```bash
git clone https://github.com/zxromxnd/labschapter2.git
cd labschapter2
```

## Usage

### Lab1 Examples

Run the examples:
```bash
python -m examples.basic_usage
python -m examples.custom_start
```

Or run lab 1 directly:
```bash
python lab1/main.py
```

### Lab3 Examples

Run examples:
```bash
python lab3/examples.py
```

Run tests:
```bash
python lab3/test_lru.py
python lab3/test_lfu.py
```

## Author

Eugene 

Gmail : zhenyabruhovetsky@gmail.com 
Telegram : @evgbryu

## License

MIT
