```python
import numpy as np

def gerar_simulacao_imagem_satelite(larg=100, alt=100):
    canal_vermelho = np.full((alt, larg), 150, dtype=np.uint8)
    canal_verde = np.full((alt, larg), 100, dtype=np.uint8)
    canal_azul = np.full((alt, larg), 50, dtype=np.uint8)
    
    imagem_simulada_rgb = np.stack([canal_vermelho, canal_verde, canal_azul], axis=-1)
    return imagem_simulada_rgb

def processar_visualizacao_rgb(dados_imagem):
    
    media_r = dados_imagem[:, :, 0].mean()
    media_g = dados_imagem[:, :, 1].mean()
    media_b = dados_imagem[:, :, 2].mean()
    
    print(f"Valores médios das bandas simuladas (Mapeadas para R, G, B do display):")
    print(f"  Vermelho (R): {media_r:.2f}")
    print(f"  Verde (G): {media_g:.2f}")
    print(f"  Azul (B): {media_b:.2f}")
    print("Resultado: A imagem seria exibida com a tonalidade determinada pela mistura destas intensidades.")


if __name__ == "__main__":

    
    dados_satelite_simulados = gerar_simulacao_imagem_satelite()
    
    processar_visualizacao_rgb(dados_satelite_simulados)
    
    
    
```