Guía de ejecución – Prototipo de Nodo de Robot Resiliente

1. Descripción
   Este repositorio implementa un nodo de robot resiliente utilizando Docker y Docker Compose.
   El sistema simula una falla controlada en el primer arranque y demuestra recuperación automática
   mediante políticas de reinicio.

   El objetivo es demostrar:
    - Tolerancia a fallos
    - Recuperación automática
    - Consistencia de despliegue
    - Alta disponibilidad básica (HA)

2. Requisitos Previos
   Antes de ejecutar el repositorio, se debe tener instalado:
    - Docker
    - Docker Compose (v2 o superior)
  
3. Instrucciones de Ejecución
   - Abrir una terminal en la carpeta del proyecto
   - Ejecutar el sistema
     "docker compose up --build -d"

4. Validación de Alta Disponibilidad
   - Comprobar el estado del contenedor
     "docker compose ps"
     Debe aparecer el contenedor robot_node como Up
   Mensajes:
   - Ver fallo inicial y recuperación automática
     En los logs se observará: "robot_node: Fallo crítico detectado (Inconsistencia de entorno)"
   - Reinicio automático del contenedor
     Mensaje de recuperación: "robot_node: Iniciando recuperación del sistema"
   - Mensajes periódicos: "HEARTBEAT: Nodo operativo y reportando a Cloud/Edge"
   Esto demuestra que detecta una falla, reinicia automáticamente y continúa operando sin intervención

5. Detener el Sistema
   "docker compose down"
     
