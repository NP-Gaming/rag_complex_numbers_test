# 01003 Mathematics 1a - Complex Numbers Course Notes

## 1: Number Sets, Fields, and Axioms
### Number Sets
- $\mathbb{N} = \{1, 2, 3, \dots\}$ *(Note: $0$ is NOT included in $\mathbb{N}$ in Mathematics 1a course!)*
- $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$
- $\mathbb{Q} = \{\frac{a}{b} \mid a, b \in \mathbb{Z}, b \neq 0\}$
- $\mathbb{R} = \{\text{ordered complete field}\}$ *(Ordered: can define $<, >$ (smaller and greater); Complete: no holes in the set)*
- $\mathbb{C} = \{a + b \cdot i \mid a, b \in \mathbb{R}\}$

### Basic & Field Axioms
A **Field** is a set for which addition and multiplication are defined (and stable, meaning the operation never leaves the set) such that all field axioms are fulfilled:
- **Basic Axioms**: 
  - Reflexive ($a=a$), Symmetric ($a=b \Leftrightarrow b=a$)
  - Transitive ($a=b \land b=c \Rightarrow a=c$)
  - Additive ($a=b \land c=d \Rightarrow a+c=b+d$)
  - Multiplicative ($a=b \land c=d \Rightarrow a \cdot c = b \cdot d$).
- **Commutative**: $a + b = b + a$ and $a \cdot b = b \cdot a$
- **Associative**: $(a + b) + c = a + (b + c)$ and $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
- **Distributive**: $a \cdot (b + c) = a \cdot b + a \cdot c$
- **Neutral/Identities**: $a + 0 = a$ and $a \cdot 1 = a$
- **Inverses**: Additive inverse (opposite) $a + (-a) = 0$; Multiplicative inverse (reciprocal) $a \cdot \frac{1}{a} = 1$.



## 2: Definition of Complex Numbers and Basic Operations
### The Imaginary Unit $i$
- Defined strictly as $i^2 = -1$.
- **!!!**: Do NOT write $i = \sqrt{-1}$. As writing $\sqrt{-1}$ leads to the false derivation $-1 = i^2 = \sqrt{-1}\cdot\sqrt{-1} = \sqrt{(-1)(-1)} = \sqrt{1} = 1$.

### Real and Imaginary Parts
For $z = a + bi \in \mathbb{C}$ where $a, b \in \mathbb{R}$:
- **Real part**: $\text{Re}(z) = a$
- **Imaginary part**: $\text{Im}(z) = b$. 
  - **Crucial**: The imaginary part $\text{Im}(z)$ is a REAL number ($\text{Im}(4+3i) = 3$).
- If $b = 0$, the number is real ($3 \in \mathbb{R}$, which is also in $\mathbb{C}$).
- If $a = 0$, the number is purely imaginary (e.g., $4i \in \mathbb{C}$).

### Addition and Multiplication
- **Addition**: $z_1 + z_2 = (a_1 + b_1i) + (a_2 + b_2i) = (a_1 + a_2) + (b_1 + b_2)i$
- **Multiplication**: $z_1 \cdot z_2 = (a_1 + b_1i)(a_2 + b_2i) = (a_1a_2 - b_1b_2) + (a_1b_2 + a_2b_1)i$



## 3: Complex Conjugate and Division (Multiplicative Inverse)
### Complex Conjugate
The complex conjugate of $z = a + bi$ is $\bar{z} = a - bi$.
- Key property: $z \cdot \bar{z} = (a + bi)(a - bi) = a^2 + b^2$ (a real number).
- **Conjugation Rules**:
  - $\bar{\bar{z}} = z$
  - $\overline{z_1 + z_2} = \bar{z_1} + \bar{z_2}$
  - $\overline{z_1 \cdot z_2} = \bar{z_1} \cdot \bar{z_2}$
  - $\overline{(1/z)} = 1/\bar{z}$ and $\overline{z^n} = (\bar{z})^n$ for $n \in \mathbb{Z}$
  - If $z \in \mathbb{R}$, then $\bar{z} = z$
  - $\overline{e^z} = e^{\bar{z}}$ and $\overline{e^{i\alpha}} = e^{-i\alpha}$
  - $\bar{z} = |z| \cdot e^{-i \cdot \text{arg}(z)}$

### Complex divison
$$\frac{z_1}{z_2} = \frac{z_1}{z_2} \frac{\overline{z_2}}{\overline{z_2}}$$
#### Division Example
To divide complex numbers, multiply numerator and denominator by the conjugate of the denominator:
$$\frac{3+4i}{1+2i} = \frac{3+4i}{1+2i} \cdot \frac{1-2i}{1-2i} = \frac{3 - 6i + 4i - 8i^2}{1^2 + 2^2} = \frac{11 - 2i}{5} = \frac{11}{5} - \frac{2}{5}i$$



## 4: Forms of Complex Numbers, Modulus, and Argument
### Forms and Coordinates
- **Rectangular form**: $z = a + bi$ with rectangular coordinates $(a, b)$.
- **Polar / Exponential form**: $z = r \cdot (\cos(\theta) + i \cdot \sin(\theta)) = r \cdot e^{i\theta}$ with polar coordinates $(r, \theta)$.
  - $\cos(\theta) + i \cdot \sin(\theta)$ can also be abbreviated to: $\text{cis}(\theta)$

### Modulus ($r$ or $|z|$)
By the Pythagorean theorem, distance from the origin is $|z| = r = \sqrt{a^2 + b^2} = \sqrt{\text{Re}(z)^2 + \text{Im}(z)^2}$.
- Example: $|3 + i| = \sqrt{3^2 + 1^2} = \sqrt{10}$.
- Geometric interpretation: $|z_1 - z_2|$ is the distance between $z_1$ and $z_2$ (difference vector).
  - Example 1: $|z + 1 + i| = |z - (-1 - i)| = 1$ describes a circle of radius $1$ centered at $(-1, -1)$.
  - Example 2: To solve $|z - 2 + 2i| = |z - 4|$: substitute $z = a + bi$, giving $|(a-2) + (b+2)i| = |(a-4) + bi|$. Squaring both sides: $(a-2)^2 + (b+2)^2 = (a-4)^2 + b^2 \Rightarrow a^2 - 4a + 4 + b^2 + 4b + 4 = a^2 - 8a + 16 + b^2 \Rightarrow 4b = -4a + 8 \Rightarrow b = -a + 2$ (line $y = -x + 2$ in the complex plane; real solution where $b=0$ is $a=2$, or intercept depending on sign).

### Argument ($\text{arg}(z)$) and Principal Argument ($\text{Arg}(z)$)
- Trigonometric relations: $\cos(\theta) = \frac{a}{r}$ and $\sin(\theta) = \frac{b}{r}$.
- **Principal Argument** (written with a CAPITAL A, $\text{Arg}(z)$): The unique angle in the interval $]-\pi; \pi]$ (or $[-\pi; \pi]$).
  - If an angle is $\theta > \pi$, subtract $2\pi$. If $\theta < -\pi$, add $2\pi$.
- **All arguments**: $\text{arg}(z) = \text{Arg}(z) + 2k\pi, \quad k \in \mathbb{Z}$.
- **Example**: Find polar coordinates of $z = 4 - 4i$.

  0. $z = 4 - 4i$.
  1. $a = 4, b = -4$.
  2. $r = \sqrt{4^2 + (-4)^2} = \sqrt{32} = 4\sqrt{2}$.
  3. $\cos(\theta) = \frac{4}{4\sqrt{2}} = \frac{1}{\sqrt{2}} \Rightarrow \theta = \pm \frac{\pi}{4}$ within $[-\pi, \pi]$.
  4. Since $b = -4 < 0$ ($\sin(\theta) < 0$), the angle is in the 4th quadrant: $\text{Arg}(z) = -\frac{\pi}{4}$.
  5. All arguments: $\theta = -\frac{\pi}{4} + 2k\pi, \quad k \in \mathbb{Z}$.



## 5: Euler's Formula and Complex Exponential Equations
### Euler's Formula
- $e^{i\theta} = \cos(\theta) + i\sin(\theta)$ (sometimes abbreviated $\text{cis}(\theta)$).
- For general $z = a + bi$: $e^z = e^{a+bi} = e^a(\cos(b) + i\sin(b))$.
- Here, modulus is $|e^z| = e^a$ and argument is $\text{arg}(e^z) = b + 2k\pi$.
- Note on range: For real $x$, $\exp: \mathbb{R} \mapsto \mathbb{R}_{>0}$. For complex $z$, $\exp: \mathbb{C} \mapsto \mathbb{C} \setminus \{0\}$.
- Multiplication in polar form is much easier: 
  - for: $z_1 = 4-4i = \sqrt{32}e^{-i\frac{\pi}{4}}$ 
  - and: $z_2 = 1+i = \sqrt{2}e^{i\frac{\pi}{4}}$
  - $z_1 \cdot z_2 = \sqrt{64}e^{i(-\frac{\pi}{4}+\frac{\pi}{4})} = 8e^0 = 8$.

### Complex Exponential Equations (Identity Theorem)
- In Mathematics 1a, we do NOT use complex logarithms or complex roots like $\ln(i)$, $\sqrt{i}$, or $\cos(i)$.
- Instead, we solve $e^z = w$ using the **Identity Theorem**: Two equal complex numbers must have the exact same modulus and the same argument (* $\theta = 2k\pi, k \in \mathbb{N}$).
- **Steps to solve $e^z = w$**:
  1. Write $z = a + bi$ so $e^a e^{ib} = w$.
  2. **Same Modulus**: $|e^a e^{ib}| = |w| \Rightarrow e^a = |w| \Rightarrow a = \ln(|w|)$ (standard real logarithm!).
  3. **Same Argument**: $\text{arg}(e^a e^{ib}) = \text{arg}(w) \Rightarrow b = \text{Arg}(w) + 2p\pi, \quad p \in \mathbb{Z}$.
  4. Combine into $z = a + bi$.
- **Example 1**: Solve $e^z = 1 + i$.
  - Set $z = a + bi \Rightarrow e^a e^{ib} = 1 + i$.
  - Same mod: $e^a = |1 + i| = \sqrt{2} \Rightarrow a = \ln(\sqrt{2})$.
  - Same arg: $b = \text{arg}(1 + i) = \frac{\pi}{4} + 2p\pi, \quad p \in \mathbb{Z}$.
  - Solution: $z = \ln(\sqrt{2}) + i\left(\frac{\pi}{4} + 2p\pi\right), \quad p \in \mathbb{Z}$.
- **Example 2**: Solve $e^z = -1$.
  - No real solution since $e^x > 0$ for all $x \in \mathbb{R}$.
  - For $z = a + bi$: Mod gives $e^a = |-1| = 1 \Rightarrow a = \ln(1) = 0$.
  - Arg gives $b = \text{arg}(-1) = \pi + 2k\pi, \quad k \in \mathbb{Z}$.
  - Solution: $z = i(2k + 1)\pi, \quad k \in \mathbb{Z}$.