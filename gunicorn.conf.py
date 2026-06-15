import multiprocessing
import os

# Bind to 0.0.0.0 as required by Pars Pack PaaS
bind = "0.0.0.0:" + os.environ.get("PORT", "8000")

# Workers
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gthread"
threads = 2

# Timeouts
timeout = 120
graceful_timeout = 30
keepalive = 5

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Security
limit_request_line = 8190
limit_request_fields = 100
