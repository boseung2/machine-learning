# Ch 10 — 폐암 수술 환자의 생존율 예측

원본: `deep_code/01_My_First_Deeplearning.py`

## 목적
- 첫 딥러닝 모델로 **이진 분류** 문제를 풀어본다.
- 폐암 수술 환자 470명의 임상 정보 17개 컬럼 → 1년 후 생존 여부.

## 데이터
- 파일: `data/ThoraricSurgery.csv`
- 행 수: 470
- 컬럼: 17개 입력 + 1개 라벨 (마지막 컬럼)
- 라벨: 0 (사망) / 1 (생존)
- 헤더 없음 (`header=None`)

## 모델 (책 그대로)
```text
Input(17) → Dense(30, relu) → Dense(1, sigmoid)
```

## 책과 다르게 가는 부분
- 데이터 로딩: `np.loadtxt` 대신 `pd.read_csv(..., header=None)` (일관성).
- 시드: `keras.utils.set_random_seed(0)` 한 줄로 모든 백엔드 RNG 일괄 설정.
- 손실 함수: 책은 `mean_squared_error` 를 썼지만 *이진 분류는 `binary_crossentropy` 가 표준*. 두 손실 모두 보여줌.
- `Sequential([Input(...), Dense(...)])` 패턴 사용.

## 학습 체크
- [ ] 470개 데이터로 30 에포크 학습 → train accuracy 출력
- [ ] MSE 손실 vs BCE 손실 비교
- [ ] sigmoid 출력값 → 0.5 임계로 0/1 변환 → 직접 정확도 계산
