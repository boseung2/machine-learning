# 책 코드 → Keras 3 마이그레이션 노트

『모두의 딥러닝』(조태호) 원본 코드는 Keras 1.x ~ 2.x (TensorFlow 1.x 시절) 기준이라, **TF 2.18 + Keras 3** 환경에서는 그대로 돌지 않습니다. 챕터별로 같은 패턴이 반복되므로 한 곳에 모아 둡니다.

> 이 문서는 *공통* 차이만 다룹니다. 챕터 고유의 차이(예: 데이터셋 URL 변경)는 해당 챕터 `notes.md`에.

---

## 1. import 경로

```python
# 책
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.datasets import mnist, reuters, imdb
from keras.preprocessing import sequence
```

```python
# Keras 3 (권장)
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.utils import to_categorical, pad_sequences
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.datasets import mnist, reuters, imdb
```

- `keras.utils.np_utils`는 사라졌습니다. `to_categorical`은 `keras.utils.to_categorical`로 직접 import.
- `keras.preprocessing.sequence.pad_sequences` → `keras.utils.pad_sequences`.

## 2. one-hot 변환

```python
# 책
from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train)
```

```python
# Keras 3
from keras.utils import to_categorical
y_train = to_categorical(y_train)
# 또는: 원-핫 없이 sparse_categorical_crossentropy 손실 사용
```

## 3. `predict_classes` 제거

```python
# 책 (Keras 2.5에서 deprecated, 이후 제거)
preds = model.predict_classes(x)
```

```python
# Keras 3
import numpy as np
probs = model.predict(x)
preds = np.argmax(probs, axis=-1)         # 다중분류
# preds = (probs > 0.5).astype("int32")   # 이진분류 (sigmoid 출력)
```

## 4. 옵티마이저 인자

```python
# 책
from keras.optimizers import Adam
opt = Adam(lr=0.001)                       # 'lr'은 더 이상 인식 안 됨
```

```python
# Keras 3
from keras.optimizers import Adam
opt = Adam(learning_rate=0.001)
```

문자열로 지정해도 됩니다: `model.compile(optimizer="adam", ...)`.

## 5. `ModelCheckpoint` 인자

```python
# 책
ModelCheckpoint(filepath="...{epoch:02d}-{val_loss:.4f}.hdf5",
                monitor="val_loss",
                verbose=1,
                save_best_only=True,
                period=1)                  # 'period' 제거됨
```

```python
# Keras 3
ModelCheckpoint(filepath="...{epoch:02d}-{val_loss:.4f}.keras",  # .hdf5 → .keras 권장
                monitor="val_loss",
                verbose=1,
                save_best_only=True,
                save_freq="epoch")         # period 대체
```

- 기본 저장 포맷이 **`.keras`** (zip 기반)로 바뀌었습니다. `.h5`/`.hdf5`도 여전히 가능하지만 권장 X.
- `model.save("foo.keras")` / `keras.models.load_model("foo.keras")`.

## 6. `fit()` 반환값과 history

```python
# 동일 — 변하지 않음
history = model.fit(x, y, epochs=200, validation_split=0.25, verbose=0)
print(history.history.keys())  # ['loss', 'accuracy', 'val_loss', 'val_accuracy']
```

단, **메트릭 키가 `acc` → `accuracy`** 로 바뀐 지 오래입니다 (Keras 2.3+). 책의 `history.history['acc']`는 `history.history['accuracy']`로.

## 7. 데이터 로딩 — `np.loadtxt` 대신 `pandas`

책은 종종 `np.loadtxt(..., delimiter=",")`를 쓰는데, CSV에 헤더가 있는 파일은 깨집니다. 통일해서 `pandas`로:

```python
import pandas as pd
df = pd.read_csv("data/wine.csv", header=None)
X = df.iloc[:, 0:12].to_numpy()
y = df.iloc[:, 12].to_numpy()
```

## 8. 시드 설정

```python
# 책
import numpy
import tensorflow as tf
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(seed)
```

```python
# Keras 3 (권장 — 한 줄로 모든 백엔드/RNG 시드)
import keras
keras.utils.set_random_seed(42)
```

## 9. 모델 입력 shape 지정

Keras 3에서는 `Sequential`의 첫 레이어에 `input_dim=` / `input_shape=` 대신 명시적 `Input` 레이어를 권장합니다.

```python
# 책 / Keras 2 스타일 — Keras 3에서도 동작은 함 (deprecation warning)
model = Sequential()
model.add(Dense(30, input_dim=17, activation="relu"))
```

```python
# Keras 3 권장
from keras import Input
model = Sequential([
    Input(shape=(17,)),
    Dense(30, activation="relu"),
    Dense(1, activation="sigmoid"),
])
```

## 10. `keras.preprocessing.sequence.pad_sequences`

```python
# 책
from keras.preprocessing import sequence
x_train = sequence.pad_sequences(x_train, maxlen=100)
```

```python
# Keras 3
from keras.utils import pad_sequences
x_train = pad_sequences(x_train, maxlen=100)
```

## 11. Embedding의 `input_length`

```python
# 책
Embedding(1000, 100, input_length=100)
```

```python
# Keras 3 — input_length는 deprecated. 모델 빌드는 첫 fit에서 자동 추론
Embedding(input_dim=1000, output_dim=100)
# 명시하고 싶으면 Input(shape=(100,))를 위에 둠
```

## 12. `model.summary()` / 그래프 시각화

`keras.utils.plot_model`은 그대로. `pydot`, `graphviz` 시스템 패키지가 필요한 점만 동일.

---

## 빠른 체크리스트 (챕터 시작할 때 훑어보기)

- [ ] `np_utils` → `to_categorical` 직접 import
- [ ] `predict_classes` → `np.argmax(model.predict(x), axis=-1)`
- [ ] `Adam(lr=...)` → `Adam(learning_rate=...)`
- [ ] `ModelCheckpoint(period=...)` → `save_freq="epoch"`, 파일 확장자 `.keras`
- [ ] `history.history['acc']` → `history.history['accuracy']`
- [ ] `Sequential([Input(shape=...), ...])` 패턴 사용
- [ ] `keras.utils.set_random_seed(42)`로 시드 일괄 설정
- [ ] `pad_sequences`는 `keras.utils`에서 import
