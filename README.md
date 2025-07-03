# Tradutor de Voz com Insight

Projeto em Flask + Azure Speech + Translator + OpenAI.

## Rotas
- `/`: interface HTML
- `/translate`: traduz texto do inglês para português
- `/insight`: gera insight com OpenAI GPT-4

## Requisitos
- Flask
- Azure Speech Services
- Azure Translator
- OpenAI Key

Configure as variáveis de ambiente no Azure App Service ou local via `.env`.
