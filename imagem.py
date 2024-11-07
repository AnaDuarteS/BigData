import fitz  # PyMuPDF
import io
from PIL import Image

def extrair_imagens_pdf(pdf_path, output_folder):
    # Abrir o arquivo PDF
    doc = fitz.open(pdf_path)

    img_count = 0

    # Percorrer todas as páginas do PDF
    for i in range(len(doc)):
        pagina = doc.load_page(i)
        # Extrair imagens da página
        imagens = pagina.get_images(full=True)

        for img_index, img in enumerate(imagens):
            xref = img[0]
            imagem_bytes = doc.extract_image(xref)
            imagem_data = imagem_bytes["image"]

            # Salvar imagem
            imagem = Image.open(io.BytesIO(imagem_data))
            img_count += 1
            imagem.save(f"{output_folder}/imagem_{i + 1}_{img_count}.png")

    print(f"Total de imagens extraídas: {img_count}")

# Exemplo de uso
pdf_path = "Fundamentos-Engenharia-de-Dados.pdf"  # Nome do seu arquivo PDF
output_folder = "imagens_extraidas"  # Pasta onde as imagens serão salvas
extrair_imagens_pdf(pdf_path, output_folder)
