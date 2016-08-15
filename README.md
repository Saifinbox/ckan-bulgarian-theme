# Визуална тема на портала за отворени данни

В това хранилище е кодът на визуалната тема, използвана на [българския портал за отворени данни](https://opendata.government.bg).

За другите компоненти, съставящи портала, вижте [събирателното хранилище governmentbg/opendata](https://github.com/governmentbg/opendata).

## Стилове (CSS)

Стиловете в тази тема са написани на [SCSS](http://sass-lang.com/) и използват [Compass](http://compass-style.org/). Намират се в [ckanext/bulgarian_theme/fanstatic/extra.scss](ckanext/bulgarian_theme/fanstatic/extra.scss). За да ги променяте, е необходимо първо да имате инсталиран Compass. [Инструкции за това има тук](http://compass-style.org/install/).

Промените трябва да се правят по `.scss`-версията на файла, а не по резултатния `.css` файл.

Може да използвате следната команда, изпълнена от папката на проекта, за да генерирате автоматично `.css` файлове от променените `'.scss'` оригинали:

    compass compile

## Инсталация

Как се инсталира или обновява темата зависи от начина, по който е deploy-нат CKAN. За [инсталационни инструкции за opendata.government.bg портала, вижте това ръководство](https://github.com/governmentbg/opendata/blob/master/guides/update_theme.md).
