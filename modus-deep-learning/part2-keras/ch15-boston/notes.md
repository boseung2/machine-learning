# Ch 15 — 보스턴 집값 예측 (회귀)

원본: `deep_code/13_Boston.py`

## 목적
- 지금까지 본 분류와 달리 **회귀(regression)**: 출력이 실수값(집값).
- 손실: `mean_squared_error`. 출력 layer에 활성화 함수 없음 (`Dense(1)`).

## 데이터
- 파일: `data/housing.csv`
- 506 rows × 14 cols (입력 13개 + 가격 1개), 공백 구분
- ⚠ 윤리 이슈: 컬럼 `B` 가 인종 관련. sklearn 1.2부터 deprecated. 본 트랙에서는 *학습용 토이 데이터*로만 사용.

## 책과 다르게 가는 부분
- `pd.read_csv(..., delim_whitespace=True)` — pandas 2.2+ 에서 deprecated → `sep=r"\s+"` 로 교체.
- `train_test_split` 으로 70/30 분리.
- 평가 지표 추가: MAE (Mean Absolute Error). MSE 단위는 `(천 달러)^2` 라 직관 떨어짐 → MAE/RMSE 같이 표시.

## 학습 체크
- [ ] 분류와 회귀의 모델 끝단 차이 (`Dense(1, sigmoid)` vs `Dense(1)`)
- [ ] MSE/MAE 단위 감각 — 평균적으로 몇 천 달러 정도 빗나가는지
- [ ] 예측값 vs 실제값 스캐터에서 직선 `y=x` 와 얼마나 떨어져 있는지
