# 농작물 가격 예측 모델

이 프로젝트는 기온, 강수량과 같은 기상 데이터를 기반으로 농작물의 가격 변동을 예측하는 머신러닝 모델을 개발하기 위한 것입니다. 주요 목표는 데이터를 활용해 농산물 유통 과정의 불확실성을 줄이고, 농업인과 유통업체의 의사결정을 지원하는 데 있습니다.

---

## 주요 내용

### 1. 프로젝트 개요
- **목표**: 기상 데이터와 과거 가격 데이터를 활용해 농작물의 미래 가격을 예측.
- **사용 기술**: Python, Pandas, NumPy, Matplotlib, Scikit-learn, TensorFlow.
- **분석 과정**:
  1. 데이터 전처리: 결측치 처리, 스케일링, 상관관계 분석.
  2. 모델 학습: 시계열 분석 모델과 회귀 모델 비교.
  3. 결과 시각화: 예측 성능 평가 및 주요 결과물 제공.

---

### 2. 주요 결과
- **모델 성능**:
  - 평균 절대 오차 (MAE): 15.3
  - 결정계수 (R²): 0.87
- **결과 시각화**:
  ![모델 성능](results/model_performance.png)

- **예측 결과**:
  ![예측 샘플](results/prediction_sample.png)

---

### 3. 사용법

#### 1) 데이터 준비
- `data/` 폴더에 제공된 데이터를 사용하거나, 새로운 데이터를 추가로 업로드하세요.

#### 2) 모델 실행
- Colab에서 [Crops_Price_Prediction.ipynb](./Crops_Price_Prediction.ipynb)를 열어 실행합니다.
- 주요 실행 단계:
  1. 데이터 전처리
  2. 모델 학습 및 평가
  3. 예측 결과 확인

#### 3) 결과 확인
- `results/` 폴더에서 시각화된 결과 및 학습된 모델 파일을 확인할 수 있습니다.

---

### 4. 주요 기술 및 라이브러리
- **Python 라이브러리**:
  - Pandas: 데이터 처리
  - NumPy: 수치 연산
  - Matplotlib/Seaborn: 데이터 시각화
  - Scikit-learn: 회귀 모델 학습
  - TensorFlow: 딥러닝 모델 구현
- **환경**:
  - Google Colab

---

### 5. 참고 자료
- [프로젝트 발표 자료](reports/발표자료.pdf)
- [최종 보고서](reports/최종보고서.pdf)
- [Colab에서 실행](https://colab.research.google.com/github/username/repository/blob/main/Crops_Price_Prediction.ipynb)

---

### 6. 기여 방법
이 프로젝트에 대한 제안이나 수정 사항이 있다면 [Issues 탭](https://github.com/username/repository/issues)을 통해 알려주세요.

---