# Ch 12 — 아이리스 품종 예측 (다중분류)

원본: `deep_code/03_Iris_Multi_Classfication.py`

## 목적
- **다중분류 (multi-class)** 의 표준 패턴: softmax 출력 + categorical_crossentropy.
- 문자열 라벨 → 정수 인코딩 (LabelEncoder) → 원-핫.

## 데이터
- 파일: `data/iris.csv` (150 rows × 5 cols)
- 컬럼: sepal_length, sepal_width, petal_length, petal_width, **species** (라벨, 문자열)
- 라벨 값: `Iris-setosa`, `Iris-versicolor`, `Iris-virginica`

## 핵심 변경 (Keras 1.x → Keras 3)
- `from keras.utils import np_utils` → `from keras.utils import to_categorical`
- `from keras.layers.core import Dense` → `from keras.layers import Dense` (`.core` 경로는 deprecated)

## 모델
```text
Input(4) → Dense(16, relu) → Dense(3, softmax)
```

## 학습 체크
- [ ] pairplot에서 어느 두 특징이 가장 잘 분리되는지 (petal_length vs petal_width 추천)
- [ ] LabelEncoder 가 `[setosa, versicolor, virginica]` 를 `[0, 1, 2]` 로 매핑하는지
- [ ] 원-핫된 라벨 shape 확인 `(150, 3)`
