import random

def generate_fake_traffic():
    return {
        "ip": f"192.168.0.{random.randint(1,255)}",
        "protocol": random.choice(["TCP", "UDP", "ICMP"]),
        "port": random.randint(20, 8080),
        "packet_size": random.randint(200, 1500)
    }
