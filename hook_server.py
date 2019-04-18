from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# Load the model
@app.route('/github_hook', methods=['POST'])
def rebuild():
    # Get the data from the POST request.
    print('new commits to github repository')
    subprocess.run(['sh', 'build_and_run.sh'])
    return jsonify('got it')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8081)