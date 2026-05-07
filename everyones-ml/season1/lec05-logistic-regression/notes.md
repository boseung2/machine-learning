# Lec 5 — Logistic (Regression) Classification

## 핵심 키워드
- Sigmoid: g(z) = 1 / (1 + e^-z)
- Hypothesis: H(X) = sigmoid(XW + b)
- Cost: -y log(H) - (1-y) log(1-H) (Binary cross-entropy)

## 학습 메모

## 실습 메모 (TF 2.x)
- `tf.keras.layers.Dense(1, activation='sigmoid')`
- Loss: `tf.keras.losses.BinaryCrossentropy()`
