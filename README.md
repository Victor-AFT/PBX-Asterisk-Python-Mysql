
# ☎️ PBX-Asterisk-Python-MySQL — Integración PBX con AGI en Python y Base de Datos

Este repositorio contiene un conjunto de scripts diseñados para **integrar Asterisk PBX**, **Python (AGI/AMI)** y **MySQL**, permitiendo automatizar flujos de llamadas, gestionar información dinámica y crear lógicas de negocio avanzadas en un entorno VoIP.

Basado en el ecosistema de scripts existentes como los mostrados en tu repositorio `AGI_Asterisk` (Scripts con Asterisk). citeturn15search103

---
## 🚀 Objetivo del proyecto
Implementar una solución que permita:
- Ejecutar **scripts Python como AGI** para controlar llamadas.
- Consultar o almacenar información en **MySQL**.
- Automatizar decisiones de enrutamiento, validación, lookup de datos, etc.
- Ampliar la funcionalidad del PBX de manera modular y escalable.

---
## 📁 Contenido sugerido del repositorio
```
PBX-Asterisk-Python-Mysql/
├── agi_scripts/
│   ├── main_agi.py            # Script AGI principal
│   ├── db_connector.py        # Conexión MySQL
│   └── utils.py               # Funciones auxiliares
├── sql/
│   ├── schema.sql             # Tablas necesarias
│   └── examples.sql
├── asterisk/
│   └── extensions_custom.conf # Integración AGI
└── README.md
```
*(Ajustable según tus archivos reales)*

---
## 🧩 ¿Qué es AGI?
El **Asterisk Gateway Interface (AGI)** permite ejecutar scripts externos en lenguajes como Python para controlar flujos de llamadas.

Más sobre AGI en Python:
- Se pueden usar módulos AGI como `pyst` para interactuar con Asterisk. citeturn15search108
- AGI es ideal para tareas como:
  - Búsqueda en base de datos.
  - Validación de Caller ID.
  - Enrutamiento dinámico.
  - Integración con APIs.

Los scripts en tu otro repo (`AGI_Asterisk`) muestran funcionalidades típicas como validación y enrutamiento. citeturn15search103

---
## 🗄️ Uso de MySQL como backend
Asterisk soporta integración con MySQL para:
- Guardado de registros de llamadas.
- Lookup de extensiones.
- Gestión de usuarios.
- Enrutamiento dinámico.

También existe la modalidad **Asterisk Realtime Architecture**, donde toda la configuración se guarda en MySQL para permitir cambios sin reiniciar Asterisk. citeturn15search107

---
## ▶️ Cómo usar este sistema
### 1. Clonar el repositorio
```bash
git clone https://github.com/Victor-AFT/PBX-Asterisk-Python-Mysql
cd PBX-Asterisk-Python-Mysql
```

### 2. Configurar acceso MySQL
Edita `db_connector.py` (o el archivo correspondiente):
```python
HOST = "localhost"
USER = "asterisk"
PASSWORD = "password"
DATABASE = "pbx"
```

### 3. Configurar Asterisk para usar el script AGI
En `extensions_custom.conf`:
```
exten => _X.,1,AGI(main_agi.py,${CALLERID(num)})
```

### 4. Ejecutar llamadas de prueba
Una vez recargado el dialplan, las llamadas ejecutarán el script Python.

---
## 📚 Recursos recomendados
- Documentación de Asterisk + Python (AGI/AMI). citeturn15search104
- Uso de Python para scripting AGI en FreePBX. citeturn15search105
- Cómo combinar Asterisk con MySQL en arquitectura realtime. citeturn15search107
- Librería `pyst` para AGI/AMI en Python. citeturn15search108

---
## 🔧 Mejoras futuras
- Implementar ARI (Asterisk REST Interface).
- Crear API REST externa para gestionar datos del PBX.
- Integrar dashboards con Grafana.
- Añadir unit tests.

---
## 🤝 Contribuciones
Las contribuciones son bienvenidas.
Puedes enviar Pull Requests o crear Issues.

---
## 📜 Licencia
Uso libre para fines educativos y profesionales.

