# Lec 2 — Linear Regression의 개념 / Lab — TensorFlow로 구현

## 핵심 키워드
- Hypothesis: H(x) = Wx + b
- Cost / Loss function (MSE)
- Goal: minimize cost(W, b)

## 학습 메모

## 실습 메모 (TF 2.x)
- `tf.Variable`로 W, b 정의
- `tf.GradientTape`로 수동 학습 또는 `tf.keras.Sequential([tf.keras.layers.Dense(1)])`
