import os
import subprocess
import socket
import platform

# Diagnóstico rápido de red para soporte técnico en sitio
# Autor: Dylan Ricardo Martínez — Mantenimiento de Sistemas Informáticos

GATEWAY     = "192.168.1.1"
DNS_EXT     = "8.8.8.8"
REPORTE_TXT = "reporte_diagnostico.txt"

SEP  = "=" * 65
LINE = "-" * 65


def info_equipo():
    hostname = socket.gethostname()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except OSError:
        try:
            ip = socket.gethostbyname(hostname)
        except OSError:
            ip = "127.0.0.1"

    return {
        "hostname": hostname,
        "ip": ip,
        "so": f"{platform.system()} {platform.release()}"
    }


def ping(host, paquetes=3):
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        r = subprocess.run(
            ["ping", flag, str(paquetes), host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=6
        )
        return r.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def main():
    eq = info_equipo()
    log = []

    def out(msg=""):
        print(msg)
        log.append(msg)

    out(SEP)
    out("  DIAGNÓSTICO DE RED — SOPORTE TÉCNICO EN SITIO")
    out(SEP)
    out(f"  Hostname  : {eq['hostname']}")
    out(f"  IP Local  : {eq['ip']}")
    out(f"  S.O.      : {eq['so']}")
    out(LINE)

    out(f"[*] Gateway local ({GATEWAY})...")
    if ping(GATEWAY):
        out(f"[+] Gateway OK — enlace físico activo.")
    else:
        out(f"[-] Sin respuesta del gateway — revisar cable o configuración IP.")

    out(LINE)

    out(f"[*] Salida a Internet ({DNS_EXT})...")
    if ping(DNS_EXT):
        out(f"[+] Internet OK — salida completa verificada.")
    else:
        out(f"[-] Sin respuesta externa — posible falla en ISP o enrutamiento.")

    out(SEP)
    out("  FIN DEL DIAGNÓSTICO")
    out(SEP)

    # Guardar evidencia en disco
    try:
        with open(REPORTE_TXT, "w", encoding="utf-8") as f:
            f.write("\n".join(log))
        print(f"\n[+] Reporte guardado en '{REPORTE_TXT}'")
    except OSError as e:
        print(f"\n[-] No se pudo guardar el reporte: {e}")


if __name__ == "__main__":
    main()
