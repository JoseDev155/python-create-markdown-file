# Create a Markdown summary file following the user's instructions.
import pypandoc

md_content = """
# Resumen – Estándares IEEE 802.11 (Wi-Fi)

## 1. Concepto de los estándares IEEE 802.11
- Conjunto de **especificaciones para redes de área local inalámbricas (WLAN)**.
- Desarrollados por el **IEEE (Institute of Electrical and Electronics Engineers)**.
- Definen normas para **redes Wi-Fi** garantizando interoperabilidad entre dispositivos de diferentes fabricantes.
- Cubren:
  - **Capa física (Physical Layer)**
  - **Capa de enlace de datos (Data Link Layer)** del modelo OSI.
- Incluyen especificaciones sobre:
  - transmisión de datos
  - seguridad
  - calidad de servicio (QoS).

---

# 2. Historia y evolución de los estándares

### 1997 – IEEE 802.11 (Original)
- Primer estándar Wi-Fi.
- Velocidad máxima: **2 Mbps**.
- Banda de frecuencia: **2.4 GHz**.

### 1999 – IEEE 802.11a y 802.11b
- **802.11a**
  - Banda: **5 GHz**
  - Velocidad: **hasta 54 Mbps**
- **802.11b**
  - Banda: **2.4 GHz**
  - Velocidad: **hasta 11 Mbps**
  - Mayor alcance que 802.11a.

### 2003 – IEEE 802.11g
- Velocidad: **54 Mbps**.
- Banda: **2.4 GHz**.
- Compatible con **802.11b**.

### 2009 – IEEE 802.11n
- Introducción de **MIMO**.
- Velocidad teórica: **hasta 600 Mbps**.
- Operación en **2.4 GHz y 5 GHz**.

---

# 3. Características de estándares importantes

## IEEE 802.11a
- Ratificado: **1999**.
- Frecuencia: **5 GHz**.
- Velocidad máxima: **54 Mbps**.

### Ventajas
- Menor interferencia.
- Banda menos congestionada.

### Desventajas
- **Menor alcance**.
- Menor capacidad para atravesar paredes.

---

## IEEE 802.11b
- Velocidad: **11 Mbps**.
- Frecuencia: **2.4 GHz**.
- Mayor alcance y mejor penetración de obstáculos.
- **Costo más bajo**, lo que favoreció su adopción.

Uso común:
- hogares
- pequeñas oficinas.

---

## IEEE 802.11g
- Velocidad: **54 Mbps**.
- Frecuencia: **2.4 GHz**.
- Compatible con **802.11b**.
- Usa **OFDM (Orthogonal Frequency Division Multiplexing)**.

Importancia:
- Estándar dominante durante varios años.

---

## IEEE 802.11n
Características principales:

- Introducción de **MIMO (Multiple Input Multiple Output)**.
- Uso de **múltiples antenas** para transmisión y recepción.
- Canales de **40 MHz**.
- Velocidad teórica: **hasta 600 Mbps**.
- Funcionamiento en **2.4 GHz y 5 GHz**.

Impacto:
- Mejora significativa en **velocidad, cobertura y estabilidad**.

---

## IEEE 802.11ac (Wi-Fi 5)

Características:

- Velocidad teórica: **hasta 6.93 Gbps**.
- Uso de **MU-MIMO** (Multi-User MIMO).
- **Beamforming** para dirigir la señal hacia los dispositivos.
- Canales de hasta **160 MHz**.
- Opera **solo en 5 GHz**.

Ventaja:
- Mejor rendimiento con **muchos dispositivos conectados**.

---

## IEEE 802.11ax (Wi-Fi 6)

Características principales:

- Velocidad teórica: **hasta 9.6 Gbps**.
- Tecnología **OFDMA** para mejorar eficiencia espectral.
- **Target Wake Time (TWT)** para ahorro de energía.
- Operación en **2.4 GHz y 5 GHz**.

Beneficios:

- Mejor rendimiento en **entornos con alta densidad de dispositivos**.
- Mayor eficiencia energética.
- Ideal para:
  - estadios
  - centros comerciales
  - oficinas con muchos dispositivos.

---

# 4. Comparación general de estándares

| Estándar | Frecuencia | Velocidad máxima | Ancho de banda |
|---------|-----------|-----------------|---------------|
| 802.11b | 2.4 GHz | 11 Mbps | 20 MHz |
| 802.11g | 2.4 GHz | 54 Mbps | 20 MHz |
| 802.11n | 2.4 / 5 GHz | 600 Mbps | 20 / 40 MHz |
| 802.11ac | 5 GHz | 6.93 Gbps | 20 / 40 / 80 / 160 MHz |
| 802.11ax | 2.4 / 5 GHz | 9.6 Gbps | 20 / 40 / 80 / 160 MHz |

Evolución principal:
- aumento de **velocidad**
- mayor **ancho de banda**
- mejor **eficiencia espectral**.

---

# 5. Frecuencias de funcionamiento

## Banda 2.4 GHz
Características:

- Mayor **alcance**.
- Mejor penetración de obstáculos.
- Más susceptible a **interferencias**.

Utilizada por:
- 802.11b
- 802.11g
- 802.11n
- 802.11ax

---

## Banda 5 GHz
Características:

- **Menor congestión**.
- **Mayores velocidades**.
- Menor alcance.

Utilizada por:

- 802.11a
- 802.11n
- 802.11ac
- 802.11ax

Muchos routers modernos:
- **dual-band (2.4 GHz y 5 GHz)**.

---

# 6. Seguridad en Wi-Fi

## WEP (1999)
- Primer protocolo de seguridad.
- Presentaba **vulnerabilidades importantes**.

## WPA (2003)
- Solución temporal a las debilidades de WEP.
- Mejoras en **autenticación y cifrado**.

## WPA2 (2004)
- Introduce **AES**.
- Se convierte en el estándar durante muchos años.

## WPA3 (2018)
- Mayor protección contra **ataques de fuerza bruta**.
- Mejor privacidad en **redes abiertas**.

---

# 7. Aplicaciones de IEEE 802.11

### Hogares inteligentes
- IoT
- streaming
- automatización del hogar.

### Empresas
- redes corporativas
- videoconferencias
- acceso a la nube.

### Espacios públicos
- hotspots en:
  - aeropuertos
  - cafeterías
  - centros comerciales.

### Industria
- monitoreo de equipos
- automatización industrial
- logística en tiempo real.

---

# 8. Ventajas de los estándares IEEE 802.11

### Interoperabilidad
- Dispositivos de diferentes fabricantes pueden comunicarse.

### Escalabilidad
- Redes pueden crecer desde:
  - pequeñas oficinas
  - grandes campus.

### Innovación
- Impulsa desarrollo de nuevas tecnologías inalámbricas.

### Reducción de costos
- Estandarización permite **economías de escala**.

---

# 9. Desafíos y limitaciones

Principales problemas:

- **Seguridad**
- **Congestión del espectro**
- **Consumo energético**
- **Alcance limitado**
- **Adopción lenta de nuevos estándares**

Factores que afectan el rendimiento:

- obstáculos físicos
- densidad de usuarios
- interferencias.

---

# 10. Tendencias futuras

## Wi-Fi 6E y Wi-Fi 7
- Uso de la **banda de 6 GHz**.
- Wi-Fi 7 promete **hasta 30 Gbps**.

## Ondas milimétricas
- Frecuencias superiores a **60 GHz**.
- Aplicaciones de **muy alta velocidad y corto alcance**.

## Integración con 5G y 6G
- Conectividad más integrada entre redes Wi-Fi y celulares.

## Inteligencia Artificial
- Optimización automática de:
  - rendimiento
  - seguridad
  - gestión del espectro.

---

# 11. Impacto global del Wi-Fi

- Aproximadamente **3.5 mil millones de usuarios** de Wi-Fi.
- Cerca del **50% del tráfico móvil** se descarga a redes Wi-Fi.
- Aproximadamente **16 millones de hotspots públicos**.

Impacto:
- democratización del acceso a Internet
- crecimiento de dispositivos móviles
- nuevos modelos de negocio digitales.

---

# 12. Integración con otras tecnologías

### Wi-Fi y Bluetooth
- Bluetooth → corto alcance, bajo consumo.
- Wi-Fi → mayor velocidad y cobertura.

### Wi-Fi y redes celulares
- Integración con **4G y 5G**.
- Tecnologías como **LTE-U y LAA**.

### Wi-Fi e IoT
- Adaptaciones como **Wi-Fi HaLow (802.11ah)**.
- Integración con:
  - Zigbee
  - Z-Wave.

---

# 13. Consideraciones para implementación

### Planificación de red
- análisis del entorno
- mapeo de cobertura
- selección de equipos.

### Seguridad
- uso de protocolos modernos
- segmentación de red
- control de acceso.

### Escalabilidad
- diseño preparado para **crecimiento futuro**.

---

# 14. IEEE 802.11 en el contexto de IoT y 5G

## Wi-Fi 6 e IoT
- Mejor manejo de **muchos dispositivos simultáneos**.

## Complementariedad con 5G
- Wi-Fi → interiores.
- 5G → exteriores y movilidad.

## Edge Computing
- Procesamiento de datos cerca del origen.
- Importante para aplicaciones IoT en tiempo real.
"""

output_path = "/mnt/data/resumen_estandares_wifi.md"

pypandoc.convert_text(md_content, 'md', format='md', outputfile=output_path, extra_args=['--standalone'])

output_path