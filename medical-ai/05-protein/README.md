# 05 · 단백질 기능 예측 (UNLV Project 3 미니)

## UNLV 프로젝트와의 연결
> "Deep neural networks for protein function predictions"

단백질의 **아미노산 시퀀스**나 **구조**에서 기능(효소 종류, 세포 내 위치 등)을 예측하는 문제. 생물정보학 + NLP의 교차점.

## 추천 데이터셋

### 🥇 1차: **CAFA-style 소규모 subset**
- UniProt + GO (Gene Ontology) terms
- [CAFA 대회](https://biofunctionprediction.org/cafa/) 데이터 혹은 축소판
- Kaggle의 "Protein Function Prediction" 대회 데이터 활용 가능

### 🥈 2차: **DeepLoc** (세포 내 위치 분류)
- ~14,000 단백질, 10 class (nucleus, cytoplasm, ...)
- 작고 잘 정리됨 → 입문용 최적
- [DeepLoc2 dataset](https://services.healthtech.dtu.dk/services/DeepLoc-2.0/)

### 🥉 3차: **Enzyme Commission (EC) number 예측**
- PDB / UniProt에서 enzyme 라벨만 뽑아서 multi-class

## 단계별 계획

### Phase A — 시퀀스 다루기 (2일)
- [ ] FASTA 파일 파싱 (Biopython or 직접)
- [ ] 아미노산 one-hot encoding
- [ ] 시퀀스 길이 통계 / padding 전략

### Phase B — 단순 모델 (2일)
- [ ] **1D-CNN**: 시퀀스에 필터 sliding (유사 motif 검출)
- [ ] **BiLSTM**: 양방향 순차 처리
- [ ] multi-label classification (한 단백질이 여러 GO term 가짐)

### Phase C — Pretrained Protein LM (3일)
- [ ] **ESM-2** (Meta) 또는 **ProtBERT** 사용 — 단백질계의 BERT
- [ ] `huggingface transformers`로 임베딩 추출
- [ ] 임베딩 위에 작은 classifier head 붙여 학습 (transfer learning)
- [ ] 1D-CNN baseline 대비 성능 비교

### Phase D (여유) — 구조 기반 (advanced)
- [ ] AlphaFold 예측 구조 사용
- [ ] GNN 시도 (nodes = residues, edges = contacts)

## 배울 개념 (체크리스트)
- [ ] 아미노산 20종의 생물학적 의미
- [ ] 시퀀스를 텐서로 바꾸는 방법 (one-hot vs embedding)
- [ ] 1D Convolution이 시퀀스에서 하는 일 (motif detection)
- [ ] LSTM의 게이트 구조
- [ ] Transformer의 self-attention
- [ ] **Protein language model**의 pretrain 목적 (masked residue)
- [ ] Multi-label metric: micro/macro F1, Fmax
- [ ] Hierarchical label (GO term은 DAG)

## 참고 자료
- **논문**: Rives et al., "ESM — Biological structure and function emerge from scaling" (2021)
- **논문**: Elnaggar et al., "ProtTrans" (2021)
- **논문**: Kulmanov & Hoehndorf, "DeepGOPlus" (2020)
- **도구**: [Hugging Face - facebook/esm2_t33_650M_UR50D](https://huggingface.co/facebook/esm2_t33_650M_UR50D)

## AI agent에 물어볼 것
1. "GO term의 계층 구조를 활용하면 multi-label 학습이 어떻게 개선될까?"
2. "ESM-2의 pretrain objective가 왜 NLP의 MLM과 달라야 했는지 설명"
3. "단백질 시퀀스 길이가 매우 다양한데 (50~5000) 어떻게 통일해서 배치 학습해?"
4. "Transfer learning에서 pretrained 모델을 freeze할지 fine-tune할지 판단 기준은?"

## 현지 가서 연결되는 것
UNLV 교수/조교가 쓰는 실제 단백질 데이터에 같은 ESM 임베딩 파이프라인을
가져가서 꽂기만 하면 됨. **Phase C까지만 해도 강력한 기반**.
