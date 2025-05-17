# 100 Prisoners Problem – Python Simulation

This project simulates the famous **100 prisoners riddle**, demonstrating the massive survival gap between:
- A naive **random strategy**
- The optimal **loop-following (cycle) strategy**

> 🔗 Based on the [Veritasium video](https://www.youtube.com/watch?v=iSNsgj1OCLA)

---

## Problem Summary

- 100 prisoners
- 100 boxes, each containing a number from 1 to 100
- Each prisoner can open **50 boxes**
- If **all** prisoners find their number: they are set free. Otherwise, all prisoners are executed.

---

## Strategies Simulated

### 1.**Best Strategy (Loop-Following)**
Each prisoner:
- Starts with the box numbered the same as them.
- Opens the box and checks the number inside.
- Uses that number to open the next box.
- Repeats for up to 50 tries.

**Why it works:** This exploits permutations and cycles. If all loops are ≤ 50 in length implies a win.

### 2. **Random Strategy**
Each prisoner:
- Opens 50 random boxes without repetition.

This leads to near-zero chance of success.

---

## How to Run

### 1. Install Python 3.x  
### 2. Run the script:
```bash
python3 prisoners_strategy.py
