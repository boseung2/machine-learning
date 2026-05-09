# Ch 14 — 와인 종류 예측 (5단계)

원본: `deep_code/08_Wine.py` ~ `12_Wine_Check_and_Stop.py`

## 목적
- 같은 와인 데이터·같은 기본 모델로 **콜백(callback)** 도입을 점진적으로 학습:
  1. **Lab 1** — Wine baseline (전체 데이터, 콜백 없음)
  2. **Lab 2** — `ModelCheckpoint` — best 모델 자동 저장
  3. **Lab 3** — 일부러 데이터를 줄여 **과적합을 시각화** (책 10장)
  4. **Lab 4** — `EarlyStopping` — 자동 학습 중단
  5. **Lab 5** — Checkpoint + EarlyStopping **조합**

## 데이터
- 파일: `data/wine.csv` (6497 rows × 13 cols)
- 입력 12개 (와인 화학 측정값), 라벨 1개 (0=화이트 / 1=레드)

## 베이스 모델
```text
Input(12) → Dense(30, relu) → Dense(12, relu) → Dense(8, relu) → Dense(1, sigmoid)
```

## Keras 1.x → Keras 3 변경
- 체크포인트: `{epoch:02d}-{val_loss:.4f}.hdf5` → `.keras`
- `ModelCheckpoint` 의 `period` 인자는 제거됨 → `save_freq="epoch"`
- `history.history['acc']` → `'accuracy'`
- `df.sample(frac=0.15)` 에 `random_state=0` 명시 (책은 안 함, 재현성 위해)

## 학습 체크
- [ ] Lab 1과 Lab 3의 차이 — 데이터 양이 줄면 학습 곡선이 어떻게 변하는가
- [ ] Lab 2가 저장한 체크포인트 파일 이름 (`{epoch}-{val_loss}`) 의미 이해
- [ ] Lab 4의 EarlyStopping 이 `patience=100` 인 이유 — 와인 데이터의 변동성
- [ ] Lab 5에서 두 콜백의 역할이 다름을 이해 (저장 vs 중단)
