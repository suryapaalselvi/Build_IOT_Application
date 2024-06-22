from flask import Flask, render_template, request

app = Flask(__name__)

def read_data():
    data = []
    with open('data.txt', 'r') as file:
        for line in file:
            item = eval(line.strip())
            item['x'] = float(item['x'])
            item['y'] = float(item['y'])
            data.append(item)
    return data

def save_data(data):
    with open('data.txt', 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

@app.route('/')
def index():
    data = read_data()
    return render_template('index.html', data=data)

@app.route('/update_state', methods=['POST'])
def update_state():
    data = read_data()
    index = int(request.form['index'])
    data[index]['state'] = 1 - data[index]['state']
    save_data(data)
    return 'Success'

@app.route('/save_positions', methods=['POST'])
def save_positions():
    data = read_data()
    for i, item in enumerate(data):
        item['x'] = float(request.form[f'x_{i}'])
        item['y'] = float(request.form[f'y_{i}'])
    print (data)
    save_data(data)
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True)
