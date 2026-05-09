# Ch 01 — 선형 회귀 (최소제곱법)

원본: `deeplearning/deep_class/01_Linear_Regression.py`

## 핵심 키워드

- 회귀 (regression)
- 최소제곱법 (least squares)
- 평균, 분산, 공분산
- 기울기 `a`, y절편 `b`

## 데이터셋

공부 시간 vs 점수.

| x (공부시간) | 2 | 4 | 6 | 8 |
| ---------- | - | - | - | - |
| y (점수)    | 81 | 93 | 91 | 97 |

## 수식 — 최소제곱법

직선 `y = a x + b`로 데이터를 가장 잘 설명하는 `a`, `b` 찾기.

### 기울기 `a`

$$
a = \frac{\sum_{i}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i}(x_i - \bar{x})^2}
= \frac{\text{Cov}(x, y)}{\text{Var}(x)}
$$

### y절편 `b`

$$
b = \bar{y} - a \bar{x}
$$

평균점 $(\bar{x}, \bar{y})$를 직선이 지난다는 사실에서 자동으로 따라옵니다.

## 직관

- 분자: x가 평균보다 큰 만큼 y도 평균보다 클수록 양수가 누적 → **양의 상관**.
- 분모: x의 퍼짐 정도(분산). 같은 변동량이라도 x가 좁게 모여 있으면 기울기가 더 가파르게 잡힘.

## 책과 다르게 쓴 부분

- 책은 `for` 루프로 분자를 계산하지만, NumPy 벡터화가 더 짧고 빠릅니다 (`((x-mx)*(y-my)).sum()`).
- 마지막 단계에서 **scikit-learn `LinearRegression`** 과 **Keras 3 모델**로 같은 결과가 나오는지 확인까지 진행 (책에는 없음).

## 학습 체크

- [ ] 최소제곱 공식의 분자/분모를 직접 계산해 본다
- [ ] `np.polyfit(x, y, 1)` 결과와 비교
- [ ] `sklearn.linear_model.LinearRegression`로 같은 `a`, `b`가 나오는지
- [ ] Keras 3로 1뉴런 회귀 모델을 학습시켜 비슷한 값이 나오는지 (다음 장 경사하강의 brigde)
