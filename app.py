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
    'b11', 'b12', 'b14', 'b15', 'b22', 'b23', 'b24', 'b25',
    'b33', 'b32', 'b43', 'b42', 'b52', 'b53', 'b54', 'b55', 'b57',
    'c25', 'c44', 'c54', 'c63',
    'd13', 'd14', 'd24', 'd28', 'd29', 'd53', 'd93', 'd94', 'd95', 'd116'
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
    input_names = ['b11', 'b12', 'b13', 'b14', 'b15',
                   'b21', 'b22', 'b23', 'b24', 'b25',
                   'b31', 'b32', 'b33', 'b34', 'b35', 'b36',
                   'b41', 'b42', 'b43', 'b44', 'b45', 'b46',
                   'b51', 'b52', 'b53', 'b54', 'b55', 'b56', 'b57', 'b58', 'b59', 'b510', 'b511', 
                   'b61', 'b62', 'b63', 'b64', 
                   'c11', 'c12', 'c13', 'c14', 'c15', 
                   'c21', 'c22', 'c23', 'c24', 'c25', 
                   'c31', 'c32', 'c33', 'c34', 'c35', 
                   'c41', 'c42', 'c43', 'c44', 
                   'c51', 'c52', 'c53', 'c54', 
                   'c61', 'c62', 'c63', 
                   'd11', 'd12', 'd13', 
                   'd21', 'd22', 'd23', 'd24', 'd25', 'd26', 'd27', 'd28', 
                   'd31', 'd32', 'd33', 'd34', 'd35', 'd36', 'd37', 'd38', 'd39', 'd310', 'd311', 'd312', 'd313', 'd314', 'd315', 'd316', 'd317', 'd318', 'd319', 'd320', 'd321', 'd322', 'd323', 
                   'd41', 'd42', 'd43', 'd44', 'd45', 'd46', 
                   'd51', 'd52', 'd53', 'd54', 'd55', 
                   'd61', 'd62', 'd63', 'd64', 'd65', 'd66', 'd67', 'd68', 
                   'd71', 'd72', 'd73', 'd74', 'd75', 'd76', 'd77', 
                   'd81', 'd82', 'd83', 'd84', 'd85', 'd86', 
                   'd91', 'd92', 'd93', 'd94', 'd95',
                   'd101', 'd102', 'd103', 'd104', 
                   'd111', 'd112', 'd113', 'd114', 'd115', 'd116', 'd117', 'd118', 'd119', 
                   'd121', 'd122', 'd123', 'd124', 
                   'd131', 'd132', 'd133', 'd134']

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

            # Prediksi dengan model NB
            prediction = model_full.predict(input_data)[0]

            # Mapping hasil prediksi ke label risiko
            risk_mapping = {1: 'Risiko Rendah', 2: 'Risiko Sedang', 3: 'Risiko Tinggi'}
            prediction_label = risk_mapping.get(prediction, "Tidak Diketahui")

    return render_template('full_classification.html', form_values=form_values, prediction=prediction_label, error=error)

if __name__ == '__main__':
    app.run(debug=True)
