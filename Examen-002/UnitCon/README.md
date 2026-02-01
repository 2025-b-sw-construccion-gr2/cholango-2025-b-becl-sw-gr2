# 🔄 Convertidor de Unidades

Proyecto simple de conversión de unidades desarrollado con Python, implementando buenas prácticas de desarrollo y CI/CD con GitHub Actions.

## 📋 Descripción

Este proyecto permite convertir entre diferentes unidades de medida:
- **Temperatura**: Celsius ↔ Fahrenheit
- **Longitud**: Metros ↔ Pies
- **Peso**: Kilogramos ↔ Libras

## 🚀 Cómo ejecutar el proyecto localmente

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio**
```bash
git clone <url-de-tu-repositorio>
cd unit_converter
```

2. **Crear un entorno virtual (opcional pero recomendado)**
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### Ejecutar el programa

```bash
python src/converter.py
```

El programa mostrará un menú interactivo donde podrás seleccionar el tipo de conversión y el valor a convertir.

### Ejemplo de uso

```
=== Convertidor de Unidades ===

1. Temperatura (Celsius ↔ Fahrenheit)
2. Longitud (Metros ↔ Pies)
3. Peso (Kilogramos ↔ Libras)

Seleccione una opción (1-3): 1
Ingrese el valor a convertir: 25

25.0°C = 77.00°F
25.0°F = -3.89°C
```

## 🧪 Ejecutar las pruebas

```bash
# Ejecutar todas las pruebas
pytest tests/

# Ejecutar con reporte de cobertura
pytest tests/ --cov=src --cov-report=term
```

## 🛠️ Pipeline de CI/CD

El proyecto utiliza **GitHub Actions** para automatizar las verificaciones de calidad de código. El pipeline se ejecuta automáticamente en cada `push` y `pull request`.

### Estructura del Pipeline

El archivo de configuración se encuentra en `.github/workflows/ci.yml` y ejecuta los siguientes jobs en orden:

#### 1️⃣ **Lint** (Análisis estático)
- **Herramienta**: Flake8
- **Propósito**: Verifica que el código siga las convenciones de estilo PEP 8
- **Se ejecuta en**: `src/` y `tests/`
- **Falla si**: Hay errores de sintaxis o violaciones de estilo

```bash
# Ejecutar localmente:
flake8 src/ tests/
```

#### 2️⃣ **Format Check** (Verificación de formato)
- **Herramienta**: Black
- **Propósito**: Valida que el código esté correctamente formateado
- **Se ejecuta en**: `src/` y `tests/`
- **Falla si**: El código no está formateado según Black

```bash
# Ejecutar localmente:
black --check src/ tests/

# Auto-formatear código:
black src/ tests/
```

#### 3️⃣ **Test** (Pruebas unitarias)
- **Herramienta**: pytest + pytest-cov
- **Propósito**: Ejecuta todas las pruebas unitarias y genera reporte de cobertura
- **Cobertura**: Mide qué porcentaje del código está cubierto por tests
- **Genera**: Reporte HTML con resultados detallados

```bash
# Ejecutar localmente:
pytest tests/ --cov=src --cov-report=term --cov-report=html
```

#### 4️⃣ **Build** (Construcción)
- **Depende de**: lint, format y test (deben pasar primero)
- **Propósito**: Verifica que el proyecto se pueda compilar y empaquetar
- **Genera**: Artefactos del build en la carpeta `build/`
- **Valida**: Sintaxis de Python y crea paquete de distribución

```bash
# Ejecutar localmente:
python -m py_compile src/converter.py
```

### Flujo de ejecución

```
┌─────────────────┐
│  Push/PR        │
└────────┬────────┘
         │
    ┌────┴────┐
    │ Trigger │
    └────┬────┘
         │
    ┌────┴──────────────────────────┐
    │                               │
┌───▼────┐  ┌────────┐  ┌──────┐   │
│ Lint   │  │ Format │  │ Test │   │ (Paralelo)
└───┬────┘  └────┬───┘  └───┬──┘   │
    │            │          │       │
    └────────────┴──────────┴───────┘
                 │
            ┌────▼────┐
            │ Build   │ (Solo si todos pasan)
            └─────────┘
```

### Estados del Pipeline

- ✅ **Success**: Todos los jobs pasaron correctamente
- ❌ **Failure**: Al menos un job falló
- 🟡 **In Progress**: El pipeline está ejecutándose

### Visualizar resultados

1. Ve a la pestaña **Actions** en tu repositorio de GitHub
2. Selecciona el workflow run que quieres revisar
3. Haz clic en cada job para ver logs detallados
4. Descarga los artefactos generados (reportes de cobertura y build)

## 📁 Estructura del Proyecto

```
unit_converter/
│
├── .github/
│   └── workflows/
│       └── ci.yml              # Configuración del pipeline CI/CD
│
├── src/
│   ├── __init__.py
│   └── converter.py            # Código principal del convertidor
│
├── tests/
│   ├── __init__.py
│   └── test_converter.py       # Pruebas unitarias
│
├── .flake8                     # Configuración de Flake8
├── pyproject.toml              # Configuración de Black
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

## 🔄 Flujo de trabajo con Git

### Crear una nueva feature

```bash
# 1. Crear rama desde develop
git checkout develop
git pull origin develop
git checkout -b feature/nombre-de-tu-feature

# 2. Hacer cambios y commits
git add .
git commit -m "Descripción de los cambios"

# 3. Push a GitHub
git push origin feature/nombre-de-tu-feature
```

### Crear Pull Request

1. Ve a GitHub y crea un Pull Request desde tu rama `feature/*` hacia `develop`
2. Espera a que el pipeline de CI pase (todos los checks en verde ✅)
3. Si trabajas en equipo, solicita revisión de código
4. Una vez aprobado, haz merge del PR

### Buenas prácticas

- ✅ Siempre trabaja en ramas `feature/*`
- ✅ Asegúrate de que el pipeline pase antes de hacer merge
- ✅ Escribe mensajes de commit descriptivos
- ✅ Mantén el código formateado con Black
- ✅ Agrega tests para nuevas funcionalidades

## 📊 Cobertura de Tests

El proyecto incluye tests para:
- ✅ Conversiones de temperatura
- ✅ Conversiones de longitud
- ✅ Conversiones de peso
- ✅ Casos edge (valores cero, negativos)

Para ver el reporte de cobertura HTML:
```bash
pytest tests/ --cov=src --cov-report=html
# Abre htmlcov/index.html en tu navegador
```

## 🛡️ Verificaciones de Calidad

Antes de hacer commit, puedes ejecutar todas las verificaciones localmente:

```bash
# 1. Lint
flake8 src/ tests/

# 2. Format
black --check src/ tests/

# 3. Tests
pytest tests/ --cov=src

# 4. Build
python -m py_compile src/converter.py
```

## 📝 Dependencias

- **pytest**: Framework de testing
- **pytest-cov**: Plugin para medir cobertura de código
- **flake8**: Linter para Python
- **black**: Formateador automático de código

## 👤 Autor

Proyecto desarrollado para el examen de Construcción y Evolución de Software.

## 📄 Licencia

Este proyecto es de uso académico.

---

**Nota**: Este README incluye toda la información necesaria para ejecutar el proyecto, entender el pipeline de CI/CD y seguir las buenas prácticas de desarrollo.

---

## 🎓 Notas del Examen
- Pipeline configurado correctamente
- Todas las pruebas pasando
- Código formateado y limpio
