# 모두를 위한 머신러닝/딥러닝 (Everyone's ML)

Sung Kim 교수님의 [모두를 위한 머신러닝/딥러닝](https://hunkim.github.io/ml/) 강의를 따라가며 정리/실습하는 트랙입니다.

- 환경: Conda `everyones-ml`
- Python: 3.11
- 프레임워크: TensorFlow 2.x (tf.keras 중심)
- 작업 방식: SSH + VS Code Remote SSH
- 강의는 TensorFlow 1.x 기반이지만, 실습은 2.x로 마이그레이션해서 진행합니다.

## 빠른 실행

```bash
cd /home/ubuntu/bsjung/learning/machine-learning/everyones-ml
conda env create -f environment.yml   # 최초 1회
conda activate everyones-ml
```

VS Code에서 열 위치:

```text
/home/ubuntu/bsjung/learning/machine-learning/everyones-ml
```

VS Code Python interpreter:

```text
/home/ubuntu/miniconda3/envs/everyones-ml/bin/python
```

## 구조

```text
everyones-ml/
  README.md
  environment.yml
  season1/        # 시즌 1 - 딥러닝의 기본 (Lec 1~12)
  season-rl/      # 시즌 RL - Deep Reinforcement Learning
  season-nlp/     # 시즌 NLP - Deep NLP
  src/            # 재사용 모듈
  data/           # 데이터, git 제외
  outputs/        # 그래프/실험 결과, git 제외
```

각 강의 폴더는 다음 패턴을 따릅니다.

```text
season1/lec02-linear-regression/
  notes.md       # 이론 정리
  lab.ipynb      # 실습 노트북 (강의 진행 시 추가)
```

Lab이 여러 개인 강의는 `lab1-*.ipynb`, `lab2-*.ipynb` 식으로 나눕니다.

## 시즌 1 - 딥러닝의 기본

| # | 폴더 | 주제 |
| - | ---- | ---- |
| 1 | `season1/lec01-ml-intro/` | 머신러닝의 개념과 용어 + TF 기본 |
| 2 | `season1/lec02-linear-regression/` | Linear Regression |
| 3 | `season1/lec03-cost-minimize/` | Cost 최소화 (Gradient Descent) |
| 4 | `season1/lec04-multi-variable-lr/` | Multi-variable LR + 파일 로딩 |
| 5 | `season1/lec05-logistic-regression/` | Logistic Regression |
| 6 | `season1/lec06-softmax/` | Softmax (Multinomial) |
| 7 | `season1/lec07-ml-tips/` | Learning rate, Overfitting, MNIST |
| 8 | `season1/lec08-dl-basics/` | 딥러닝 기본 개념 (XOR, Backprop 역사) |
| 9 | `season1/lec09-nn-xor-backprop/` | NN으로 XOR + Backpropagation + TensorBoard |
| 10 | `season1/lec10-relu-init-dropout/` | ReLU, 초기화, Dropout, MNIST 98% |
| 11 | `season1/lec11-cnn/` | CNN (MNIST 99% / 99.5%) |
| 12 | `season1/lec12-rnn/` | RNN (Hi Hello, Long Seq, Time Series) |

## 시즌 RL - Deep Reinforcement Learning

| # | 폴더 | 주제 |
| - | ---- | ---- |
| 1 | `season-rl/lec01-overview/` | 수업의 개요 |
| 2 | `season-rl/lec02-openai-gym/` | OpenAI Gym |
| 3 | `season-rl/lec03-dummy-q-learning/` | Dummy Q-learning (table) |
| 4 | `season-rl/lec04-q-learning-exploit/` | Exploit & Exploration, Discounted Reward |
| 5 | `season-rl/lec05-q-learning-nondeterministic/` | Non-deterministic Q-learning |
| 6 | `season-rl/lec06-q-network/` | Q-Network (Frozen Lake, Cart Pole) |
| 7 | `season-rl/lec07-dqn/` | DQN (NIPS 2013 / Nature 2015 / Pacman) |

## 시즌 NLP - Deep NLP

| 폴더 | 주제 |
| ---- | ---- |
| `season-nlp/lec00-overview/` | 수업의 개요 |
| `season-nlp/bot-lab1-api-ai/` | API.ai 개념 + 사용해보기 |

## 공통 규칙

- 큰 데이터와 산출물은 git에 올리지 않습니다 (`data/`, `outputs/`).
- 각 강의 폴더의 `notes.md`에 핵심 개념과 한 줄 요약을 남깁니다.
- 실습 노트북 출력 그래프는 `outputs/<season>/<lec>/`로 저장합니다.
