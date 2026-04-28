# 03 · 병리 이미지 암 분류 (UNLV Project 1 미니)

## UNLV 프로젝트와의 연결
> "Pathological Image Analysis for Cancer Classification"

진짜 병리 영상(Whole-Slide Image, WSI)은 한 장이 수 GB. 우리는 **패치 단위로 잘린 공개 데이터**로 같은 원리를 연습한다.

## 추천 데이터셋

### 🥇 1차 추천: **PatchCamelyon (PCam)**
- 96×96 RGB, 327,680장, 림프절 전이 이진 분류 (H&E 염색)
- `torchvision.datasets.PCAM`으로 한 줄 다운로드 가능
- 진짜 의료 영상 + 가벼움 + 잘 연구된 벤치마크 → 끝판왕 튜토리얼 데이터

### 2차: **MedMNIST v2**
- 여러 의료 영상 (PathMNIST, BloodMNIST, DermaMNIST 등) 을 MNIST 형식으로
- 가볍고 여러 도메인 한 번에 체험
- `pip install medmnist`

### 고급: **Camelyon16** (WSI 원본)
- 진짜 WSI (Whole-Slide Image) — Nevada 가서 실제로 쓸 가능성 높음
- 전처리: `openslide`, `histolab`으로 패치 추출

## 단계별 계획

### Phase A — 베이스라인 (1~2일)
- [ ] PCam 소량(1만 장) 로드 후 간단 CNN으로 분류
- [ ] `02-pytorch-basics/03_cnn_mnist.ipynb`의 `SmallCNN`을 거의 그대로 (채널 1→3, 입력 96×96)
- [ ] 테스트셋 AUROC 측정

### Phase B — Transfer Learning (2~3일)
- [ ] `torchvision.models.resnet18(weights=...)` 로드
- [ ] 마지막 FC layer만 새 task에 맞게 교체
- [ ] `requires_grad=False`로 백본 얼리고 fine-tune
- [ ] 베이스라인 대비 AUROC 얼마나 뛰는지 기록

### Phase C — 개선 요소 하나씩 (2~3일)
- [ ] Data augmentation: random flip, rotation, color jitter (병리는 stain 편차 큼)
- [ ] **Stain normalization** (Macenko/Vahadane) — 병리 이미지 특화
- [ ] 더 큰 backbone (ResNet50 / ViT-B)
- [ ] Cosine LR schedule + Early stopping

### Phase D — 해석 (1일)
- [ ] Grad-CAM으로 "모델이 어느 영역을 보고 전이라고 판단했나" 시각화
- [ ] 잘못 분류한 샘플들 눈으로 확인 → 패턴 발견

## 배울 개념 (체크리스트)
- [ ] `torchvision.transforms`의 augmentation 파이프라인
- [ ] Pretrained model의 feature extractor vs fine-tuning 차이
- [ ] ImageNet pretrain이 의료 영상에 적용 가능한 이유와 한계
- [ ] AUROC, Sensitivity, Specificity 의학적 의미
- [ ] Grad-CAM 원리

## 참고 자료
- **논문**: Veeling et al., "Rotation Equivariant CNNs for Digital Pathology" (2018) — PCam 소개 논문
- **논문**: He et al., "Deep Residual Learning" (2015) — ResNet
- **블로그**: [PatchCamelyon benchmark leaderboard](https://github.com/basveeling/pcam)

## AI agent에 물어볼 것
1. "PCam 데이터의 양성 샘플이 뭘 의미하는지 의학적으로 자세히 설명해줘 (metastasis)"
2. "Stain normalization이 왜 필요한지 이미지 예시로 보여줘"
3. "ResNet의 residual connection이 왜 깊은 네트워크를 가능하게 했는지 수식 흐름으로"
4. "Grad-CAM이 내부적으로 어떤 gradient를 쓰는지 설명해줘"

## 현지 가서 연결되는 것
UNLV에서 받을 실제 WSI / 바이오이미지 데이터셋에 여기서 만든 파이프라인을
**그대로 가져가서** 입출력만 바꿔 쓸 수 있다. 템플릿 확보가 목적.
