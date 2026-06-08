# Script de Automatización de Diagnóstico TI 🛠️

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey.svg)
![Environment](https://img.shields.io/badge/environment-console%20%2F%20terminal-orange.svg)
![Dependencies](https://img.shields.io/badge/dependencies-none%20%28native%20libs%29-green.svg)

Un script de automatización desarrollado en Python ejecutable desde consola, diseñado específicamente para agilizar el proceso de diagnóstico inicial en hardware, sistema y conectividad de red cuando una estación de trabajo presenta fallas en sitio. 

Esta herramienta permite a los técnicos de soporte optimizar los tiempos de respuesta, estandarizar las pruebas rutinarias de mantenimiento y recolectar evidencias de manera inmediata sin necesidad de configuraciones complejas en la máquina afectada.

## 🚀 Características Clave

* **Recolección Automatizada del Sistema:** Obtiene de forma instantánea el nombre del equipo (*Hostname*), la dirección IP local asignada en la interfaz activa y la versión exacta del Sistema Operativo instalado.
* **Diagnóstico Flash de Red:** Ejecuta de manera secuencial pruebas de conectividad mediante comandos de red controlados (*Pings*):
  * **Conexión Local:** Diagnóstico hacia la puerta de enlace predeterminada (*Gateway*) o servidor local para verificar el estado del switch/enrutador físico.
  * **Conexión Externa:** Verificación de salida real a Internet apuntando a los servidores DNS públicos de Google (`8.8.8.8`).
* **Cero Dependencias Externas:** Desarrollado utilizando exclusivamente la librería estándar de Python. Puede ser ejecutado de inmediato en cualquier computadora corporativa sin necesidad de usar `pip` o instalar paquetes de terceros.
* **Generación Automática de Reportes (Logs):** Exporta exactamente los mismos resultados estructurados de la consola hacia una bitácora técnica de texto plano (`reporte_diagnostico.txt`) en la misma carpeta, sirviendo como historial técnico o soporte para el software de mesa de ayuda.

## 🛠️ Arquitectura y Tecnologías

* **Lenguaje base:** Python 3.x
* **Módulos Nativos Utilizados:**
  * `os` & `subprocess`: Para interactuar con los comandos del sistema operativo de manera controlada.
  * `socket`: Para la resolución y captura de direcciones IP locales del adaptador de red activo.
  * `platform`: Para identificar la arquitectura y versión detallada del entorno operativo.

## 📦 Instalación y Modo de Uso

### Prerrequisitos
Tener instalado Python 3.x en el equipo de soporte o en la máquina donde se realizará la auditoría.

### Pasos para Ejecución

1. **Clonar el repositorio o descargar el script:**
   ```bash
   git clone [https://github.com/DyR7666GYFT/it-support-automation.git](https://github.com/DyR7666GYFT/it-support-automation.git)
2. **Navegar al directorio del proyecto:**
   ```bash
   cd it-support-automation
3. **Ejecutar el script en la terminal (CMD, PowerShell o Bash):**
   ```bash
   python main.py
 4. Revisar la terminal para ver el diagnóstico en tiempo real y abrir el archivo reporte_diagnostico.txt generado automáticamente en el mismo directorio.
