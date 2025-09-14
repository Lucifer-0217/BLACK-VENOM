# core/config.py

def load_config():
    # In future, can be extended to load from JSON/YAML
    config = {
        "default_ports": [21, 22, 80, 443, 8080],
        "timeout": 1
    }
    return config
