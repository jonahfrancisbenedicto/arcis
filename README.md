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
a&=\frac{dv}{dt} \\
a_x&=\frac{dv_x}{dt} \\
a_xdt&=dv_x \\
a_xdt&=v_x_f-v_x_i \\
a_xdt+v_x_i&=v_x_f \\
v_x_f=a_xdt+v_x_i \\
v_y_f=a_ydt+v_y_i \\
v_z_f=a_zdt+v_z_i
```

Newton's Second Law of Motion:
```math
F=ma
```

Acceleration Due to Gravity
```math
F_z=-mg
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
