from flask import Flask, jsonify
import subprocess

app = Flask(__name)

@app.route('/run-python-script', methods=['POST'])
def run_python_script():
try:
    output = subprocess.check_output(["python", "clans.py"], stderr=subprocess.STDOUT, text=True)
    return jsonify({"output": output})
except subprocess.CalledProcessError as e:
    app.logger.error(f"Error running 'clans.py': {str(e.output)}")
    return jsonify({"error": str(e.output)})
if __name__ == '__main__':
    app.run()
