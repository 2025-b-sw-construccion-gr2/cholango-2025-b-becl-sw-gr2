# 📖 GUÍA PASO A PASO - EXAMEN CI/CD

## 🎯 Objetivo
Esta guía te llevará paso a paso para completar el examen exitosamente.

---

## PARTE 1: PREPARAR TU REPOSITORIO EN GITHUB

### Paso 1.1: Acceder a tu repositorio
1. Ve a la organización del curso en GitHub
2. Encuentra tu repositorio asignado
3. Copia la URL del repositorio (botón verde "Code")

### Paso 1.2: Clonar el repositorio
Abre tu terminal y ejecuta:
```bash
git clone <URL-de-tu-repositorio>
cd <nombre-de-tu-repositorio>
```

---

## PARTE 2: SUBIR EL PROYECTO

### Paso 2.1: Copiar los archivos del proyecto
Copia TODOS los archivos que te he proporcionado en tu repositorio clonado.

La estructura debe quedar así:
```
tu-repositorio/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
│   └── converter.py
├── tests/
│   ├── __init__.py
│   └── test_converter.py
├── .flake8
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Paso 2.2: Verificar que todo esté en su lugar
```bash
# Ver la estructura de carpetas
ls -la

# Deberías ver:
# .github/
# src/
# tests/
# .flake8
# .gitignore
# pyproject.toml
# requirements.txt
# README.md
```

---

## PARTE 3: VERIFICAR LOCALMENTE (IMPORTANTE)

Antes de subir a GitHub, vamos a asegurarnos de que todo funciona.

### Paso 3.1: Crear entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Activar (Linux/Mac)
source venv/bin/activate
```

### Paso 3.2: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 3.3: Probar el programa
```bash
python src/converter.py
```
- Selecciona opción 1
- Ingresa 25
- Deberías ver la conversión de temperatura

### Paso 3.4: Ejecutar las verificaciones

**A. Linter (Flake8)**
```bash
flake8 src/ tests/
```
✅ No debe mostrar ningún error

**B. Formato (Black)**
```bash
black --check src/ tests/
```
✅ Debe decir "All done!" o "would reformat"

Si dice "would reformat", ejecuta:
```bash
black src/ tests/
```

**C. Tests**
```bash
pytest tests/ --cov=src --cov-report=term
```
✅ Todos los tests deben pasar (verde)
✅ La cobertura debe ser alta (>90%)

**D. Build**
```bash
python -m py_compile src/converter.py
```
✅ No debe dar errores

---

## PARTE 4: CONFIGURAR GIT Y RAMAS

### Paso 4.1: Crear rama develop (si no existe)
```bash
# Ver ramas actuales
git branch

# Crear rama develop
git checkout -b develop
```

### Paso 4.2: Subir rama develop a GitHub
```bash
git add .
git commit -m "Initial commit: Unit converter project"
git push -u origin develop
```

---

## PARTE 5: TRABAJAR CON FEATURES

### Paso 5.1: Crear rama feature
```bash
# Asegúrate de estar en develop
git checkout develop

# Crear nueva feature
git checkout -b feature/add-converter-functionality
```

### Paso 5.2: Hacer cambios simulados
Para demostrar el flujo, vamos a hacer un pequeño cambio:

Abre `README.md` y agrega al final:
```markdown
## 🎓 Notas del Examen
- Pipeline configurado correctamente
- Todas las pruebas pasando
- Código formateado y limpio
```

### Paso 5.3: Commit y push
```bash
git add README.md
git commit -m "docs: Add exam notes section"
git push -u origin feature/add-converter-functionality
```

---

## PARTE 6: CREAR PULL REQUEST

### Paso 6.1: Ir a GitHub
1. Ve a tu repositorio en GitHub
2. Verás un banner amarillo que dice "Compare & pull request"
3. Haz clic en ese botón

### Paso 6.2: Configurar el PR
- **Base**: `develop`
- **Compare**: `feature/add-converter-functionality`
- **Título**: "Add converter functionality"
- **Descripción**: 
  ```
  ## Cambios
  - Implementado convertidor de unidades
  - Agregados tests unitarios
  - Configurado pipeline CI/CD
  
  ## Checklist
  - [x] Pipeline pasa todos los checks
  - [x] Tests incluidos
  - [x] Documentación actualizada
  ```

### Paso 6.3: Crear el PR
Haz clic en "Create Pull Request"

---

## PARTE 7: VERIFICAR EL PIPELINE

### Paso 7.1: Ver el Pipeline ejecutándose
1. En el PR, verás checks ejecutándose
2. Haz clic en "Details" junto a cada check
3. Observa los logs de:
   - ✅ Lint
   - ✅ Format
   - ✅ Test
   - ✅ Build

### Paso 7.2: Esperar a que todo pase
Espera a que todos los checks estén en verde ✅

**Si algo falla:**
- Lee el error en los logs
- Corrige el problema localmente
- Haz commit y push de nuevo
- El pipeline se ejecutará automáticamente

---

## PARTE 8: SIMULAR APROBACIÓN

Como estás trabajando sola, puedes hacer el merge directamente una vez que el pipeline pase.

### Paso 8.1: Merge del PR
1. Una vez que todos los checks estén verdes
2. Haz clic en "Merge pull request"
3. Confirma el merge
4. Opcionalmente, elimina la rama feature

---

## PARTE 9: DOCUMENTAR PARA EL EXAMEN

### Paso 9.1: Tomar capturas de pantalla

**Captura 1: Estructura del proyecto**
- Captura de tu repositorio mostrando la estructura de carpetas

**Captura 2: Pipeline exitoso**
- Captura de la pestaña "Actions" mostrando el workflow en verde

**Captura 3: Detalles de cada job**
- Captura mostrando los 4 jobs: lint, format, test, build

**Captura 4: Pull Request**
- Captura del PR con todos los checks pasados

**Captura 5: Cobertura de tests**
- Captura del reporte de cobertura (puedes ejecutar localmente y capturar)

### Paso 9.2: Preparar tu entrega

Crea un documento que incluya:

1. **Enlace al repositorio**
2. **Enlace al Pull Request**
3. **Capturas de pantalla**
4. **Explicación breve** de cómo funciona el pipeline

---

## ✅ CHECKLIST FINAL

Antes de entregar, verifica que tienes:

- [ ] Proyecto subido al repositorio de la organización
- [ ] Estructura de carpetas correcta
- [ ] Archivo `.github/workflows/ci.yml` configurado
- [ ] Linter (Flake8) funcionando
- [ ] Format check (Black) funcionando
- [ ] Tests con pytest ejecutándose
- [ ] Build generándose correctamente
- [ ] Al menos un Pull Request creado
- [ ] Pipeline ejecutándose en verde
- [ ] README completo y claro
- [ ] Capturas de pantalla tomadas

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Si el linter falla:
```bash
# Ver qué está mal
flake8 src/ tests/

# Arreglar automáticamente lo que se pueda
black src/ tests/
```

### Si los tests fallan:
```bash
# Ver detalles del error
pytest tests/ -v

# Ejecutar un test específico
pytest tests/test_converter.py::TestTemperatureConversion::test_celsius_to_fahrenheit -v
```

### Si el pipeline no se activa:
- Verifica que el archivo esté en `.github/workflows/ci.yml`
- Verifica que hayas hecho push de ese archivo
- Ve a Settings → Actions → General → Allow all actions

### Si GitHub Actions está deshabilitado:
- Ve a Settings → Actions → General
- Selecciona "Allow all actions and reusable workflows"

---

## 📞 TIPS FINALES

1. **No tengas miedo de romper cosas** - Git te permite volver atrás
2. **Lee los errores del pipeline** - son muy descriptivos
3. **Prueba todo localmente primero** - evita commits innecesarios
4. **El README es tu carta de presentación** - manténlo claro
5. **Si algo no funciona, Google es tu amigo** - pero primero revisa los logs

---

## 🎉 ¡ÉXITO!

Si seguiste todos estos pasos, deberías tener:
- ✅ Un proyecto funcionando
- ✅ Pipeline de CI/CD completo
- ✅ Buenas prácticas implementadas
- ✅ Documentación clara
- ✅ Todo listo para entregar

**¡Mucha suerte en tu examen!** 🚀
