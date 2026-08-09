import re

with open('/Users/pasternak/Documents/antigravity/TopRentMoto/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Translations
translations = {
    'Rent KTM 1190 Adventure<br>in Italy': 'Арендовать KTM 1190 Adventure<br>в Санремо',
    'Home': 'Главная',
    'Location': 'Санремо',
    'Motos': 'Мотоциклы',
    'from 95€ / day': 'от 95€ / день',
    'Book now': 'Оформить заказ',
    'or Call now:': 'или Звоните сейчас:',
    'Moto Specifications': 'Спецификации мотоцикла',
    'Engine (cc)': 'Двигатель (куб.см)',
    'Power (hp)': 'Мощность (л.с.)',
    'Weight': 'Вес',
    'Number of cylinders': 'Кол-во цилиндров',
    'Rental Conditions': 'Условия аренды',
    'Age and CC deposit': 'Возраст и депозит',
    'For insurance reasons, the minimum age for rental is at least 18 years. A valid driver’s license is always required to rent a KTM 1190 Adventure in Italy, as well as a minimum amount of 1500 in your credit card, which is blocked on the rental period and released only after the return of the motorcycle.': 'По соображениям страховки минимальный возраст для аренды составляет не менее 18 лет. Для аренды KTM 1190 Adventure в Италии всегда требуются действующие водительские права, а также минимальная сумма 1500 на вашей кредитной карте, которая блокируется на период аренды и разблокируется только после возврата мотоцикла.',
    'Assurance': 'Страховка',
    'The moto insurance system (CASCO) which is applied to all vehicles provides collision damage to the rented vehicle, but does not cover such things as damages to other vehicles, property or injury to other persons.': 'Система мото-страхования (КАСКО), применяемая ко всем транспортным средствам, покрывает ущерб арендованному транспортному средству при столкновении, но не покрывает ущерб другим транспортным средствам, имуществу или травмы других лиц.',
    'Price and milleage': 'Цена и пробег',
    'The rental price does not include mileage. The cost of each kilometer 0.22.': 'В стоимость аренды не входит пробег. Стоимость каждого километра 0.22.',
    'Other Brand Models KTM': 'Другие модели KTM',
    'Reviews for KTM 1190 Adventure': 'Отзывы о KTM 1190 Adventure',
    'Write review': 'Написать отзыв',
    'Other Reviews': 'Другие отзывы',
    'Company Overview': 'Кратко о компании',
    'In our company you will find only new motorcycles for rent at affordable prices. In the Top Rent Moto fleet, everyone will find a suitable option...': 'В нашей компании вы найдете только новые мотоциклы в аренду по приемлемым ценам. В мотопарке Top Rent Moto каждый найдет для себя подходящий вариант...',
    'Call now:': 'Звоните сейчас:',
    'Motorcycles': 'Мотоциклы',
    'Services': 'Услуги',
    'About Us': 'О нас',
    'Read more': 'Читать далее',
    'Hide': 'Скрыть',
}

for eng, ru in translations.items():
    content = content.replace(eng, ru)

with open('/Users/pasternak/Documents/antigravity/TopRentMoto/ru.html', 'w', encoding='utf-8') as f:
    f.write(content)
