# Labs chapter 2

Python labs for learning generators, iterators, and project organization.

## About

This repository contains laboratory work for programming course.

## Labs

### Lab 1: Generators and Iterators

Simple implementation of python generators and timeout-based iterators.

- Incremental counter generator
- Iterator that runs for specified time
- Calculates running sum and average

**Location** `lab1/`

### Lab 2: Project Setup

Set up proper project structure with configuration files, examples, and documentation.

### Lab 3: Memoization Function

Implementation of memoization decorator with configurable cache eviction strategies.

**Features:**
- LRU (Least Recently Used) eviction
- LFU (Least Frequently Used) eviction
- Time-based cache expiry
- Configurable cache size and TTL

**Location:** `lab3/`

### Lab 4: Bi-Directional Priority Queue

Implementation of priority queue with dual access modes.

**Features:**
- Priority-based operations (highest/lowest)
- Insertion order operations (oldest/newest)
- Peek and dequeue functionality
- FIFO and LIFO support

**Location:** `lab4/`

### Lab 5: Async Array Functions

Asynchronous versions of array map function.

**Implementations:**
- Callback-based version
- Promise-based version
- Async/await support
- AbortController for cancellation

**Location:** `lab5/`

## Installation 

Clone the repository:
```bash
git clone https://github.com/zxromxnd/labschapter2.git
cd labschapter2
```

## Usage

### Lab 1 Examples

Run Lab 1 examples:
```bash
python -m examples.basic_usage
python -m examples.custom_start
python lab1/main.py
```

### Lab 3 Examples

Run Lab 3 examples:
```bash
python lab3/examples.py
python lab3/test_lru.py
python lab3/test_lfu.py
```

### Lab 4 Examples

Run Lab 4 examples:
```bash
python lab4/examples.py
python lab4/test_queue.py
```

### Lab 5 Examples

Run Lab 5 examples:
```bash
python lab5/examples.py
python lab5/test_abort.py
```

## Author

Eugene 

Gmail : zhenyabruhovetsky@gmail.com 
Telegram : @evgbryu

## License

MIT