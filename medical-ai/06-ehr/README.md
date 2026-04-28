# 06 · EHR 분석 (UNLV Project 4 미니)

## UNLV 프로젝트와의 연결
> "Deep neural networks for electronic health record (EHR) analysis"

EHR(전자 의무 기록)은 병원에서 쌓이는 환자 데이터:
- 진단 코드(ICD-10), 처방, 검사 수치(lab), 바이탈 사인, 의무기록 텍스트
- **불규칙 시계열** (측정 간격 제각각), **희소**, **결측**

대표 태스크: 사망률 예측, 재입원 예측, 패혈증 조기 경보, 입원 기간 예측.

## 추천 데이터셋

### 🥇 1차: **MIMIC-IV Demo** (공개, 무료)
- 100명 환자 서브셋 (de-identified)
- [PhysioNet 무료 가입](https://physionet.org/content/mimic-iv-demo/) 후 즉시 다운로드
- 실제 병원 데이터 구조 그대로 (테이블 여러 개)

### 🥈 2차: **Synthea** (합성 EHR)
- [synthetichealth/synthea](https://github.com/synthetichealth/synthea)
- 가짜지만 구조는 진짜와 동일. 개인정보 이슈 없음. 양 조절 가능.

### 🥉 3차: **eICU Collaborative Research Database Demo**
- ICU 특화, 여러 병원 혼합
- 구조가 MIMIC과 다른 연습

### 🏆 Full MIMIC-III/IV (credentialed)
- PhysioNet CITI training 수료 후 접근 가능
- UNLV 가서 쓸 가능성 높음 → 현지에서 credential 받기

## 단계별 계획

### Phase A — EHR 데이터 구조 이해 (2~3일)
- [ ] MIMIC-IV Demo 다운로드, `admissions`, `patients`, `labevents`, `chartevents`, `diagnoses_icd` 테이블 탐색
- [ ] 한 환자의 timeline 그려보기 (pandas)
- [ ] ICD-10 진단 코드 상위 분포 보기

### Phase B — Tabular Baseline (2일)
- [ ] 입원 첫 24시간 feature 요약 (vital 평균, 주요 lab 마지막값)
- [ ] XGBoost로 **in-hospital mortality** 예측
- [ ] AUROC 보고 → 베이스라인

### Phase C — 시퀀스 모델 (3~4일)
- [ ] 시간 window 별 lab / vital 시계열 구성
- [ ] **LSTM/GRU**로 예측
- [ ] 결측값 처리: forward fill vs learnable mask vs GRU-D
- [ ] 불규칙 간격 처리: 시간 delta 추가 feature로

### Phase D — Transformer (advanced, 2일)
- [ ] Self-attention 기반 EHR 모델 (e.g., BEHRT 아이디어)
- [ ] Concept embedding: 진단/처방 코드를 임베딩으로

### Phase E — 공정성 / 해석 (1일)
- [ ] 인종/성별/연령군별 성능 격차 확인 (fairness)
- [ ] Attention weight 또는 SHAP로 예측 근거 제시

## 배울 개념 (체크리스트)
- [ ] EHR 테이블 구조 (OMOP/MIMIC 스키마 기본)
- [ ] 불규칙 시계열(irregular time series) 처리 전략
- [ ] Masking & padding in sequence models
- [ ] 결측 자체가 정보가 되는 경우 (missingness indicator)
- [ ] Calibration (확률이 실제 빈도와 맞나)
- [ ] Clinical utility vs statistical performance
- [ ] 데이터 leakage — **미래 정보가 예측 시점에 들어가면 안 됨**

## 참고 자료
- **논문**: Rajkomar et al., "Scalable and accurate deep learning with electronic health records" (Nature Digital Medicine, 2018)
- **논문**: Choi et al., "RETAIN" (2016) — 해석 가능한 RNN for EHR
- **논문**: Li et al., "BEHRT" (2020) — Transformer for EHR
- **튜토리얼**: [MIT MIMIC code repo](https://github.com/MIT-LCP/mimic-code)

## AI agent에 물어볼 것
1. "MIMIC-IV의 `chartevents`와 `labevents` 차이가 뭐야?"
2. "EHR에서 데이터 leakage가 일어나기 쉬운 구체적 케이스 3가지"
3. "GRU-D가 결측을 어떻게 학습에 활용하는지 수식으로 설명"
4. "EHR 모델을 임상에 적용할 때 calibration이 왜 accuracy보다 중요해?"
5. "MIMIC Demo로 in-hospital mortality 예측을 Phase A+B까지 한 번에 돌려줄 스케치 코드 보여줘"

## 현지 가서 연결되는 것
- UNLV credential로 실제 MIMIC-III/IV 전체에 접근 가능
- 여기서 만든 전처리 파이프라인 그대로 스케일업
- EHR은 **모든 태스크의 토대**라 폭넓게 도움됨
