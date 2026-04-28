# 01 · Classical ML for Medical Tabular Data

## 목표
"딥러닝 없이 의료 tabular 데이터를 끝까지 처리해본다." UNLV 4개 프로젝트 중
Project 2(생존 분석), Project 4(EHR) 는 결국 tabular 성질이 강하다.
**고전 ML이 베이스라인이다** — 이걸 넘어야 딥러닝을 쓸 명분이 생긴다.

## 노트북
| # | 파일 | 데이터 | 주제 |
|---|---|---|---|
| 01 | `01_heart_disease_classification.ipynb` | Heart Disease UCI | 이진 분류, 평가지표, ROC/AUC |
| 02 | `02_diabetes_regression.ipynb` | sklearn Diabetes | 회귀, CV, 잔차 분석 |
| 03 | `03_rf_vs_xgboost.ipynb` | Breast Cancer | 트리 앙상블 비교, feature importance |

## 배울 개념 (체크리스트)
- [ ] `train_test_split`으로 데이터 나누기
- [ ] `StandardScaler`로 스케일링 (왜 트리는 불필요한지)
- [ ] **분류 지표**: accuracy / precision / recall / F1 / AUROC
- [ ] **회귀 지표**: MAE / MSE / RMSE / R²
- [ ] Confusion matrix 읽기
- [ ] Cross-validation의 의미
- [ ] Overfitting/underfitting을 학습곡선으로 진단
- [ ] Feature importance 해석
- [ ] **의료 도메인 포인트**: 클래스 불균형, precision-recall trade-off (병원에서 FN vs FP 비용)

## 끝내면 생길 질문 (Layer 2로 가는 다리)
- "모든 모델이 ~85%에서 멈추는데, 신경망으로 올릴 수 있을까?"
- "Feature를 사람이 고르지 않고 모델이 학습하게 할 수는 없나?"
- "이미지/시퀀스 데이터는 이렇게 못 풀 텐데 어떻게 풀지?"

→ 이 질문들이 생기면 `02-pytorch-basics/`로 간다.
