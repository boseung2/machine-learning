# 밑바닥부터 시작하는 딥러닝 실습

『밑바닥부터 시작하는 딥러닝 1』을 Python, NumPy, Matplotlib로 직접 구현하며 공부하는 공간입니다.

## 참조

- 책 소스 코드 참조용 GitHub: https://github.com/boseung2/deep-learning-from-scratch

이 디렉토리는 위 repo를 clone한 것이 아니라, 직접 공부하며 작성하는 개인 실습 트랙입니다.
필요한 예제 코드는 GitHub에서 웹으로 확인하고, 여기에는 직접 이해하며 작성한 코드와 노트를 남깁니다.

## 위치

```text
/home/ubuntu/bsjung/learning/machine-learning/deep-learning-from-scratch
```

## 환경

Conda 환경 이름:

```text
dlfs
```

주요 패키지:

- Python 3.11
- NumPy
- Matplotlib
- ipykernel

환경 생성:

```bash
cd /home/ubuntu/bsjung/learning/machine-learning/deep-learning-from-scratch
conda env create -f environment.yml
conda activate dlfs
python -m ipykernel install --user --name dlfs --display-name "Python (dlfs)"
```

이미 환경이 만들어져 있다면:

```bash
conda activate dlfs
```

## VS Code Remote SSH 사용

웹 JupyterLab 서버는 사용하지 않습니다.

1. 로컬 VS Code에서 Remote SSH로 서버 접속
2. 이 폴더 열기:

```text
/home/ubuntu/bsjung/learning/machine-learning/deep-learning-from-scratch
```

3. Python interpreter 선택:

```text
/home/ubuntu/miniconda3/envs/dlfs/bin/python
```

또는 VS Code에서 보이는 kernel/interpreter:

```text
Python (dlfs)
```

## 구조

```text
notes/       # 장별 개념 정리
practice/    # 직접 구현하는 .py 코드
notebooks/   # VS Code Jupyter 확장으로 실행할 .ipynb 실험
src/         # 장을 넘어서 재사용할 코드
  common/
  dataset/
data/        # 데이터 파일, git 제외
outputs/     # 그래프/실험 결과, git 제외
```

## 첫 실행 테스트

```bash
cd /home/ubuntu/bsjung/learning/machine-learning/deep-learning-from-scratch
conda activate dlfs
python practice/ch01/hello_numpy.py
```

예상 출력:

```text
Python: ...
NumPy: ...
Matplotlib: ...
x = [0 1 2 3 4]
y = [ 0  1  4  9 16]
saved: outputs/ch01_square.png
```
