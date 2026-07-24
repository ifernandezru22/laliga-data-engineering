# LaLiga Data Engineering Project

Proyecto de aprendizaje orientado a construir un pipeline de Data Engineering a partir de datos históricos de partidos de LaLiga.

## Objetivo

Construir progresivamente un sistema capaz de:

* Ingerir datos históricos de partidos.
* Validar la calidad de los datos.
* Limpiar y transformar la información.
* Cargar los datos en una base de datos.
* Construir modelos analíticos.
* Automatizar el pipeline.
* Obtener métricas históricas por equipo y temporada.

## Dataset

El dataset contiene partidos de LaLiga desde la temporada 1995-96 hasta la temporada 2025-26.

Cada fila representa un partido.

### Columnas

| Columna    | Significado                                           |
| ---------- | ----------------------------------------------------- |
| `Season`   | Temporada del partido                                 |
| `Date`     | Fecha del partido                                     |
| `HomeTeam` | Equipo local                                          |
| `AwayTeam` | Equipo visitante                                      |
| `FTHG`     | Goles del equipo local al final del partido           |
| `FTAG`     | Goles del equipo visitante al final del partido       |
| `FTR`      | Resultado final: `H` local, `A` visitante, `D` empate |
| `HTHG`     | Goles del local al descanso                           |
| `HTAG`     | Goles del visitante al descanso                       |
| `HTR`      | Resultado al descanso: `H`, `A` o `D`                 |

## Exploración inicial

Durante la primera inspección del dataset se ha comprobado lo siguiente:

* 31 temporadas disponibles.
* No existen filas completamente duplicadas.
* Todas las temporadas completas contienen 380 partidos.
* La temporada 2025-26 está incompleta porque los datos fueron recopilados antes de finalizar la temporada.
* Existen 2 partidos con valores nulos en `HTHG`, `HTAG` y `HTR`.
* No existen valores nulos en los datos del resultado final.
* Los valores posibles de `FTR` son `H`, `A` y `D`.
* Los valores posibles de `HTR` son `H`, `A`, `D` y valores nulos.
* El rango de fechas del dataset va desde el 2 de septiembre de 1995 hasta el 27 de octubre de 2025.

### Partidos con información incompleta al descanso

Los dos registros afectados son:

* Athletic Bilbao 1-0 Deportivo de La Coruña — 19/11/1995
* Valladolid 0-3 Betis — 10/01/1999

Se ha decidido conservar estos registros porque el resultado final es válido. Únicamente se excluirán de análisis que requieran información del descanso.

## Validaciones de consistencia

Se está comprobando que:

* `FTHG > FTAG` implique `FTR = H`.
* `FTHG < FTAG` implique `FTR = A`.
* `FTHG == FTAG` implique `FTR = D`.

## Estructura actual

```text
laliga-data-engineering/
├── data/
│   └── LaLiga_Matches.csv
├── src/
│   └── explore_data.py
├── sql/
├── tests/
└── README.md
```
