from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Load model SVM

model = joblib.load("model/dt_model.pkl")

@app.route('/classification', methods=['GET', 'POST'])
def classification():
    input_names = [
    'b15', 'b22', 'b25',
    'b33', 'b32', 'b43', 'b42', 'b54', 'b55',
    'c25', 'c54', 'c63',
    'd13', 'd14', 'd24', 'd28', 'd29', 'd93', 'd95', 'd116'
]


    form_values = {}
    prediction_label = None
    error = None

    if request.method == 'POST':
        # Ambil nilai dari form
        form_values = {name: request.form.get(name, '').strip() for name in input_names}

        # Cek apakah ada input kosong
        if any(value == '' for value in form_values.values()):
            error = "Semua Form Isian Harus Diisi"
        else:
            # Konversi nilai ke float
            input_data = np.array([float(value) for value in form_values.values()]).reshape(1, -1)

            # Prediksi dengan model SVM
            prediction = model.predict(input_data)[0]

            # Mapping hasil prediksi ke label risiko
            risk_mapping = {0: 'Risiko Rendah', 1: 'Risiko Tinggi'}
            prediction_label = risk_mapping.get(prediction, "Tidak Diketahui")

    return render_template('classification.html', form_values=form_values, prediction=prediction_label, error=error)

if __name__ == '__main__':
    app.run(debug=True)
