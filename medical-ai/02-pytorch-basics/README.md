# 02 · PyTorch Basics

## 목표
PyTorch의 "빌딩 블록"을 익혀서, Layer 3 이후의 모든 미니 프로젝트에서
**모델 구조만 바꿔 끼워 쓸 수 있게** 만든다.

## 노트북
| # | 파일 | 주제 |
|---|---|---|
| 01 | `01_tensors_and_autograd.ipynb` | Tensor, 자동 미분, 경사하강 한 번 직접 |
| 02 | `02_mlp_tabular.ipynb` | MLP로 Breast Cancer 풀기 (Layer 1 XGBoost와 비교) |
| 03 | `03_cnn_mnist.ipynb` | CNN 입문 (Project 1 병리 이미지 준비) |

## 배울 개념 (체크리스트)
- [ ] `torch.Tensor` vs `np.ndarray`의 차이
- [ ] `requires_grad=True` → `.backward()` → `.grad` 자동 미분 흐름
- [ ] `nn.Module`을 상속해서 모델 만들기
- [ ] `Dataset` / `DataLoader`로 batch 처리
- [ ] 학습 루프: zero_grad → forward → loss → backward → step
- [ ] Loss 함수: `CrossEntropyLoss`, `BCEWithLogitsLoss`, `MSELoss`
- [ ] Optimizer: `SGD`, `Adam`
- [ ] Train/eval 모드 전환 (`model.train()` / `model.eval()`)
- [ ] GPU/MPS로 옮기기 (`.to(device)`)
- [ ] CNN의 Conv2d → Pool → Conv2d → Flatten → Linear 패턴

## 끝내면 생길 질문
- "왜 batch 크기가 성능에 영향을 줘?"
- "learning rate 스케줄링은 뭘 하는 거야?"
- "Dropout / BatchNorm은 언제 넣어?"

→ 이 질문들은 Layer 3에서 실제 프로젝트 돌리며 감을 잡는다.
