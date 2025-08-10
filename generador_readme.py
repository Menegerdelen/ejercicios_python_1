import os

# Emojis por tipo de carpeta
emojis = {
    "variables": "🔤",
    "operadores": "➕",
    "condicional": "🧩",
    "ciclo": "🔁",
    "estructuradato": "🧵",
    "funciones": "🛠️",
    "archivos": "📂",
    "excepciones": "⚠️",
}

contenido = """# 📘 Repositorio de Ejercicios Python

Este repositorio contiene ejercicios organizados por tipo de conocimiento. Cada carpeta incluye:

- 💡 Archivo principal con la solución.
- 🧠 Archivo comentado con explicaciones línea por línea.

---

## 📂 Índice de Ejercicios
"""

for carpeta in sorted(os.listdir(".")):
    if carpeta.startswith("e") and os.path.isdir(carpeta):
        # Detectar el emoji según el nombre de la carpeta
        emoji = "📁"
        for clave in emojis:
            if clave in carpeta.lower():
                emoji = emojis[clave]
                break

        contenido += f"\n### {emoji} `{carpeta}`\n"

        archivos = [f for f in os.listdir(carpeta) if f.endswith(".py")]
        principales = [f for f in archivos if "comentado" not in f.lower()]
        comentados = [f for f in archivos if "comentado" in f.lower()]

        for archivo in sorted(principales):
            nombre = archivo.replace(".py", "").replace("_", " ").capitalize()
            contenido += f"- `{archivo}` – {nombre}\n"

        for archivo in sorted(comentados):
            contenido += f"  - 🧠 `{archivo}` – Versión comentada\n"

contenido += """

---

## 🎓 Filosofía de trabajo

Cada ejercicio busca enseñar, no solo funcionar.  
Incluye versiones comentadas para facilitar la comprensión paso a paso.

> *“El código debe enseñar, no solo funcionar.”*
"""

# Guardar el README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(contenido)

print("✅ README.md generado con estilo visual y didáctico.")
