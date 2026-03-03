import os
import time
import sys

flag_file = "/tmp/failed_once.txt"

if not os.path.exists(flag_file):
    with open(flag_file, "w") as f:
        f.write("error_logged")
    print("robot_node: Fallo crítico detectado (Inconsistencia de entorno)")
    time.sleep(2)
    sys.exit(1)

print("robot_node: Iniciando recuperación del sistema")
while True:
    print("HEARTBEAT: Nodo operativo y reportando a Cloud/Edge")
    time.sleep(2)
