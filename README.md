# Arcis 
Simulates projectiles motion

## Math
Position:
```math
\begin{aligned}
p&=\begin{bmatrix} x \\ y \\ z \end{bmatrix} \\
p_x=x \\
p_y=y \\
p_z=z
\end{aligned}
```

Velocity:
```math
\begin{aligned}
v&=\frac{dp}{dt} \\
v_x&=\frac{dx}{dt} \\
v_xdt&=dx \\
v_xdt&=x_f-x_i \\
v_xdt+x_i&=x_f \\
x_f=v_xdt+x_i \\
y_f=v_ydt+y_i \\
z_f=v_zdt+z_i
\end{aligned}
```

Acceleration:
```math
\begin{aligned}
a&=\frac{dv}{dt} \\
a_x&=\frac{dv_x}{dt} \\
a_xdt&=dv_x \\
a_xdt&={v_x}_f-{v_x}_i \\
a_xdt+{v_x}_i&={v_x}_f \\
{v_x}_f=a_xdt+{v_x}_i \\
{v_y}_f=a_ydt+{v_y}_i \\
{v_z}_f=a_zdt+{v_z}_i
\end{aligned}
```

Newton's Second Law of Motion:
```math
F_{\text{net}}=ma
```

Assumption: Acceleration Due to Gravity Only
```math
\begin{aligned}
a_x&=0 \\
a_y&=0 \\
a_z&=-g
\end{aligned}
```

Acceleration:
```math
\begin{aligned}
{v_x}_f&=0dt+{v_x}_i \\
{v_x}_f&={v_x}_i \\
{v_y}_f&=0dt+{v_y}_i \\
{v_y}_f&={v_y}_i \\
{v_z}_f&=-gdt+{v_z}_i \\
\end{aligned}
```

## Contributions
This repository is maintained by @jonahfrancisbenedicto
1. **Fork** the Project
2. **Create** your Feature Branch (`git checkout -b feature/custom-feature`)
3. **Commit** your Changes (`git commit -m 'Add custom feature'`)
4. **Push** to the Branch (`git push origin feature/custom-feature`)
5. **Open** a Pull Request

## License
This repository is licensed under the [MIT License](./LICENSE).
