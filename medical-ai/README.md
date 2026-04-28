# Medical AI Study — UNLV 2026 대비

2026년 여름 UNLV(네바다주립대) 빅데이터 컨소시엄 해외 연구 프로그램
(Dr. Mingon Kang 연구실, 6/22 ~ 7/17) 대비 학습 워크스페이스.

## 학습 철학
**Application → 내부 원리 (하향식)**. 먼저 돌아가는 코드를 만들고,
그 다음 "이게 왜 되지?"라는 질문을 AI agent에게 던지며 한 층씩 파고든다.

## 타겟: UNLV 4개 프로젝트
| # | 프로젝트 | 데이터 | 핵심 모델 | 폴더 |
|---|---|---|---|---|
| 1 | 병리 이미지 암 분류 | 의료 영상 | CNN / ViT | `03-pathology/` |
| 2 | 유전체 기반 생존 분석 | 고차원 tabular | Cox + DNN (DeepSurv) | `04-survival/` |
| 3 | 단백질 기능 예측 | 시퀀스 / 그래프 | Transformer / GNN | `05-protein/` |
| 4 | EHR 분석 | 시계열 의료 기록 | RNN / Transformer | `06-ehr/` |

## 학습 경로
```
00-setup          ← 환경 확인 (30분)
   ↓
01-classical-ml   ← Layer 1: scikit-learn으로 의료 tabular 데이터 돌리기 (1~2주)
   ↓
02-pytorch-basics ← Layer 2: PyTorch 기초 + 신경망 기본기 (1주)
   ↓
03-pathology      ← Layer 3a: Project 1 미니 (1주)
04-survival       ← Layer 3b: Project 2 미니 (1주)
05-protein        ← Layer 3c: Project 3 미니 (1주)
06-ehr            ← Layer 3d: Project 4 미니 (1주)
```

## 타임라인 (권장)
- **~5월 중순**: Layer 1 ~ 2 완료 (classical ML + PyTorch 기본기)
- **~6월 중순**: Layer 3에서 최소 2개 미니 프로젝트 완료 (병리 이미지 + 생존 분석 추천)
- **6/22 ~ 7/17**: UNLV 현지 프로그램 — 남은 2개는 현지에서 실전으로

## 셋업
```bash
cd /Users/boseung/machine-learning/medical-ai
pip install -r requirements.txt
jupyter lab
```

## 학습 메서드
1. **쓰기 먼저, 이해는 나중** — 각 노트북을 끝까지 돌린 뒤 "왜?"를 묻는다.
2. **에러 로그를 스승으로** — 에러를 AI agent에게 그대로 붙여넣고 "원인+수정+왜 나는지" 요청.
3. **주 1편 논문** — 각 Layer 진입 시 seminal paper 요약 요청 (ResNet, DeepSurv, Attention Is All You Need 등).
4. **노트북은 재활용** — UNLV 현지에서 코드 템플릿으로 그대로 쓸 수 있도록 깔끔하게.
