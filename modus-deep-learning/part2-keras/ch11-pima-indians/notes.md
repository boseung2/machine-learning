# Ch 11 — 피마 인디언 당뇨병 예측

원본: `deep_code/02_Data_preparation.py` (EDA) + `02_Pima_Indian.py` (학습)

## 목적
- **데이터 준비/탐색(EDA)** 단계와 모델 학습을 한 흐름으로 본다.
- pandas / seaborn 으로 컬럼 의미·분포·상관관계를 파악한 뒤 모델 학습.

## 데이터
- 파일: `data/pima-indians-diabetes.csv` (768 rows)
- 컬럼 (책에서 부여한 이름):
  | 이름 | 의미 |
  | - | - |
  | pregnant | 임신 횟수 |
  | plasma | 포도당 농도 (2시간 OGTT) |
  | pressure | 혈압 (mm Hg) |
  | thickness | 삼두근 피하지방 두께 (mm) |
  | insulin | 2시간 인슐린 (mu U/ml) |
  | BMI | 체질량지수 |
  | pedigree | 당뇨병 가족력 점수 |
  | age | 나이 |
  | class | 5년 내 당뇨병 발병 (0/1) |

## 모델 (책 그대로)
```text
Input(8) → Dense(12, relu) → Dense(8, relu) → Dense(1, sigmoid)
```

## 책과 다르게 가는 부분
- EDA와 학습을 **한 노트북**에서 진행 (책은 두 .py 파일).
- `np.loadtxt` 대신 `pd.read_csv` 로 통일 + 컬럼 이름 부여 → 그래프 가독성 ↑.

## 학습 체크
- [ ] `df.describe()` 에서 어떤 컬럼이 0이 많은지 (의미상 0이 비정상인 컬럼: glucose/BP/BMI 등)
- [ ] 상관관계 히트맵에서 `class` 와 가장 강하게 연관된 컬럼은?
- [ ] FacetGrid 히스토그램으로 plasma의 클래스별 분포 비교
