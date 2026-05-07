# Machine Learning Study

머신러닝/딥러닝을 주제별로 실습하고 정리하는 학습 저장소입니다.

## 학습 트랙

### `deep-learning-from-scratch/`

『밑바닥부터 시작하는 딥러닝 1』을 Python, NumPy, Matplotlib 중심으로 직접 구현하며 공부하는 공간입니다.

- 환경: Conda `dlfs`
- Python: 3.11
- 주요 패키지: NumPy, Matplotlib, ipykernel
- 작업 방식: SSH + VS Code Remote SSH
- 웹 JupyterLab 서버는 사용하지 않음
- 책 소스 코드 참조: https://github.com/boseung2/deep-learning-from-scratch

빠른 실행:

```bash
cd /home/ubuntu/bsjung/learning/machine-learning/deep-learning-from-scratch
conda activate dlfs
python practice/ch01/hello_numpy.py
```

VS Code에서 열 위치:

```text
/home/ubuntu/bsjung/learning/machine-learning/deep-learning-from-scratch
```

VS Code Python interpreter:

```text
/home/ubuntu/miniconda3/envs/dlfs/bin/python
```

또는 kernel:

```text
Python (dlfs)
```

구조:

```text
deep-learning-from-scratch/
  README.md          # 실습 트랙 설명
  environment.yml    # dlfs conda 환경 정의
  notes/             # 장별 개념 정리
  practice/          # 직접 구현하는 .py 코드
  notebooks/         # VS Code에서 실행하는 .ipynb 실험
  src/               # 재사용 코드
  data/              # 데이터, git 제외
  outputs/           # 그래프/실험 결과, git 제외
```

### `everyones-ml/`

Sung Kim 교수님의 [모두를 위한 머신러닝/딥러닝](https://hunkim.github.io/ml/) 강의를 따라가며 정리/실습하는 공간입니다.

- 환경: Conda `everyones-ml`
- Python: 3.11
- 프레임워크: TensorFlow 2.x (tf.keras 중심, 원본 강의는 1.x)
- 작업 방식: SSH + VS Code Remote SSH

빠른 실행:

```bash
cd /home/ubuntu/bsjung/learning/machine-learning/everyones-ml
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

구조:

```text
everyones-ml/
  README.md          # 트랙 설명, 강의 목록
  environment.yml    # everyones-ml conda 환경 정의
  season1/           # 시즌 1 - 딥러닝의 기본 (Lec 1~12)
  season-rl/         # 시즌 RL - Deep Reinforcement Learning
  season-nlp/        # 시즌 NLP - Deep NLP
  src/               # 재사용 모듈
  data/              # 데이터, git 제외
  outputs/           # 그래프/실험 결과, git 제외
```

각 강의 폴더(`lecXX-*/`) 안에 `notes.md`(이론)와 `lab.ipynb`(실습)을 함께 둡니다.

### `medical-ai/`

의료 AI 학습 커리큘럼입니다.

- 환경 설정
- 전통적 머신러닝
- PyTorch basics
- pathology, survival, protein, EHR 등 주제별 확장

### `healthcare-analytics/`

헬스케어 분석을 위한 머신러닝 실습입니다.

### `jupyter-test/`

Jupyter 실행 테스트용 노트북 공간입니다.

## 공통 규칙

- 큰 데이터와 산출물은 git에 올리지 않습니다.
- 각 학습 트랙은 자체 README나 notes를 통해 실행 방법을 남깁니다.
- 실험 결과 이미지는 `outputs/` 아래에 저장하고, 필요한 경우만 선별해서 문서에 포함합니다.
- VS Code Remote SSH로 접속해 각 트랙 디렉토리를 열고, 해당 Conda/Python 환경을 선택해 실행합니다.
