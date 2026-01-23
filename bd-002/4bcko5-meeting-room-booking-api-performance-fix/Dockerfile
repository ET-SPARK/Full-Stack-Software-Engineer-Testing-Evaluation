FROM node:18-alpine

WORKDIR /app

COPY repository_before/server/package*.json ./

RUN npm install

COPY repository_before/server/ ./

EXPOSE 5000

CMD ["sh", "-c", "node seed.js && node index.js"]
