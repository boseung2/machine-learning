# 모두의 딥러닝 (조태호) — Modern Edition

조태호 저 『모두의 딥러닝』(길벗) 예제를 **최신 Keras 3 / TensorFlow 2.18**로 재작성하며 공부하는 트랙입니다.

- 책 원본 소스: https://github.com/gilbutITbook/006958
- 환경: Conda `modus-dl`
- Python: 3.11
- 프레임워크: TensorFlow 2.18 + Keras 3 (멀티 백엔드 통합)
- 작업 방식: SSH + VS Code Remote SSH
- 책은 Keras 1.x ~ 2.x 시절(약 10년 전) 코드라 일부 API가 다릅니다. 차이는 [`MIGRATION.md`](MIGRATION.md) 한 곳에 모아둡니다.

## 빠른 실행

```bash
cd /home/ubuntu/bsjung/learning/machine-learning/modus-deep-learning
conda env create -f environment.yml   # 최초 1회
conda activate modus-dl
```

VS Code에서 열 위치:

```text
/home/ubuntu/bsjung/learning/machine-learning/modus-deep-learning
```

VS Code Python interpreter:

```text
/home/ubuntu/miniconda3/envs/modus-dl/bin/python
```

## 구조

```text
modus-deep-learning/
  README.md
  MIGRATION.md         # 책 → Keras 3 API 매핑 (전 챕터 공통)
  environment.yml
  data/                # 책의 6개 CSV (작아서 같이 커밋)
  src/                 # 재사용 모듈 (datasets 등)
  outputs/             # 그래프/체크포인트, git 제외
  part1-basics/        # 책 1~3부 — 이론/수학 (deep_class/ 대응)
  part2-keras/         # 책 4~5부 — Keras 실전 예제 (deep_code/ 대응)
```

각 챕터 폴더는 다음 패턴을 따릅니다.

```text
part1-basics/01-linear-regression/
  notes.md       # 이론 정리
  lab.ipynb      # 책 코드를 최신 Keras 3로 재작성한 실습
```

## Part 1 — 딥러닝 동작 원리 (이론)

원본 `deep_class/` 폴더 대응. 수학과 NumPy로 직접 구현해 보는 부분.

| # | 폴더 | 원본 파일 | 주제 |
| - | ---- | --------- | ---- |
| 1 | `part1-basics/01-linear-regression/` | `01_Linear_Regression.py` | 최소제곱법으로 직선 구하기 |
| 2 | `part1-basics/02-rmse/` | `02_RMSE.py`, `02_Data_preparation.py` | 평균제곱오차 / 데이터 준비 |
| 3 | `part1-basics/03-gradient-descent/` | `03_Gradient_Descent.py` | 경사하강법 |
| 4 | `part1-basics/04-multi-linear-regression/` | `04_Multi-Linear-Regression.py` | 다중 선형회귀 |
| 5 | `part1-basics/05-3d-graph/` | `05_3D_Graph.py` | 다변수 손실 시각화 |
| 6 | `part1-basics/06-logistic-regression/` | `06_Logistic_Regression.py` | 로지스틱 회귀 |
| 7 | `part1-basics/07-multi-logistic-regression/` | `07_Multi_Logistic_Regression.py` | 다중 로지스틱 |
| 8 | `part1-basics/08-xor/` | `08_XOR.py` | 단층 퍼셉트론의 한계 |
| 9 | `part1-basics/09-xor-backprop/` | `09_XOR-backpropagation.py` | 역전파로 XOR 풀기 |

## Part 2 — Keras 실전 예제 (책 4~5부)

폴더 = 책 장 번호. 한 장이 여러 단계로 나뉜 경우 (13/14장), 한 폴더 안에 `lab1-…/lab2-…` 식으로 분할.

| 책 장 | 폴더 | 데이터 | 주제 / 단계 | 원본 파일 |
| - | - | - | - | - |
| 10장 | `part2-keras/ch10-thoracic-surgery/` | ThoraricSurgery.csv | 첫 딥러닝, 수술 후 생존 예측 | `01_My_First_Deeplearning.py` |
| 11장 | `part2-keras/ch11-pima-indians/` | pima-indians-diabetes.csv | EDA + 당뇨병 이진분류 | `02_Data_preparation.py`, `02_Pima_Indian.py` |
| 12장 | `part2-keras/ch12-iris/` | iris.csv | 다중분류 (softmax + categorical_crossentropy) | `03_Iris_Multi_Classfication.py` |
| 13장 | `part2-keras/ch13-sonar/` | sonar.csv | 이진분류 4단계: <br>① baseline ② train/test split ③ 모델 저장/로드 ④ Stratified K-fold | `04-Sonar.py`, `05_Sonar_Train_Test.py`, `06-Sonar-Save-Model.py`, `07_Sonar-K-fold.py` |
| 14장 | `part2-keras/ch14-wine/` | wine.csv | Wine 분류 5단계: <br>① baseline ② Checkpoint ③ 과적합 시각화 ④ EarlyStopping ⑤ Checkpoint + EarlyStopping 조합 | `08_Wine.py`, `09_Wine_Checkpoint.py`, `10_Wine_Overfit_Graph.py`, `11_Wine_Early_Stop.py`, `12_Wine_Check_and_Stop.py` |
| 15장 | `part2-keras/ch15-boston/` | housing.csv | Boston housing 회귀 (MSE / MAE) | `13_Boston.py` |
| 16장 | `part2-keras/ch16-mnist-cnn/` | MNIST (자동 다운로드) | CNN — 손글씨 숫자 분류 (Conv2D + MaxPool) | `14_MNIST_CNN.py` |
| 17장 | `part2-keras/ch17-reuters-rnn/` | Reuters (자동 다운로드) | RNN/LSTM — 뉴스 카테고리 분류 (46-class) | `15_Reuters_LSTM.py` |

## 학습 방식

1. 각 챕터의 `notes.md`에 책 개념을 요약.
2. `lab.ipynb`에서 원본 코드를 **최신 Keras 3로 재작성**해 실행. 책 그대로 돌리려는 시도는 하지 않음.
3. 책과 다르게 쓴 부분이 *반복적인 deprecation*이면 → `../../MIGRATION.md`에만 기록.
4. *그 챕터 고유의 차이*면 → 그 챕터 `notes.md`에 메모.
