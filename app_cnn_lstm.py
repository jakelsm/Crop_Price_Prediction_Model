from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd

# Flask 앱 초기화
app = Flask(__name__)
CORS(app)

# 데이터를 불러오고 스케일링 및 슬라이딩 윈도우 적용 (예시 데이터 사용)
# 실제 데이터로 대체 필요
data = pd.read_csv('C:/radish_price_prediction/finaldata_1.csv')  # 사용 중인 데이터 파일 경로로 대체

# 예시 feature와 target 설정
features = data[['rainfall', 'temp', 'monthrf', 'monthtp', 'trade']].values
target = data['Price']

# 스케일러 설정
scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()
X_scaled = scaler_X.fit_transform(features)
y_scaled = scaler_y.fit_transform(target.values.reshape(-1, 1))

# 슬라이딩 윈도우 설정
window_size = 30
X_windows, y_windows = [], []

for i in range(len(X_scaled) - window_size):
    X_windows.append(X_scaled[i:i + window_size])
    y_windows.append(y_scaled[i + window_size])

X_windows = np.array(X_windows)
y_windows = np.array(y_windows)

# 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X_windows, y_windows, test_size=0.2, random_state=42)

# 학습된 모델 로드
model = tf.keras.models.load_model('CNN_LSTM_model.h5')

# 날짜 입력을 받아 미래 가격을 예측하는 API
@app.route('/predict_cnn_lstm', methods=['POST'])
def predict():
    data = request.get_json()
    print(f"Received input date: {data['input_date']}")  # 로그로 요청 데이터 확인

    # 입력된 날짜
    input_date = data['input_date']  # yyyy-mm-dd 형식으로 입력됨

    # 마지막 데이터로 예측 수행
    latest_data = X_test[-1].reshape(1, window_size, X_train.shape[2])  # 실제 데이터로 변경
    predicted_price_scaled = model.predict(latest_data)
    predicted_price_original = scaler_y.inverse_transform(predicted_price_scaled)

    # 최저, 평균, 최고 가격 계산
    min_price = float(predicted_price_original[0][0] * 0.9)  # float32를 float으로 변환
    max_price = float(predicted_price_original[0][0] * 1.1)  # float32를 float으로 변환
    mean_price = float(predicted_price_original[0][0])  # float32를 float으로 변환

    result = {
        'min_price': round(min_price, 2),
        'mean_price': round(mean_price, 2),
        'max_price': round(max_price, 2)
    }

    print(f"Predicted price: {predicted_price_original[0][0]}")  # 예측 값 출력

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
