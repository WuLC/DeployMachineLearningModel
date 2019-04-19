# -*- coding: utf-8 -*-
# Created on Fri Apr 19 2019 13:3:3
# Author: WuLC
# EMail: liangchaowu5@gmail.com

from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/github_webhook', methods=['POST'])
def rebuild():
    print('new commits to github repository')
    ## subprocess.run can just deal with the first change
    ## since it stuck in it, use popen instead
    # subprocess.run(['sh', 'build_and_run.sh'])
    subprocess.Popen(['sh', 'build_and_run.sh'])
    return jsonify('got it')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)