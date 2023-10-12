from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name)

# Set the database URL as an environment variable
os.environ["DATABASE_URL"] = "https://crashbandicootsthe1.github.io/teams/"

@app.route('/run-python-script', methods=['POST'])
def run_python_script():
    try:
        # Access the database URL from the environment variable
        database_url = os.environ.get("DATABASE_URL", "")
        
        # You can use 'database_url' in your 'clans.py' script as needed
        # For example:
        subprocess.check_output(["python", "clans.py", database_url], stderr=subprocess.STDOUT, text=True)

        output = f"Running 'clans.py' with DATABASE_URL={database_url}"

        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()
