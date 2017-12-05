from flask import Flask
from flask import request
from flask import jsonify
import json
import subprocess

app = Flask(__name__)
config = None

@app.route('/<hook>', methods=['POST'])
def hook_listen(hook):
    if request.method == 'POST':
        if hook in config['hooks']:
            token = request.args.get('token')
            if token == config['hooks'][hook]['token']:
                hook_call = config['hooks'][hook]['call']
                if hook_call:
                    try:
                        subprocess.call(hook_call)
                        return jsonify(success=True), 200
                    except OSError as e:
                        return jsonify(success=False, error=str(e)), 400
                else:
                    return jsonify(success=False, error="No call defined for hook"), 500
            else:
                return jsonify(success=False, error="Invalid token"), 400
        else:
            return jsonify(success=False, error="Unknown hook"), 404
    else:
        return jsonify(success=False, error="Method not allowed"), 405

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

if __name__ == '__main__':
    config = load_config()
    app.run(host=config.get('host', 'localhost'), port=config.get('port', 8000))
