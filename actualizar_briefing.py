import datetime

def generar_briefing():
    # 1. Configurar fechas de hoy
    hoy = datetime.datetime.now()
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    fecha_larga = f"{dias_semana[hoy.weekday()]}, {hoy.day} de {meses[hoy.month-1]} de {hoy.year}"

    # 2. Leer la plantilla base
    with open("template.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # 3. Datos Macro y financieros simulados/dinámicos (puedes expandir esto en el futuro)
    # Aquí definimos las variables que irán dentro de los marcadores del HTML
    datos_actualizacion = {
        "{{FECHA_LARGA}}": fecha_larga,
        # Si tu plantilla usa otros placeholders específicos, los mapeas aquí.
        # Ejemplo si usaras {{TIPO_INTERES}}: "4.00%"
    }

    # 4. Reemplazar los placeholders en el contenido de la plantilla
    # Como el HTML completo de la respuesta anterior ya está maquetado, si tu plantilla
    # contiene textos fijos y solo cambias la fecha, esto actualizará la fecha automáticamente.
    for placeholder, valor in datos_actualizacion.items():
        html_content = html_content.replace(placeholder, valor)

    # 5. Sobrescribir el index.html principal que lee GitHub Pages
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"✅ Briefing actualizado con éxito para el {fecha_larga}")

if __name__ == "__main__":
    generar_briefing()
