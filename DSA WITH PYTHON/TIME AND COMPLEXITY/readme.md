# Time and Space Complexity

## What is Time Complexity?

Time complexity measures how the running time of an algorithm grows as the input size (`n`) increases. It does **not** measure the actual execution time in seconds; instead, it describes the **rate of growth** of an algorithm with respect to the input size.

## Why do we use Time Complexity?

- To compare the efficiency of different algorithms.
- To predict how an algorithm performs for large inputs.
- To write optimized and scalable programs.



## Cases of Time Complexity

- Best Case → Ω (Omega)
- Average Case → Θ (Theta)
- Worst Case → O (Big-O)

> In Data Structures and Algorithms (DSA), we generally calculate the **Worst Case Time Complexity (Big-O notation)** because it guarantees the maximum time an algorithm can take in the worst possible scenario.

---

## Rules for Calculating Time Complexity

- Always calculate the **Worst Case Time Complexity** unless the question specifies otherwise.
- Ignore constant factors.
  - Example: `O(2n)` → `O(n)`
- Ignore lower-order terms.
  - Example: `O(n² + n)` → `O(n²)`
- Focus only on the term with the highest growth rate.
- Time complexity depends on how the number of operations grows with the input size, not on the actual execution time.

---

## Common Time Complexities

| Complexity | Name |
|------------|------|
| O(1) | Constant |
| O(log n) | Logarithmic |
| O(n) | Linear |
| O(n log n) | Linearithmic |
| O(n²) | Quadratic |
| O(n³) | Cubic |
| O(2ⁿ) | Exponential |
| O(n!) | Factorial |

---

## Common Python List Operation Complexities

| Operation | Time Complexity |
|----------|-----------------|
| Get Item (`list[i]`) | O(1) |
| Set Item (`list[i] = x`) | O(1) |
| Get Length (`len(list)`) | O(1) |
| Append | O(1) *(Amortized)* |
| Pop Last | O(1) |
| Pop Intermediate | O(n) |
| Insert | O(n) |
| Delete (`del list[i]`) | O(n) |
| Remove | O(n) |
| Search (`in`) | O(n) |
| Copy | O(n) |
| Get Slice | O(k) |
| Set Slice | O(k + n) |
| Delete Slice | O(n) |
| Concatenate (`+`) | O(n + m) |
| Multiply (`list * k`) | O(n × k) |
| Reverse | O(n) |
| Sort | O(n log n) |
| Min | O(n) |
| Max | O(n) |

---

# What is Space Complexity?

Space complexity measures the total amount of memory required by an algorithm as the input size increases.

It consists of two parts:

- **Input Space**
- **Auxiliary Space**

### Input Space

The memory required to store the input data.

### Auxiliary Space

The extra memory used by the algorithm to solve the problem, excluding the input space.

### Rules for Space Complexity

- Space complexity is also represented using **Big-O notation**.
- Count only the memory required by the algorithm.
- Ignore constant-sized variables.
- Focus on how memory usage grows as the input size increases.
- Unless the question specifically allows it, we should **not modify the input values**. Instead, we use additional variables if needed.

---

# What I Learned

- What Time Complexity is.
- What Space Complexity is.
- Time complexity measures the **rate of increase in running time** with respect to the input size.
- Space complexity measures the **memory required** by an algorithm.
- Difference between Time Complexity and Space Complexity.
- Difference between **Input Space** and **Auxiliary Space**.
- Big-O notation represents the **Worst Case**.
- Omega (Ω) represents the **Best Case**.
- Theta (Θ) represents the **Average Case**.
- In DSA, we usually calculate the **Worst Case Time Complexity**.
- Ignore constant factors while calculating complexity.
- Ignore lower-order terms and keep only the dominant term.
- How nested loops affect time complexity.
- Common Python list operation complexities.
- The importance of writing efficient and scalable algorithms.