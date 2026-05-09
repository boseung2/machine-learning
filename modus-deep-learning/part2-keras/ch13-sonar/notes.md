# Ch 13 — 초음파 광물 예측 (Sonar)

원본: `deep_code/04-Sonar.py` ~ `07_Sonar-K-fold.py`

## 목적
- 같은 데이터(`sonar.csv`)·같은 베이스 모델을 가지고 **검증 방법**을 점진적으로 발전시켜 본다:
  1. **Lab 1** — 학습/검증 분리 없이 전체로 학습 (베이스라인의 함정)
  2. **Lab 2** — `train_test_split` 도입
  3. **Lab 3** — 학습한 모델을 `.keras` 파일로 저장/로드
  4. **Lab 4** — Stratified K-fold 교차검증

## 데이터
- 파일: `data/sonar.csv` (208 rows × 61 cols)
- 입력 60개 (소나 신호 주파수 빈), 라벨 1개 (`R`=암석 / `M`=지뢰)
- 라벨이 문자열이라 `LabelEncoder` 로 0/1 변환 필요

## 베이스 모델 (4 lab 모두 동일)
```text
Input(60) → Dense(24, relu) → Dense(10, relu) → Dense(1, sigmoid)
```

## Keras 1.x → Keras 3 변경
- `from keras.layers.core import Dense` → `from keras.layers import Dense`
- 모델 저장: `.h5` → `.keras` (Keras 3 권장)

## 학습 체크
- [ ] Lab 1의 train accuracy 가 매우 높은데 *왜 신뢰할 수 없는지*
- [ ] Lab 2 의 test accuracy 가 train accuracy 와 얼마나 차이 나는지
- [ ] Lab 3 으로 저장한 모델을 다시 로드해도 같은 정확도가 나오는지
- [ ] Lab 4 의 fold별 정확도 분산을 보고, *데이터 분할에 따라 모델 성능이 얼마나 흔들리는지* 체감
