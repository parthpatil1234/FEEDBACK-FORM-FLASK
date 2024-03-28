from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Route for the feedback form
@app.route('/')
def feedback_form():
    return render_template('feedback_form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_feedback():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        feedback = request.form['feedback']
        
        # Here you can process the feedback data (e.g., save it to a database)
        
        # For now, just print the feedback
        print(f"Feedback received from {name} ({email}): {feedback}")

        # Redirect to a thank you page
        return redirect('/thankyou')

# Route for the thank you page
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
