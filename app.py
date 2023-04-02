from flask import Flask, render_template, request
import random, copy

app = Flask(__name__, static_url_path='/static')

original_questions = {
 #Format is 'question':[options]
 'Taj Mahal':['Agra','New Delhi','Mumbai','Chennai'],
 'Great Wall of China':['China','Beijing','Shanghai','Tianjin'],
 'Petra':['Ma\'an Governorate','Amman','Zarqa','Jerash'],
 'Machu Picchu':['Cuzco Region','Lima','Piura','Tacna'],
 'Egypt Pyramids':['Giza','Suez','Luxor','Tanta'],
 'Colosseum':['Rome','Milan','Bari','Bologna'],
 'Christ the Redeemer':['Rio de Janeiro','Natal','Olinda','Betim']
}

questions = copy.deepcopy(original_questions)

def shuffle(q):
    selected_keys = []
    i = 0
    while i < len(q):
        if len(q.keys()) == 0:
            break
        current_selection = random.choice(list(q.keys()))
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i += 1
    return selected_keys

@app.route('/')
def index():
    questions_shuffled = questions
    for i in questions.keys():
        random.shuffle(questions[i])
    return render_template('index.html', q = questions_shuffled, o = questions)

@app.route('/quiz', methods=['POST'])
def quiz():
    score = 0
    for i in questions.keys():
        answered = request.form[i]
        if original_questions[i][0] == answered:
            score += 1
        
    return  render_template('main.html', score = score)

if __name__ == '__main__':
    app.run(debug=True)
