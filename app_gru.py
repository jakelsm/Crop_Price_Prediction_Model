import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 허용

# GRU 모델 경로
GRU_MODEL_PATH = 'gru_model.h5'

# GRU 모델 예측 엔드포인트
@app.route('/predict', methods=['POST'])
def predict_gru():
    try:
        data = request.get_json()

        current_date = data['current_date']
        current_temp = float(data['current_temp'])
        current_rainfall = float(data['current_rainfall'])
        future_date = data['future_date']

        # 날짜 차이 계산
        current_date_dt = datetime.strptime(current_date, "%Y.%m.%d")
        future_date_dt = datetime.strptime(future_date, "%Y.%m.%d")
        days_difference = (future_date_dt - current_date_dt).days

        # GRU 모델 로드
        gru_model = tf.keras.models.load_model(GRU_MODEL_PATH)

        # 스케일러 설정 (학습할 때 사용된 범위)
        scaler = StandardScaler()
        scaler.fit(np.array([[10, 0, 9000], [30, 200, 30000]]))  # 학습 데이터 범위로 설정

        # 입력값 스케일링
        future_input_scaled = scaler.transform([[current_temp, current_rainfall, 0]])
        current_temp_scaled, current_rainfall_scaled, _ = future_input_scaled[0]

        # 시퀀스 생성
        future_sequence = np.array([[current_temp_scaled, current_rainfall_scaled]] * 90)
        future_input_gru = future_sequence.reshape(1, 90, 2)

        # GRU 모델 예측
        predicted_price_scaled = gru_model.predict(future_input_gru)
        final_price_scaled = predicted_price_scaled[0][0]

        # 원래 스케일로 복원
        original_scale = scaler.inverse_transform([[current_temp_scaled, current_rainfall_scaled, final_price_scaled]])
        future_price = original_scale[0, 2]

        return jsonify({
            'current_date': current_date,
            'future_date': future_date,
            'days_difference': days_difference,
            'predicted_price': round(future_price, 2)
        })

    except Exception as e:
        print(f"오류 발생: {e}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
