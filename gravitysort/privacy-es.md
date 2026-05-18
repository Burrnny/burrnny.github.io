# Política de Privacidad — Gravity Sort

**Última actualización:** 6 de mayo de 2026

> 🇲🇽 **Español (canónica)** · 🇺🇸 [English](en/) · 🇵🇹 [Português](pt/) · 🇫🇷 [Français](fr/) · 🇩🇪 [Deutsch](de/) · 🇯🇵 [日本語](ja/)

Gracias por jugar Gravity Sort ("la app", "el juego"). Esta política describe qué datos recogemos y cómo los usamos.

## 1. Datos que recogemos

### 1.1 Datos del juego (locales)
- Progreso de niveles, estrellas, monedas, racha, achievements desbloqueados
- Configuraciones (sonido, vibración, modo daltonismo, idioma, notificaciones)
- Skins desbloqueados / aplicados
- Compras In-App activas (Coin Doubler, Pack de rescate, etc.)

Estos datos se almacenan **en tu dispositivo** mediante UserDefaults y, opcionalmente, se sincronizan a tu cuenta de iCloud personal (NSUbiquitousKeyValueStore + CloudKit privado). **Nosotros nunca vemos estos datos** — están en tu Apple ID.

### 1.2 Datos para anuncios (Google AdMob)
Si das tu consentimiento mediante el prompt de App Tracking Transparency (ATT) de Apple, podríamos compartir tu **Identifier for Advertisers (IDFA)** con Google AdMob para ads personalizados. Sin consentimiento, los ads serán contextuales (no personalizados).

AdMob también puede recoger:
- IP address aproximada (para fraud prevention)
- Eventos de interacción con ads (impressions, clicks, completions)
- Datos de diagnóstico de la app (crashes relacionados con ads)

Ver política completa de Google: https://policies.google.com/technologies/partner-sites

Si publicamos en EU/UK/Suiza, mostramos un formulario de consentimiento GDPR (Google UMP) antes del prompt ATT. Puedes cambiar tu consentimiento en cualquier momento desde **Ajustes → Opciones de privacidad**.

### 1.3 Compras In-App (StoreKit)
Las compras se procesan a través de Apple App Store. Recibimos solo confirmación de compra (transaction receipt); no vemos tus datos de pago. Para reembolsos: reportaproblem.apple.com

### 1.4 Diagnóstico de rendimiento
Usamos MetricKit nativo de Apple para detectar crashes y problemas de rendimiento. Los datos se almacenan localmente y NO se envían a ningún servidor de terceros.

## 2. Datos que NO recogemos
- Email, nombre, teléfono
- Ubicación (geolocalización precisa o aproximada manual)
- Lista de contactos
- Acceso a fotos / cámara / micrófono
- Cualquier dato personal directamente identificable

## 3. Cuentas y eliminación de datos
Gravity Sort **no requiere cuenta de usuario**. Todos los datos están en tu dispositivo o en tu iCloud personal.

Para eliminar todos los datos:
1. Elimina la app de tu dispositivo (limpia UserDefaults locales)
2. **iOS Settings → [Tu nombre] → iCloud → Manage Storage → Gravity Sort → Delete Data** (limpia iCloud)
3. Si compraste IAP, los entitlements quedan en tu Apple ID — puedes restaurarlos en cualquier reinstalación

## 4. Servicios de terceros
- **Google AdMob** (anuncios) — [Política](https://policies.google.com/privacy)
- **Google UMP** (consentimiento GDPR para EU) — incluido en Google Mobile Ads SDK
- **Apple iCloud** (sincronización opcional) — [Política Apple](https://www.apple.com/legal/privacy/)
- **Apple StoreKit** (compras) — [Política Apple](https://www.apple.com/legal/privacy/)

## 5. Niños
Esta app es apta para todas las edades (4+). Cumplimos con COPPA, GDPR-K y otras regulaciones aplicables. No recogemos datos personales de menores intencionalmente. AdMob filtra ads a contenido apto para menores cuando detecta dispositivo de menor.

## 6. Tus derechos

### Usuarios EU/UK/Suiza (GDPR)
- Derecho de acceso, rectificación, supresión, portabilidad, oposición
- Para ejercerlos: contáctanos al email abajo
- Autoridad supervisora: tu DPA local

### Usuarios México (LFPDPPP)
- Derechos ARCO+P (Acceso, Rectificación, Cancelación, Oposición, Portabilidad)
- Solicítalos al email abajo
- Autoridad supervisora: INAI

### Usuarios California (CCPA)
- Derecho a saber, eliminar, opt-out de venta. Nosotros NO vendemos tus datos.

## 7. Seguridad
Datos en tu dispositivo: protegidos por iOS sandbox. Datos en tránsito a AdMob: HTTPS. iCloud: encriptado por Apple.

## 8. Retención
Los datos del juego permanecen en tu dispositivo / iCloud hasta que tú los elimines (ver sección 3).

## 9. Cambios
Si cambia esta política, actualizaremos la fecha. Los cambios materiales se notificarán dentro de la app.

## 10. Contacto
Para dudas o ejercer derechos:
**juanmanuelchio12@gmail.com**
**Responsable:** Juan Manuel Cornejo Chio (México)
