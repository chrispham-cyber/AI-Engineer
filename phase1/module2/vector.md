# Linear Algebra

## Vector
A vector is a sequence of numbers, representing:
- Direction + magnitude (geometrically)
- A point in space (algebraically)
- A list of features (in ML)

In AI, vectors represent:
- Images: Each pixel = 1 dimension → a 28x28 image = a 784-dimensional vector
- Text: Each word → a vector of ~300–1536 dimensions 
- User: [age, gender, income, ...] = a vector

## Operators
```
import numpy as np

# 3D vector
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Geometry: Place one vector end-to-end with another.
v1 + v2
v1 - v2

# Geometry: Stretch / Shrink / Invert.
v1 * 3
-v1

# Magnitude
# L2 norm (Euclidean) — default
np.linalg.norm(v1)        

# L1 norm (Manhattan)
np.linalg.norm(v1, ord=1)  

# Dot Product 
dot = np.dot(v1, v2) 

# or
dot = v1 @ v2

Meaning:
= 0: The two vectors are orthogonal.
> 0: Same direction (angle < 90°).
< 0: Opposite direction.
```

### Cosine Similarity — Build RAG
```
def cosine_similarity(a, b):
return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Question and documents
question = np.array([0.5, 0.8, 0.1, 0.3])
doc1 = np.array([0.4, 0.7, 0.2, 0.4])    # similar
doc2 = np.array([0.1, 0.1, 0.9, 0.8])    # very different

cosine_similarity(question, doc1)   # ~0.97 (very similar)
cosine_similarity(question, doc2)   # ~0.42 (unrelated)
```

Practical Reason: When you build a RAG system, this is how the system "knows" which documents are relevant to a query.

## Matrix
```
M = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

M.shape    # (2, 3) — 2 rows, 3 columns
```

In AI, matrix representations include:
- Datasets: each row represents a sample, each column represents a feature.
- Grayscale images: an HxW matrix.
- Color images: a 3D tensor (H, W, 3).
- Neural network weights.

## Matrix Operators
```
# Element-wise 
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A + B      
A * B       
A ** 2     

# Matrix Multiplication 
A @ B
np.matmul(A, B)
np.dot(A, B)

# Rule : (m, n) @ (n, p) → (m, p). The number of columns of A must equal the number of rows of B.

# Transpose
A.T

# Identity matrix
I = np.eye(3)
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]

# A @ I = A

# Inverse
A = np.array([[1, 2], [3, 5]]) [[a, b], [c, d]]
A_inv = np.linalg.inv(A) # [[d -b], [-c ,a]]

# Determinant (ad - bc)
np.linalg.det(A)

# Trace (diagonal summary)
np.trace(A)
```

| Determinant | Meaning                     |
| ----------- | --------------------------- |
| `0`         | singular, không invert được |
| `> 0`        | orientation preserved       |
| `< 0`        | orientation flipped         |
