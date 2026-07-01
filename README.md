# News-Classifier

Пайплайн для ежедневного сбора новостей из RSS-фида, классификации их тональности и тематики с сохранением результатов в PostgreSQL.

## Что делает

- Забирает до 100 новостей из RSS-фида
- Пропускает уже обработанные новости (дедупликация по ссылке)
- Определяет тональность заголовка: `positive`, `neutral`, `negative`
- Определяет, связана ли новость с СВО
- Сохраняет результаты в PostgreSQL

## Модели

| Задача | Модель |
|---|---|
| Тональность | [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) |
| Тематика | [MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli](https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli) |

Обе модели работают локально на CPU, интернет-соединение нужно только для загрузки RSS.
