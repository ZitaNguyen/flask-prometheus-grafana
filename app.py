from flask import Flask, request
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# Define Prometheus Metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint']) # track total number of HTTP requests
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP Request Latency', ['endpoint']) # measure request duration

@app.route('/')
def home():
    REQUEST_COUNT.labels(method=request.method, endpoint='/').inc() # Count requests
    return "Hello DevOps!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200 # Expose metrics in Prometheus format

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
