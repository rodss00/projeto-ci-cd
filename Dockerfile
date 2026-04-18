# Usa a imagem oficial do Nginx (um servidor web muito rápido e leve)
FROM nginx:alpine

# Copia todos os arquivos da pasta atual para a pasta publica do Nginx
COPY . /usr/share/nginx/html

# Expõe a porta 80 (padrão web)
EXPOSE 80
