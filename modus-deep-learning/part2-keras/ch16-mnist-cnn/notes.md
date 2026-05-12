# Ch 16 — MNIST 손글씨 분류 (CNN)

원본: `deep_code/14_MNIST_CNN.py`

## 목적
- **합성곱 신경망 (Convolutional Neural Network)** 의 첫 실전 적용.
- 이미지 데이터(2D 픽셀 행렬)에 Dense 만 쓰면 위치 정보가 깨짐 → Conv2D 가 그걸 보존.
- 핵심 구성요소: `Conv2D`, `MaxPooling2D`, `Dropout`, `Flatten`.

## 데이터
- `keras.datasets.mnist.load_data()` — 첫 실행 시 ~11MB 자동 다운로드 (`~/.keras/datasets/`).
- 학습 60,000 / 테스트 10,000장, 28×28 grayscale, 라벨 0~9 (10 클래스).
- 균형 잡힌 데이터셋 (각 클래스 ~6,000장).

## 핵심 변경 (Keras 1.x → Keras 3)
- `from keras.layers.convolutional import Conv2D, MaxPooling2D` → `from keras.layers import Conv2D, MaxPooling2D`
- `from keras.utils import np_utils` 제거 → `sparse_categorical_crossentropy` 사용 시 one-hot 변환 자체 불필요.
- 입력 shape: 책은 `(28, 28, 1)` reshape 명시. Keras 3 도 동일하나 `dtype="float32"` 와 `/255.0` 정규화를 명시적으로 함.

## 책과 다르게 가는 부분
- 손실 함수: `categorical_crossentropy` + `to_categorical` 대신 `sparse_categorical_crossentropy` + 정수 라벨 그대로 사용 (메모리·코드 절약).
- 데이터 증강(augmentation)은 다루지 않음 — 책의 14장 범위 유지.

## 모델
```text
Input(28, 28, 1)
 → Conv2D(32, (3,3), relu)
 → Conv2D(64, (3,3), relu)
 → MaxPool(2,2)
 → Dropout(0.25)
 → Flatten
 → Dense(128, relu)
 → Dropout(0.5)
 → Dense(10, softmax)
```

총 파라미터 약 1.2M. CPU 에서 5 epoch ~5-8분.

## Conv2D 의 의미 (한 줄씩)
- `Conv2D(32, (3,3))` — 3×3 필터 32개를 슬라이딩. 출력 채널 32개. 각 필터가 "특정 패턴이 있는지" 검사.
- `MaxPool(2,2)` — 2×2 영역에서 최대값 하나. 공간 해상도 절반 → 위치 변화에 둔감해지면서 채널 정보는 유지.
- `Dropout(0.25)` — 학습 중에만 25% 뉴런 끄기. 과적합 방지.
- `Flatten` — (H, W, C) 3D 텐서를 1D 로 펴기. Dense 로 넘기기 직전에 필수.

## 학습 체크
- [ ] 첫 Conv2D 의 출력 shape 가 `(26, 26, 32)` 인지 — 28×28 에 3×3 필터 적용하면 양쪽 1픽셀씩 잘려서 26.
- [ ] MaxPool 후 shape 가 `(12, 12, 64)` 인지.
- [ ] test accuracy 가 0.99 근처까지 가는지 — MNIST 에서 CNN 으로 그 정도는 표준.
- [ ] 틀린 샘플 시각화에서 사람도 헷갈릴 만한 4↔9, 3↔5, 7↔1 케이스가 보이는지.
