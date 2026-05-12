# Ch 17 — Reuters 뉴스 분류 (RNN/LSTM)

원본: `deep_code/15_Reuters_LSTM.py`

## 목적
- **순환 신경망 (RNN)** 의 첫 실전 적용. 가변 길이 시퀀스(텍스트) 처리.
- 핵심 구성요소: `Embedding`, `LSTM`, `Dense(softmax)`.
- 단어 → 정수 → 임베딩 벡터 → LSTM 시퀀스 처리 → 분류 의 흐름을 코드로 따라가기.

## 데이터
- `keras.datasets.reuters.load_data(num_words=1000)` — 첫 실행 시 ~3MB 자동 다운로드.
- **이미 정수 인코딩 되어 있음** — 각 기사는 단어 인덱스 시퀀스 (예: `[1, 56, 2, 781, ...]`). 토크나이저 불필요.
- 학습 8,982건 / 테스트 2,246건, **46개 카테고리** (지진·곡물·이자율·무역 등).
- 시퀀스 길이는 가변 (수십~수천 단어). `pad_sequences` 로 통일 필요.

## 핵심 변경 (Keras 1.x → Keras 3)
- `from keras.preprocessing.sequence import pad_sequences` → `from keras.utils import pad_sequences`
- `from keras.layers.recurrent import LSTM` → `from keras.layers import LSTM`
- `from keras.layers.embeddings import Embedding` → `from keras.layers import Embedding`
- `from keras.layers.core import Activation, Dense` → `from keras.layers import Activation, Dense`

## 책과 다르게 가는 부분
- 손실: `categorical_crossentropy` + one-hot 대신 `sparse_categorical_crossentropy` + 정수 라벨 (ch16 과 동일 패턴).
- 학습/검증 분리: 책은 train 전체로 학습. 우리는 `validation_split=0.2` 로 학습 중 일반화 추적.

## 모델
```text
Input(sequence, maxlen=100)
 → Embedding(num_words=1000, output_dim=100)   # (100, 100)
 → LSTM(100)                                    # (100,)  ← 마지막 hidden state
 → Dense(46, softmax)
```

총 파라미터 약 180k. CPU 에서 10 epoch ~3–5분.

## 각 층의 의미
- **Embedding(1000, 100)** — 1,000개 단어 각각을 100차원 벡터로 매핑. 학습 가능한 lookup table. 한 정수 → 100차원 벡터.
- **LSTM(100)** — 시퀀스를 한 단어씩 읽으며 100차원 hidden state 유지. 기본 출력은 **마지막 step 의 hidden state** 만 (`return_sequences=False`).
- **Dense(46, softmax)** — 46개 클래스 중 하나로 분류.

## RNN 의 핵심 직관
- Dense 만 쓰면 단어 순서가 무시됨 (단어 가방 = bag-of-words).
- LSTM 은 시퀀스를 **순차적으로** 읽으면서 hidden state 에 "여기까지 본 맥락" 을 누적. 단어 순서가 의미에 영향.
- 그래서 같은 단어들로 이뤄진 두 문장도 순서가 다르면 다른 표현이 됨.

## 학습 체크
- [ ] `num_words=1000` 이라 1,000개 빈도 상위 단어만 사용 — 나머지는 OOV(out-of-vocabulary) 로 무시됨
- [ ] `pad_sequences(maxlen=100)` 이후 모든 시퀀스 shape 이 `(100,)` 으로 통일되는지
- [ ] Embedding 의 output shape: `(batch, 100, 100)` — (배치, 시퀀스, 임베딩차원)
- [ ] LSTM 의 output shape: `(batch, 100)` — 마지막 hidden state 만 나옴
- [ ] test accuracy 가 0.65~0.75 정도 나오는지 — 46-class 균형 문제고 baseline (다수클래스) 는 ~0.36
