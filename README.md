### 🐍`it-support-automation`
Crea el archivo `README.md` dentro de la carpeta local de tu script de Python antes de subirlo, o directamente en la interfaz web de ese repositorio, y pega este contenido:

```markdown
# Script de Automatización de Diagnóstico TI 🛠️

Un script automatizado en Python ejecutado a través de la consola/terminal, desarrollado específicamente para agilizar el proceso de diagnóstico inicial en hardware y conectividad de red cuando un equipo de cómputo presenta fallas en sitio.

Este proyecto surge como una herramienta práctica para técnicos de soporte que buscan estandarizar las pruebas rutinarias de mantenimiento predictivo y correctivo, reduciendo tiempos de atención.

## 🚀 Características Clave

* **Recolección de Información del Sistema:** Obtiene de forma automática datos del entorno local como el Hostname, la dirección IP local interna y la versión del Sistema Operativo.
* **Diagnóstico Flash de Conectividad:** Ejecuta de forma secuencial pruebas de conectividad (Pings controlados) tanto a nivel local (Puerta de enlace/Gateway) como externo (DNS públicos de Google `8.8.8.8`) para aislar problemas de red.
* **Cero Dependencias Externas:** Programado utilizando estrictamente módulos nativos de Python, permitiendo su ejecución inmediata en cualquier terminal de la empresa sin configuraciones previas con `pip`.
* **Generación Automatizada de Reportes:** Exporta los resultados completos de la consola directamente a una bitácora técnica de texto (`reporte_diagnostico.txt`), sirviendo como evidencia para el historial de soporte.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librerías Nativas:** `os`, `subprocess`, `socket`, `platform`

## 📦 Modo de Uso

1. Clonar este repositorio o descargar el archivo `main.py`.
2. Abrir la terminal o CMD en la ruta del archivo.
3. Ejecutar el script con el siguiente comando:
   ```bash
   python main.py
4. Revisar la terminal para ver el diagnóstico en tiempo real y abrir el archivo reporte_diagnostico.txt generado automáticamente en el mismo directorio.
