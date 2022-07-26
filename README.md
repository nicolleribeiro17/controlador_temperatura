Implementação de um sistema fuzzy para a realização de um controle de temperatura e de tempo de ciclo de uma máquina de lavar.

Entradas:
O grau da sujeira presente na roupa (cloth_dirtiness), a massa da roupa (cloth_mass), a sensibilidade da roupa na resistencia a temperatura (cloth_sensitivity).

Saídas:
O tempo de lavagem necessário (time_process), e a temperatura da água (temperatura).

Membership functions:
![image](https://user-images.githubusercontent.com/50892395/180896152-e8f39fd2-5566-42a0-965d-649d110a7da4.png)
![image](https://user-images.githubusercontent.com/50892395/180896176-2341407d-b167-4a1c-b2c0-c9f104aa53ee.png)
![image](https://user-images.githubusercontent.com/50892395/180896190-a3c94756-f41d-4f7f-a068-f0a7364e1e2d.png)
![image](https://user-images.githubusercontent.com/50892395/180896223-0fd24ef9-86bd-48dc-b585-581ed6f66d98.png)
![image](https://user-images.githubusercontent.com/50892395/180896259-e9bcaeb1-4731-4b66-8c14-356aef4b8701.png)

Este sistema utilizou 12 regras no motor de inferência para determinar a saída agregada.
