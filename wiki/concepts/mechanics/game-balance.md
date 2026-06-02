# Game Balance

El arte y la ciencia de ajustar todos los elementos de un juego hasta que produzcan la experiencia deseada. El balance no es un estado que se alcanza — es un proceso continuo de ajuste iterativo que nunca termina del todo. **Balancear un juego es tan artesanal como cualquier otra parte del diseño**: requiere entender sutiles relaciones entre elementos y saber cuándo cambiarlos y cuánto.

---

## Qué es el balance (s001, s005)

**Sellers (s001, ch.9):** El balance es una propiedad del sistema completo game+player: surge de las relaciones entre las partes del juego — sus atributos, valores y comportamientos. Un juego bien balanceado:
- Evita estrategias dominantes que hagan obsoleto el resto del diseño
- Ofrece un espacio de posibilidades explorable donde múltiples estrategias tienen mérito
- Mantiene al jugador en el canal de flujo — ni demasiado fácil (aburrimiento) ni demasiado difícil (ansiedad)
- Nunca está "perfectamente" balanceado: cualquier jugador puede desequilibrar un juego de nuevas formas. Construye **sistemas resilientes**, no sistemas perfectos.

**Schell (s005, ch.11):** Balancear un juego es "ajustar sus elementos hasta que generen exactamente la experiencia que quieres". Es una analogía culinaria: no solo identificar los ingredientes (el diseño de mecánicas) sino decidir las proporciones correctas y cómo combinarlos. La habilidad más artesanal del diseño.

---

## Los cuatro métodos de balance (s001, ch.9)

Sellers identifica cuatro aproximaciones complementarias:

| Método | Descripción | Cuándo usarlo |
|--------|-------------|---------------|
| **Diseñador** | Intuición y juicio basados en experiencia | Primera aproximación; siempre presente |
| **Jugador** | Observar cómo juegan realmente los jugadores | Playtesting; datos de comportamiento real |
| **Analítico** | Datos y analytics sobre el juego en funcionamiento | Live games; ajustes post-lanzamiento |
| **Matemático** | Probabilidades, modelos, valor esperado | Diseño de economías; sistemas de azar |

Los cuatro se usan en conjunto — ninguno solo es suficiente. El matemático informa al diseñador; el playtesting con jugadores corrige las suposiciones de ambos.

---

## Sistemas transitivos vs. intransitivos (s001, ch.9; s005, ch.11)

### Sistemas transitivos
Relaciones de poder ordenadas: A > B > C > D. Existe una jerarquía clara.

**Problema:** La **estrategia dominante** — una opción que es siempre mejor que todas las demás. Cuando existe, el juego se "resuelve" y pierde profundidad.

> "Once a dominant strategy is discovered, the game is no longer fun, because the puzzle of the game has been solved — there are no more choices to make." (s005, ch.11)

Los exploits son estrategias dominantes ocultas que los jugadores descubren. Cuando se elimina una estrategia dominante, el diseñador novato entra en pánico ("ya no entiendo cómo ganar"), pero en realidad es un logro: el juego acaba de ganar profundidad.

**Balancear sistemas transitivos:** asignar valor numérico a cada atributo y comparar totales entre opciones (el ejemplo del Biplane Battle: velocidad, maniobrabilidad, potencia de fuego). El modelo informa el prototipo; el prototipo informa el modelo en ciclo virtuoso.

### Sistemas intransitivos
Relaciones cíclicas: A vence a B, B vence a C, C vence a A. El ejemplo canónico: **piedra, papel, tijeras**.

**Ventaja:** Ninguna opción es universalmente superior — siempre hay una respuesta a cualquier estrategia. Esto crea depth sin jerarquía de poder.

Aplicaciones en juegos:
- Tríadas de unidades en estrategia (infantería vence caballería, caballería vence arqueros, arqueros vence infantería)
- Tríadas de personajes en brawlers y fighting games
- Tríadas de armas (cuerpo a cuerpo / distancia / area)

La relación intransitiva asegura que ningún jugador puede "resolver" el meta con una sola elección.

---

## Los 12 tipos de balance (Schell, s005, ch.11)

Schell identifica 12 dimensiones distintas de balance que cada diseñador debe examinar. Cada una viene con Lenses específicas.

### Tipo 1: Justicia (Fairness)
*Lens #30*

¿Tienen todos los jugadores una oportunidad justa de ganar?

**Juegos simétricos** — todos los jugadores comienzan con los mismos recursos y capacidades. La única variable que determina el resultado es la habilidad. Problema: el jugador que va primero puede tener ventaja.

**Juegos asimétricos** — los jugadores tienen diferentes fuerzas, recursos u objetivos. Requiere balance activo. Razones legítimas para el asimétrico:
1. Simular situaciones del mundo real (guerra, negociación)
2. Dar a los jugadores formas distintas de explorar el espacio del juego
3. Personalización según las fortalezas del jugador
4. Nivelar el campo entre jugadores de distinto nivel (hándicap)
5. Crear situaciones tácticamente interesantes

Un ejemplo brillante de asimetría aceptada: *Alien vs. Predator* — los Predators tienen ventaja mecánica, pero los jugadores lo aceptan porque es coherente con la ficción del universo y "vencer siendo Alien" se convierte en un logro de orgullo.

**Herramienta:** asigna valor numérico a cada atributo, suma por opción, ajusta hasta que los totales sean equivalentes. Luego valida con playtesting: la teoría informa el modelo, el juego informa la teoría.

---

### Tipo 2: Reto vs. Éxito (Challenge vs. Success)
*Lens #31*

El canal de flujo aplicado al diseño de dificultad. El reto debe crecer con la habilidad para mantener al jugador en la zona de engagement.

**Técnicas:**
- **Aumentar dificultad con cada éxito** — cada nivel es más difícil que el anterior; el jugador construye habilidad hasta superar el nivel actual y se enfrenta a uno que le desafía de nuevo
- **Dejar a los jugadores hábiles pasar las partes fáciles rápido** — los jugadores avanzados llegan antes a su nivel de desafío; no se aburren en contenido trivial
- **Capas de desafío** — calificaciones por nivel (C para continuar, A para orgullo, S+ para los completistas); distintos jugadores encuentran su propio umbral de satisfacción
- **Elección de dificultad** — Easy/Normal/Hard; el riesgo es fragmentar la percepción del juego "real"
- **Testear con mezcla de habilidades** — nunca solo con el equipo de desarrollo ni solo con novatos

> "Just learning to play a game at all is a challenge. The first level or two should be very simplistic — the player is already challenged trying to understand the controls and goals." (s005, ch.11)

---

### Tipo 3: Elecciones significativas
*Lenses #32–33*

**Elecciones significativas (s005, ch.11 y Mateas):**

*Choices = Desires* → El jugador siente libertad y plenitud
*Choices > Desires* → El jugador se siente abrumado
*Choices < Desires* → El jugador se siente frustrado

No es solo el número de elecciones sino su relevancia. 50 vehículos que se controlan igual = 0 elecciones reales. 2 armas genuinamente distintas = 2 elecciones reales.

**Triangularidad** — la elección más emocionante: una opción segura con baja recompensa vs. una opción arriesgada con alta recompensa. Cuando está bien balanceada, ninguna es trivialmente mejor; el jugador debe evaluar su situación cada vez.

> "About eight out of ten times someone comes to me asking for help on a game prototype that 'just isn't fun,' the game is missing this kind of meaningful choice." (Schell, s005, ch.11)

*Space Invaders* como ejemplo perfecto de triangularidad: los aliens normales son seguros y dan pocos puntos. El platillo volante es peligroso (requiere quitar los ojos del campo de batalla, arriesgando ser bombardeado) pero da 100–300 puntos. La elección ¿juego seguro o voy a por el platillo? ocurre varias veces por partida.

Balance con valor esperado (Lens #28): el valor esperado del camino arriesgado debe ser comparable al del seguro para que la elección sea genuina. Ejemplo del juego *Qix*: el rectángulo rápido (baja precisión requerida, pocos puntos) vs. el lento (alta precisión, el doble de puntos). Las probabilidades de éxito se calibran matemáticamente para que el valor esperado de ambos sea igual.

---

### Tipo 4: Habilidad vs. Azar (Skill vs. Chance)
*Lens #34*

Dos fuerzas opuestas. Más azar → el juego se vuelve más relajado, accidental, menos "justo" como medida de habilidad. Más habilidad → el juego se vuelve más serio, más competitivo, más medidor de excelencia.

**Patrón de alternancia:** repartir una mano de cartas es azar puro; jugarlas es habilidad pura. Tirar el dado es azar; decidir dónde mover la pieza es habilidad. Esta alternancia crea tensión y relajación que muchos jugadores encuentran muy placentera.

La preferencia varía por audiencia, edad, cultura (ej.: los juegos de mesa alemanes tienden a minimizar el azar más que los americanos). El diseñador debe conocer su audiencia.

---

### Tipo 5: Cabeza vs. Manos (Head vs. Hands)
*Lens #35*

¿Cuánto requiere el juego de actividad física (reflejos, destreza, velocidad) vs. pensamiento (estrategia, planificación, resolución de puzzles)?

Ambas pueden coexistir (y en los mejores juegos de acción-plataforma, simultáneamente: el boss requiere entender el patrón Y ejecutarlo con destreza). El problema es la comunicación: el juego debe dejar claro qué tipo de desafío ofrece. *Pac-Man 2* falló porque la caja sugería un juego de acción y era un juego de puzzles psicológicos — mismatch que traicionó expectativas de ambos tipos de jugadores.

---

### Tipo 6: Competición vs. Cooperación
*Lenses #36–38*

Dos impulsos animales básicos — competir para establecer estatus y cooperar para potenciar capacidades colectivas. Los juegos son un espacio psicológicamente seguro para explorar ambos.

Opciones de diseño:
- Puramente competitivo (ajedrez, fighting games)
- Puramente cooperativo (Lord of the Rings board game, Pandemic)
- Mixto: *Joust* — dos jugadores compiten por puntos pero pueden coordinarse para sobrevivir más tiempo y puntuaciones absolutas más altas. Las rondas "Team Wave" incentivan cooperación; las "Gladiator Wave" incentivan traición. Esta tensión dinámica entre ambos es lo más interesante del diseño mixto.
- Competición en equipo: combina ambos (cooperas con tu equipo, compites contra el rival)

---

### Tipo 7: Corto vs. Largo (Short vs. Long)
*Lens #39*

La duración determina cuánta estrategia se puede desarrollar, qué tipo de arco dramático es posible, y a qué audiencia sirves.

Herramientas para controlar la duración:
- **Condiciones de victoria y derrota** — el único factor que realmente termina el juego; cambiarlas puede doblar o reducir a la mitad la duración
- **Tiempo de seguridad inicial** (*Spy Hunter*): los primeros 90 segundos son invulnerables — los novatos tienen tiempo de aprender antes de que las muertes importen
- **Deadline elegante** (*Minotaur*): a los 20 minutos suena una campana y todos los jugadores supervivientes son teletransportados a una sala pequeña llena de monstruos ("Armageddon"). Garantiza que el juego siempre termina en menos de 25 minutos, con drama final garantizado.

> "Often it makes sense to follow the old vaudevillian adage: 'Leave them wanting more.'" (s005, ch.11)

---

### Tipo 8: Recompensas (Rewards)
*Lens #40*

Los juegos dan feedback positivo al jugador diciéndole que ha hecho bien. Schell identifica **8 tipos**:

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Elogio** | El juego dice que lo hiciste bien — audio, animación, mensaje | Nintendo's signature jingles |
| **Puntos** | Medida cuantificable de éxito; valen más si son visibles por otros | Leaderboards |
| **Juego prolongado** | Tiempo o vidas adicionales — el deseo de supervivencia | Extra life en pinball |
| **Portal** | Acceso a nuevo contenido — satisface el deseo de explorar | Nuevo nivel, puerta desbloqueada |
| **Espectáculo** | Música, animación especial — raramente satisface solo; funciona combinado | Pac-Man intermission |
| **Expresión** | Capacidad de personalizar — ropa, decoración, marcas propias | Skins, custom characters |
| **Poderes** | Capacidades nuevas o mejoradas — el jugador se vuelve más poderoso | Kineado en damas, mushroom en Mario |
| **Recursos** | Objetos de valor en el mundo del juego | Munición, HP, dinero virtual |
| **Completitud** | El cierre de haberlo completado todo — el último umbral | 100%, créditos finales |

**Principios de balance de recompensas:**
- La gente se aclimata a las recompensas fijas — las recompensas **variables** mantienen la emoción mucho más tiempo. La misma cantidad de puntos en promedio, pero distribuida aleatoriamente, mantiene la anticipación (Skinner + variable ratio schedule → cf. [[../../player/motivation]])
- Las recompensas deben crecer gradualmente con la progresión — "jumping from level 3 to level 10 rewards" sigue siendo emocionante aunque sepas que el diseñador lo está haciendo deliberadamente

---

### Tipo 9: Castigos (Punishments)
*Lens #41*

Paradójicamente, el castigo bien diseñado **aumenta el disfrute**: crea valor endógeno (lo que puede perderse vale más), hace que el riesgo sea emocionante, y aumenta la sensación de logro al superar el juego.

**6 tipos de castigo:**
1. **Vergüenza** — el juego te dice que lo hiciste mal (animación de derrota, "Missed!", "Defeated!")
2. **Pérdida de puntos** — relativamente raro; los puntos ganados que pueden perderse valen menos (menor valor endógeno)
3. **Juego acortado** — perder una vida, perder tiempo
4. **Juego terminado** — Game Over
5. **Retroceso** — te devuelve al inicio del nivel o último checkpoint; la clave es dónde poner los checkpoints
6. **Recursos agotados** — pérdida de poderes, dinero, objetos. *Toontown Online* case study: el castigo por "morir" (laff meter a cero) era una combinación calibrada de setback leve (1 minuto de caminata), resource depletion (ítems baratos, 10 minutos para recuperarlos), vergüenza (el personaje baja la cabeza), y temporary removal of powers (30 segundos de movimiento lento). Más ligero → las batallas eran aburridas (sin riesgo). Más severo → los jugadores se volvían demasiado cautelosos. El calibrado final producía el riesgo-recompensa correcto.

**Regla de oro:** Convertir castigos en recompensas siempre que sea posible. *Diablo* example: el sistema "comida" original penalizaba no comer (los stats bajaban). Blizzard lo invirtió: comer da un boost temporal de poderes. Los jugadores lo experimentan como positivo en vez de como una carga.

> "It is crucial that all punishment in a game is for things that the player is able to understand and prevent. When punishment feels random and unstoppable, the player will quickly label the game 'unfair.'" (s005, ch.11)

---

### Tipo 10: Libertad vs. Experiencia controlada
*Lens #71 (Freedom)*

¿Cuánto control das al jugador? La paradoja: dar control total no solo cuesta más desarrollo, puede resultar aburrido para el jugador (más interesante que la vida real ≠ simulación completa de la vida real).

Ejemplo: en *Aladdin's Magic Carpet VR*, la escena final con Jafar requería control de cámara preciso. Los diseñadores le quitaron libertad al jugador para garantizar la experiencia dramatica óptima. Ningún playtester lo notó — porque todos querían hacer exactamente lo que el juego les estaba dirigiendo a hacer. Moraleja: **la libertad que los jugadores quieren aprovechar y la libertad que no notan que falta son equivalentes en cuanto a satisfacción**.

---

### Tipo 11: Simple vs. Complejo
*Lenses #42–43*

Schell distingue dos tipos de complejidad:

**Complejidad innata** — el conjunto de reglas en sí mismo es complejo. Surge cuando intentas simular situaciones del mundo real o cuando añades reglas especiales para balancear el juego. Keywords: "unless", "except", "but if". El ejemplo del peón en ajedrez tiene complejidad innata (movimiento/captura distintos, primer movimiento especial, en passant) que genera complejidad emergente muchísimo mayor.

**Complejidad emergente** — un conjunto de reglas simple produce situaciones complejas. El Go es el ejemplo canónico: reglas trivialmente simples, profundidad estratégica casi ilimitada. *Space Invaders*: una sola regla (cuanto menos aliens quedan, más rápido van) genera dos propiedades muy deseables que emergen naturalmente (el juego se acelera al acercarse al final; es más difícil cuando ya eres bueno).

El ideal: **elegancia** — sistemas simples que funcionan robustamente en situaciones complejas. Medida operacional: **cuántos propósitos sirve cada elemento**. Los puntos en *Pac-Man* sirven 5 propósitos simultáneos (meta corto plazo, meta largo plazo, triangularidad [las bocadas te ralentizan], medida de éxito, vidas extra). Eso es elegancia.

**Carácter vs. Elegancia:** son opuestos necesarios. La elegancia pura produce algo perfecto pero sin personalidad. Los tokens de Monopoly (un sombrero, un zapato, un perro) no tienen NADA que ver con bienes raíces — pero son parte de la identidad del juego. Los "defectos" que los jugadores adoran son el carácter.

---

### Tipo 12: Detalle vs. Imaginación
*Lens #45 (Imagination)*

¿Qué detallas explícitamente y qué dejas a la imaginación del jugador? Los jugadores tienen imaginaciones ricas — la imaginación de los jugadores a menudo es mejor que lo que el diseñador puede producir con presupuesto limitado. Principios:
- Solo detalla lo que puedes hacer bien
- Da detalles que den pie a la imaginación
- Los mundos familiares necesitan poco detalle (el jugador rellena con memoria)
- El "efecto binoculares" — un primer plano inicial construye la imagen mental; el resto del juego la imaginación la sostiene

---

## Metodología de balance (s005, ch.11)

### Doblar y partir (Doubling and halving)
El método más eficiente para encontrar el rango de balance:

> "You never know what is enough unless you know what is more than enough." — William Blake

Cuando cambias un valor para balancear el juego, **no lo cambies en pequeños incrementos** (de 100 a 90 daño). **Dóblalo o pártelo por la mitad** (de 100 a 50). Esto revela los extremos del espacio de diseño rápidamente; luego vas refinando hacia el centro. Cambios pequeños solo hacen perder tiempo cuando el rango correcto puede estar lejos del valor inicial.

### Usa el modelo matemático
Construye un modelo del balance antes de playtestear. El modelo informa el prototipo; el prototipo informa el modelo. Este ciclo virtuoso produce balance más rápido que solo playtesting sin modelo.

### Problema antes de solución
Enunciar el problema claramente antes de proponer soluciones. Muchos diseñadores saltan a soluciones de balance antes de entender el problema real, creando desbalances en cascada.

### Playtesting con mezcla de habilidades
El equipo de desarrollo está demasiado expuesto. Los novatos pasan demasiado al otro lado. La mezcla es lo que revela la curva de dificultad real.

---

## Sistemas transitivos: curvas de coste/beneficio (s001, ch.9–10)

**Sellers:** El principio fundamental de los sistemas transitivos: **todo beneficio tiene un coste, y los dos están inextricablemente vinculados**. La *demora* en poder pagar costes más altos es lo que pace el juego mientras el jugador siente que mejora.

**Curvas de progresión:** Regulan la progresión vinculada coste/beneficio para jugadores y objetos (armas, niveles de XP). La curva determina cuándo el jugador puede acceder a mayor poder — demasiado rápida y el juego se trivializa; demasiado lenta y se frustra.

**Balance analítico:** En sistemas complejos, los datos de comportamiento real de jugadores revelan desequilibrios que el modelo matemático no predijo. En live games, el balance analítico es el principal motor de ajuste post-lanzamiento.

---

## MDA: el balance como dinámica emergente (s011)

El balance no se diseña en el nivel de las mecánicas — se experimenta en el nivel de las dinámicas. El Monopoly case study de MDA ilustra esto: la mecánica (los ricos ganan más propiedades) produce una dinámica de feedback positivo desbocado (el rico se vuelve más rico sin freno) que produce la estética opuesta a la deseada (la tensión competitiva colapsa; el juego se vuelve aburrido antes del final).

La solución MDA: identificar el feedback loop problemático en la capa de Dynamics (no en la de Mechanics), y diseñar mecánicas que introduzcan un feedback balanceador. → [[../../theory/mda-framework]], [[game-loops]]

---

## Key concepts & cross-links

- [[core-mechanics]] — las mecánicas que se balancean
- [[game-loops]] — los loops de feedback son el motor del balance sistémico
- [[progression-systems]] — las curvas de poder son el balance de la progresión
- [[emergence]] — el balance emergente vs. el balance innato
- [[../../theory/systems-thinking]] — sistemas transitivos/intransitivos; reinforcing/balancing loops
- [[../../theory/mda-framework]] — el balance como propiedad de la capa dinámica
- [[../../player/flow-channel]] — el canal de flujo como target del balance de dificultad
- [[../../player/motivation]] — reward schedules y variable ratio reinforcement
- [[../../design-reference/mechanics]] — Lenses #30–47 (todas las lenses de balance)

## Sources

s005 ch.11 (Schell — 12 tipos de balance; elegancia/carácter; metodología: doblar/partir; asimétrico/simétrico; triangularidad; Space Invaders, Pac-Man, Qix, Toontown, Minotaur case studies) · s001 ch.9–10 (Sellers — métodos de balance; transitive/intransitive; power curves; analytical balance) · s011 (MDA — Monopoly feedback loop como caso de balance fallido; dinámica como target del balance)
