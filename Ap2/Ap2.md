## Projeto: O Cão na Ponte de Madeira (Estrutura da Cena)

**Cenário:** Animação 3D de um cachorro atravessando uma ponte de madeira sobre um riacho, com grama e poste de luz, feita no Blender.

### Estrutura da Cena (Hierarquia)

* **Camera:** Objeto de captura da cena.
* **Light:** Fonte de iluminação global (ex: Key Light ou Sun).
* **Plane / Plane.001:** Objetos utilizados para o terreno (Grama / Riacho).
* **Dog Skeleton:** Coleção contendo o *Rig* (esqueleto) do cão.
    * **Dog Skeleton (Objeto):** O *Armature* (esqueleto) para animação.
* **Garden lamp post (Coleção):** Elementos do poste de iluminação.
    * **Garden lamp post (Objeto):** Corpo principal do poste.
    * **Cylinder.002:** Componente da luminária.
    * **Point / Point.001:** Fontes de luz (luzes de ponto) que simulam o brilho da lâmpada.
    * **Sphere:** Globo ou cobertura da luminária.
* **ponte:** Objeto da ponte de madeira (pode conter a geometria da ponte e as modificações aplicadas).

### Iluminação

* **Fontes:** Light (geral) e Point / Point.001 (luzes internas do poste).
* **Qualidade:** Iluminação ajustada para atmosfera (final de tarde/noite), com Point Lights simulando a fonte real do poste.

### Elementos Chave do Projeto

* **Dog Skeleton:** Essencial para a animação de caminhada do cão (rigging).
* **ponte:** O objeto principal de travessia.
* **Plane/Plane.001:** Compõem a base da cena (terreno e água).
* **Garden lamp post:** Elemento de ambientação e fonte de Fill Light.

### Animação

* **Foco:** Movimento do Dog Skeleton (ciclo de caminhada) e movimento da Camera.

---

Gostaria que eu detalhasse a função do **Dog Skeleton** e como ele se relaciona com a animação?