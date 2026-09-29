# Justificación de Importaciones y Cumplimiento de Reglas de Arquitectura

Este documento detalla y audita las cláusulas de importación (`import`) utilizadas en una clase representativa de cada capa desarrollada por la **Persona 1**, demostrando el cumplimiento estricto del Principio de Inversión de Dependencias (DIP) y los límites de Clean Architecture exigidos por la rúbrica del taller.

---

## 1. Capa de Dominio
* **Clase auditada:** `Prestamo`
* **Archivo:** `dominio/prestamo.py`
* **Cláusulas de importación utilizadas:**
  ```python
  from datetime import date
  ```
* **Justificación de cumplimiento:** Esta clase cumple perfectamente con las restricciones de la rúbrica. Al encontrarse en el núcleo del sistema, **no importa ningún elemento de la capa de aplicación, de infraestructura ni la librería externa `sqlite3`**. Únicamente utiliza componentes primitivos y nativos del lenguaje Python (`date`), manteniéndose como código de negocio puro, aislado de la base de datos y de los canales de entrega.

---

## 2. Capa de Aplicación (Casos de Uso)
* **Clase auditada:** `RegistrarPrestamo`
* **Archivo:** `aplicacion/casos_uso/registrar_prestamo.py`
* **Cláusulas de importación utilizadas:**
  ```python
  from dominio.prestamo import Prestamo
  from dominio.excepciones import LimitePrestamosExcedido, EstudianteConMultaPendiente, EquipoNoDisponible
  from aplicacion.puertos.repo_prestamo import RepoPrestamo
  from aplicacion.puertos.repo_estudiante import RepoEstudiante
  from aplicacion.puertos.repo_equipo import RepoEquipo
  from aplicacion.puertos.proveedor_fecha import ProveedorFecha
  ```
* **Justificación de cumplimiento:** Este archivo cumple rigurosamente con la norma técnica de Clean Architecture. **No importa la librería `sqlite3` ni clases concretas de la capa de infraestructura**. Sus dependencias se dirigen exclusivamente hacia adentro de la arquitectura (hacia las entidades `Prestamo` y las excepciones del `dominio`) o de manera horizontal hacia las interfaces de la misma capa (`aplicacion/puertos/`). La lógica transaccional del caso de uso es agnóstica a la tecnología física de persistencia.

---

## 3. Capa de Infraestructura (Adaptadores de Persistencia)
* **Clase auditada:** `SQLitePrestamo`
* **Archivo:** `infraestructura/sqlite_prestamo.py`
* **Cláusulas de importación utilizadas:**
  ```python
  import sqlite3
  from datetime import datetime, date
  from aplicacion.puertos.repo_prestamo import RepoPrestamo
  from dominio.prestamo import Prestamo
  from typing import List
  ```
* **Justificación de cumplimiento:** Al encontrarse en la capa más externa, es completamente válido que este archivo importe la librería de bajo nivel `sqlite3` para gestionar el detalle técnico de las consultas SQL, las tablas y la persistencia en disco. Cumple a cabalidad con el **Principio de Inversión de Dependencias (DIP)** porque no amarra la aplicación a la base de datos, sino que **la base de datos se adapta al sistema implementando el puerto abstracto (`RepoPrestamo`)** definido por la capa de aplicación.

---

## 4. Orquestador de Arranque (Composición Global)
* **Archivo:** `main.py`
* **Cláusulas de importación utilizadas (Infraestructura):**
  ```python
  import sqlite3
  from infraestructura.sqlite_estudiantes import SQLiteEstudiantes
  from infraestructura.memoria_prestamo import MemoriaPrestamo
  from infraestructura.sqlite_prestamo import SQLitePrestamo
  ```
* **Justificación de cumplimiento:** De acuerdo con la directriz explícita del curso, **`main.py` es el único archivo autorizado en todo el proyecto para importar clases concretas de infraestructura**. Su única función es actuar como la raíz de composición (*Composition Root*), encargándose de instanciar los motores reales de base de datos e inyectarlos de forma transparente a través de los constructores de los casos de uso, evitando que el acoplamiento técnico se propague al resto del software.
