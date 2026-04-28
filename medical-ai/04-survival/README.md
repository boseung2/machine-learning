# 04 · 유전체 기반 생존 분석 (UNLV Project 2 미니)

## UNLV 프로젝트와의 연결
> "Deep Learning-Based Survival Analysis Using Genomic Data"

**생존 분석(Survival Analysis)** 은 분류/회귀와 전혀 다른 문제 유형:
- 타겟: "사건(사망/재발)까지 걸린 시간"
- **censoring**: 관측 기간 내에 사건이 안 일어난 환자도 쓸 수 있어야 함
- 지표: **C-index** (concordance)

Dr. Mingon Kang 연구실의 주요 테마 중 하나. 여기서 **가장 깊게 파는 것**을 추천.

## 추천 데이터셋

### 🥇 1차 추천: **lifelines 내장 데이터셋**
- `from lifelines.datasets import load_rossi, load_gbsg2, load_waltons`
- 수십~수백 샘플, 몇 개 feature. 개념 체득용.

### 🥈 2차: **TCGA subset via cBioPortal**
- Breast cancer (BRCA), Glioma (LGG) 등
- [cBioPortal Web UI](https://www.cbioportal.org/)에서 clinical + expression 다운로드
- 수백 환자 × 수만 유전자 (고차원/저샘플) — **진짜 도전**
- 참고: `pycox` 패키지의 METABRIC 예제 (고전적 벤치마크)

### 🥉 3차: **SUPPORT / FLCHAIN** (pycox 내장)
- 중환자 사망 / 혈청 단백질 — 튜토리얼로 자주 쓰임

## 단계별 계획

### Phase A — 고전 생존 분석 (2~3일)
- [ ] Kaplan-Meier: 그룹별 생존 곡선 그리기
- [ ] Log-rank test: 두 그룹 차이 통계적 검정
- [ ] **Cox Proportional Hazards** (lifelines의 `CoxPHFitter`)
- [ ] hazard ratio 해석

### Phase B — 딥러닝 생존 모델 (2~3일)
- [ ] **DeepSurv** (Katzman et al. 2018) — Cox의 linear predictor를 MLP로 교체
- [ ] `pycox` 라이브러리로 구현 (`CoxPH` 클래스)
- [ ] 고전 Cox vs DeepSurv C-index 비교

### Phase C — 고차원 유전체 데이터 도전 (3~4일)
- [ ] TCGA subset 다운로드 (expression + clinical merge)
- [ ] Feature selection (top variable genes, LASSO-Cox)
- [ ] DeepSurv로 학습 + C-index 측정
- [ ] Kaplan-Meier로 high/low risk 그룹 분리해서 생존 차이 확인

### Phase D — 해석 (1~2일)
- [ ] 어떤 유전자가 예측에 중요? (feature attribution)
- [ ] 위험도 분포를 환자 클러스터로 나눠보기

## 배울 개념 (체크리스트)
- [ ] **Censoring** — 관측 중단의 의미와 왜 단순 회귀로 못 푸는지
- [ ] **Hazard function, Survival function, Cumulative hazard**
- [ ] **Proportional hazards assumption**
- [ ] **C-index (concordance)** — AUROC의 생존 버전
- [ ] Partial likelihood (Cox가 baseline hazard 없이 학습하는 트릭)
- [ ] DeepSurv loss가 partial likelihood의 negative log
- [ ] 고차원 + 저샘플(= p ≫ n)에서의 overfit 주의

## 참고 자료
- **논문**: Cox, "Regression models and life tables" (1972) — 고전
- **논문**: Katzman et al., "DeepSurv" (2018)
- **논문**: Ching et al., "Cox-nnet" (2018)
- **책**: Kleinbaum & Klein, "Survival Analysis: A Self-Learning Text"
- **패키지 문서**: [lifelines docs](https://lifelines.readthedocs.io/), [pycox docs](https://github.com/havakv/pycox)

## AI agent에 물어볼 것
1. "Censoring된 환자를 단순 제거하면 왜 편향이 생기는지 예시로 설명해줘"
2. "Cox partial likelihood 수식을 한 단계씩 유도해줘"
3. "C-index가 왜 AUROC보다 생존에 더 적합한지 기하적으로 설명해줘"
4. "Proportional hazards 가정이 깨졌을 때 어떻게 진단하고 대응해?"
5. "TCGA BRCA 데이터를 cBioPortal에서 받는 구체적 절차를 알려줘"

## 현지 가서 연결되는 것
UNLV Project 2가 이 방향 그대로일 가능성이 매우 높다. **여기서 한 것은
현지에서 첫 미팅 때 바로 보여줄 수 있는 포트폴리오**가 된다. 제일 공들일 폴더.
