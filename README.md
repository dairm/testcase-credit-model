## Run


Давайте сгенерируем файлы 
Предобрабатываем файлы и собираем датасет

```sh
python preprocess_data.py -d ./data/credit_train.csv -t ./data/transactions.csv -g ./data/merchants_train.csv
```
Скорим моделькой наши файлы
```sh
python inference.py -m ./models/auto_woe.pkl -d ./dataset.csv
```

## Преданализ

1. Процент целевого события равен 17.6%
2. Портрет неблагонадежного заемщика мужчина 35 лет, брал кредит более 2 раз, со средним доходом 38 тыс, из региона ÎÁË ÌÎÑÊÎÂÑÊÀß
3. Средний портрет нашего клиента это женщина 36 лет, брала кредит более 2 раз, со средним доходом  40 тыс, из региона ÎÁË ÌÎÑÊÎÂÑÊÀß
4. Список регионов большим процентом дефота среди клиентов

        ['ÑÅÂÅÐÍÀß ÎÑÅÒÈß - ÀËÀÍÈß ÐÅÑÏ',
         'ÎÁË ÐßÇÀÍÑÊÀß',
         'ÐÅÑÏ ÊÀËÌÛÊÈß',
         'ÐÅÑÏ ÊÀÁÀÐÄÈÍÎ-ÁÀËÊÀÐÑÊÀß',
         'ÊÓÐÑÊÀß ÎÁË',
         'ÐÅÑÏ ÀËÒÀÉ',
         'ÐÅÑÏ ÊÀÐÀ×ÀÅÂÎ-×ÅÐÊÅÑÑÊÀß',
         'ÒÛÂÀ ÐÅÑÏ',
         'ÊÐÀÉ ÕÀÁÀÐÎÂÑÊÈÉ',
         'ÐÅÑÏ ÄÀÃÅÑÒÀÍ']

### Геоданные
Запустить файл ./output/map.html

### Качество
Модели | auto_woe | lightgbm |
--- | --- | --- |
Качество ROC AUC | 0.73 | 0.75 |  |

### Выходные данные
Важные фичи
output/feat_imp.png

Скоры по предсказанию
output/prediction.csv

Отчет по модели
reports/autowoe_report.html